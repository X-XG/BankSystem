import string
import pymysql


class client:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def add(self):
        pass

    def delete(self, id):
        pass

    def modify(self):
        pass

    def search(self, id: string):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM client WHERE client_id=\'%s\'' % id
        cursor.execute(sql)
        return cursor.fetchall()


a = client()
a.search('4I5V4FS10E8RUMFL3')
