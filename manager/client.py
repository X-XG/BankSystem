import string
import pymysql
import re


class client:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def check(self, data: dict):
        if not (str.isalnum(data['client_id'])
                and len(data['client_id']) == 4):
            raise Exception('error: client_id format')
        elif not str.isalpha(data['name']):
            raise Exception('error: client_name format')
        elif not str.isdigit(data['phone']):
            raise Exception('error: client_phone format')
        elif len(data['address']) == 0:
            raise Exception('error: address is empty')
        elif not str.isalpha(data['contact_name']):
            raise Exception('error: contact_name format')
        elif not str.isdigit(data['contact_phone']):
            raise Exception('error: contact_phone format')
        elif re.match(
                "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
                data['contact_email']) == None:
            raise Exception('error: contact_email format')
        elif not str.isalpha(data['relation']):
            raise Exception('error: relation format')

    def insert(self, data: dict):
        self.check(data)
        cursor = self.db.cursor()
        sql = "INSERT INTO client VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
            (str.upper(data['client_id']), data['name'], data['phone'], data['address'], \
            data['contact_name'], data['contact_phone'], data['contact_email'], data['relation'])
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(e)
        cursor.close()

    def delete(self, id: string):
        cursor = self.db.cursor()
        sql = "DELETE FROM client WHERE client_id='%s'" % id
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception('error: the client has account or loan')
        cursor.close()

    def update(self, data: dict):
        self.check(data)
        cursor = self.db.cursor()
        sql = "UPDATE client SET name = '%s', phone = '%s', address = '%s', contact_name = '%s', contact_phone = '%s', contact_email='%s', relation='%s' WHERE client_id = '%s'" % \
            (data['name'], data['phone'], data['address'], data['contact_name'], \
             data['contact_phone'], data['contact_email'], data['relation'], str.upper(data['client_id']))
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception('error: update client format is wrong')
        cursor.close()

    def search_id(self, id: string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM client WHERE client_id='%s'" % id
        cursor.execute(sql)
        result = dict(
            zip([x[0] for x in cursor.description],
                [x for x in cursor.fetchone()]))
        cursor.close()
        return result

    def search_name(self, name: string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM client WHERE name LIKE '%%%s%%'" % name
        cursor.execute(sql)

        def result2dict(result):
            return dict(
                zip([x[0] for x in cursor.description], [x for x in result]))

        result_list = list(map(result2dict, cursor.fetchall()))
        cursor.close()
        return result_list


# a = client()
# print(a.search_name('a'))
# try:
#     a.delete('C002')
# except Exception as e:
#     print(e)
