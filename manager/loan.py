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
        sql = "INSERT INTO loan VALUES('%s', '%s', '%s', 'not issue')" % \
            (str.upper(data['loan_id']), data['branch_name'], data['loan_money'])
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
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