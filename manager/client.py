import string
import pymysql


class client:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def insert(self, data: tuple):
        cursor = self.db.cursor()
        sql = "INSERT INTO client VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise Exception('error: insert client format is wrong')
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

    def update(self, client_id: string, data: tuple):
        cursor = self.db.cursor()
        sql = "UPDATE client SET name = '%s', phone = '%s', address = '%s', contact_name = '%s', contact_phone = '%s', contact_email='%s', relation='%s' WHERE client_id = '%s'" % (
            data + client_id)
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
        cursor.close()
        return cursor.fetchall()

    def search_name(self, name: string):
        cursor = self.db.cursor()
        sql = "SELECT * FROM client WHERE name LIKE '%%%s%%'" % name
        cursor.execute(sql)
        cursor.close()
        return cursor.fetchall()


a = client()
print(a.search_id('C003'))
try:
    a.delete('C002')
except Exception as e:
    print(e)
