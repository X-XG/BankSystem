from itertools import chain
import re
import string
import pymysql


class account:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def _check(self, data: dict):
        if not (str.isalnum(data['account_id'])
                and len(data['account_id']) == 4):
            raise Exception('error: account_id format')
        elif not str.isalnum(data['branch_name']):
            raise Exception('error: branch_name format')
        elif re.match("^[-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+)$",
                      data['balance']) == None:
            raise Exception('error: balance format')
        elif re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                      data['open_date']) == None:
            raise Exception('error: open_date format')

    def _check_id(self, data):
        cursor = self.db.cursor()
        sql = "SELECT * FROM checking_account WHERE account_id='%s'" % data[
            'account_id']
        cursor.execute(sql)
        if len(cursor.fetchall()) != 0:
            raise Exception(
                'the account id %s has been used in checking account' %
                data['account_id'])

        sql = "SELECT * FROM saving_account WHERE account_id='%s'" % data[
            'account_id']
        cursor.execute(sql)
        if len(cursor.fetchall()) != 0:
            raise Exception(
                'the account id %s has been used in saving account' %
                data['account_id'])
        cursor.close()

    def check_checking(self, data: dict):
        self._check(data)
        if re.match("^[-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+)$",
                    data['overdraft']) == None:
            raise Exception('error: overdraft format')

    def check_saving(self, data: dict):
        self._check(data)
        if re.match("^[-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+)$",
                    data['rate']) == None:
            raise Exception('error: rate format')
        elif not str.isalnum(data['currency_type']):
            raise Exception('error: currency_type format')

    def check_insert(self, type: string, data: dict):
        client_id = str.upper(data['client_id'])
        cursor = self.db.cursor()
        if type == 'checking':
            sql = "SELECT branch_name FROM client_check_account, checking_account \
                WHERE client_check_account.account_id=checking_account.account_id \
                AND client_id='%s'" % client_id
        elif type == 'saving':
            sql = "SELECT branch_name FROM client_saving_account, saving_account \
                WHERE client_saving_account.account_id=saving_account.account_id \
                AND client_id='%s'" % client_id
        cursor.execute(sql)
        if data['branch_name'] in list(chain.from_iterable(cursor.fetchall())):
            raise Exception('the client has %s account in branch:%s' %
                            (type, data['branch_name']))

    def account_type(self, account_id: string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM checking_account WHERE account_id='%s'" % account_id
        cursor.execute(sql)
        if len(cursor.fetchall()) != 0:
            return 'checking'
        else:
            return 'saving'

    def insert(self, type, data: dict):
        cursor = self.db.cursor()
        if type == 'checking':
            self.check_checking(data)
            self._check_id(data)
            sql = "INSERT INTO checking_account VALUES('%s', '%s', '%s', '%s', '%s')" % \
                (str.upper(data['account_id']), data['branch_name'], data['balance'], data['open_date'], data['overdraft'])
            sql_c = "INSERT INTO client_check_account VALUES('%s', '%s', NOW())" % \
                (str.upper(data['client_id']), str.upper(data['account_id']))
        elif type == 'saving':
            self.check_saving(data)
            self._check_id(data)
            sql = "INSERT INTO saving_account VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % \
                (str.upper(data['account_id']), data['branch_name'], data['balance'], data['open_date'], data['rate'], data['currency_type'])
            sql_c = "INSERT INTO client_saving_account VALUES('%s', '%s', NOW())" % \
                (str.upper(data['client_id']), str.upper(data['account_id']))
        self.check_insert(type, data)
        try:
            cursor.execute(sql)
            cursor.execute(sql_c)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()

    def delete(self, id: string):
        cursor = self.db.cursor()
        sql = "DELETE FROM checking_account WHERE account_id='%s'" % id
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception("error: when delete accout '%s'" % id)

        sql = "DELETE FROM saving_account WHERE account_id='%s'" % id
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception("error: when delete accout '%s'" % id)
        cursor.close()

    def update(self, type, data):
        if type == 'checking':
            self.check_checking(data)
            sql = "UPDATE checking_account SET branch_name = '%s', balance = '%s', open_date = '%s', overdraft = '%s' WHERE account_id='%s'" % \
                (data['branch_name'], data['balance'], data['open_date'],data['overdraft'], data['account_id'])
        elif type == 'saving':
            self.check_saving(data)
            sql = "UPDATE saving_account SET branch_name = '%s', balance = '%s', open_date = '%s', rate = '%s', currency_type = '%s' WHERE account_id='%s'" % \
                (data['branch_name'], data['balance'], data['open_date'],data['rate'], data['currency_type'], data['account_id'])

        cursor = self.db.cursor()

        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception('error: update account format is wrong')
        cursor.close()

    def search(self, id: string):

        def result_checking2dict(result):
            _dict = dict(
                zip([x[0] for x in cursor.description], [x for x in result]))
            _dict['type'] = 'checking'
            return _dict

        def result_saving2dict(result):
            _dict = dict(
                zip([x[0] for x in cursor.description], [x for x in result]))
            _dict['type'] = 'saving'
            return _dict

        result_list = []

        cursor = self.db.cursor()
        sql = "SELECT * FROM checking_account WHERE account_id LIKE '%%%s%%'" % id
        cursor.execute(sql)
        result_list.extend(list(map(result_checking2dict, cursor.fetchall())))

        sql = "SELECT * FROM saving_account WHERE account_id LIKE '%%%s%%'" % id
        cursor.execute(sql)
        result_list.extend(list(map(result_saving2dict, cursor.fetchall())))
        cursor.close()
        return result_list

    def client_visit(self, account_id):

        def result2dict(result):
            return dict(
                zip([x[0] for x in cursor.description], [x for x in result]))

        cursor = self.db.cursor()
        sql = "SELECT * FROM client_check_account WHERE account_id='%s'" % account_id
        cursor.execute(sql)
        result_list = list(map(result2dict, cursor.fetchall()))
        if len(result_list) == 0:
            sql = "SELECT * FROM client_saving_account WHERE account_id='%s'" % account_id
            cursor.execute(sql)
            result_list = list(map(result2dict, cursor.fetchall()))
        cursor.close()
        return result_list

    def add_client_visit(self, client_id, account_id):
        type = self.account_type(account_id)
        cursor = self.db.cursor()
        if type == 'checking':
            sql_c = "INSERT INTO client_check_account VALUES('%s', '%s', NOW())" % \
                    (str.upper(client_id), str.upper(account_id))
        elif type == 'saving':
            sql_c = "INSERT INTO client_saving_account VALUES('%s', '%s', NOW())" % \
                    (str.upper(client_id), str.upper(account_id))

        data = self.search(account_id)[0]
        data['client_id'] = client_id
        self.check_insert(type, data)
        try:
            cursor.execute(sql_c)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()

    def delete_client_visit(self, client_id, account_id):
        type = self.account_type(account_id)
        cursor = self.db.cursor()
        if type == 'checking':
            sql_c = "DELETE FROM client_check_account WHERE client_id='%s' AND account_id='%s'" % \
                    (str.upper(client_id), str.upper(account_id))
        elif type == 'saving':
            sql_c = "DELETE FROM client_saving_account WHERE client_id='%s' AND account_id='%s'" % \
                    (str.upper(client_id), str.upper(account_id))
        try:
            cursor.execute(sql_c)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()
