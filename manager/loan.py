import re
import string
import pymysql


class loan:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def _check(self, data: dict):
        if not (str.isalnum(data['loan_id']) and len(data['loan_id']) == 4):
            raise Exception('error: loan_id format')
        elif not str.isalnum(data['branch_name']):
            raise Exception('error: branch_name format')
        elif re.match("^[-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+)$",
                      data['loan_money']) == None:
            raise Exception('error: loan_money format')
        elif re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                      data['loan_date']) == None:
            raise Exception('error: loan_date format')

    def search(self, id: string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM loan WHERE loan_id LIKE '%%%s%%'" % id
        cursor.execute(sql)

        def result2dict(result):
            return dict(
                zip([x[0] for x in cursor.description], [x for x in result]))

        result_list = list(map(result2dict, cursor.fetchall()))
        cursor.close()
        return result_list

    def insert(self, data: dict):
        cursor = self.db.cursor()
        self._check(data)
        sql = "INSERT INTO loan VALUES('%s', '%s', '%s', 'not issue', '%s')" % \
            (str.upper(data['loan_id']), data['branch_name'], data['loan_money'], data['loan_date'])
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()

    def delete(self, id: string):
        cursor = self.db.cursor()
        if self.search(id)[0]['status'] == 'issuing':
            raise Exception('could not delete because issuing')
        sql = "DELETE FROM loan WHERE loan_id='%s'" % id
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception("error: when delete accout '%s'" % id)
        cursor.close()

    def client_loan(self, loan_id):

        def result2dict(result):
            return dict(
                zip([x[0] for x in cursor.description], [x for x in result]))

        cursor = self.db.cursor()
        sql = "SELECT * FROM client_loan WHERE loan_id='%s'" % loan_id
        cursor.execute(sql)
        result_list = list(map(result2dict, cursor.fetchall()))
        cursor.close()
        return result_list

    def add_client_loan(self, client_id, loan_id):
        cursor = self.db.cursor()
        sql_c = "INSERT INTO client_loan VALUES('%s', '%s')" % \
                (str.upper(client_id), str.upper(loan_id))
        try:
            cursor.execute(sql_c)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()

    def delete_client_loan(self, client_id, loan_id):
        cursor = self.db.cursor()
        sql_c = "DELETE FROM client_loan WHERE client_id='%s' AND loan_id='%s'" % \
                (str.upper(client_id), str.upper(loan_id))
        try:
            cursor.execute(sql_c)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()

    def pay_loan(self, loan_id):

        def result2dict(result):
            return dict(
                zip([x[0] for x in cursor.description], [x for x in result]))

        cursor = self.db.cursor()
        sql = "SELECT * FROM pay_loan WHERE loan_id='%s'" % loan_id
        cursor.execute(sql)
        result_list = list(map(result2dict, cursor.fetchall()))
        cursor.close()
        return result_list

    def issue(self, loan_id, pay_money):

        loan_money = self.search(loan_id)[0]['loan_money']
        paid_money = 0
        paid_list = self.pay_loan(loan_id)
        for paid in paid_list:
            paid_money += paid['pay_money']

        if paid_money + pay_money > loan_money:
            raise Exception('pay_money is more than not issued')

        if abs(loan_money - paid_money - pay_money) < 0.1:
            status = 'issued'
        else:
            status = 'issuing'

        cursor = self.db.cursor()
        sql = "INSERT INTO pay_loan VALUES('%s', NOW(), '%s')" % \
                (str.upper(loan_id), str(pay_money))
        sql2 = "UPDATE loan SET status = '%s' WHERE loan_id='%s'" % (
            status, str.upper(loan_id))

        try:
            cursor.execute(sql)
            cursor.execute(sql2)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()
