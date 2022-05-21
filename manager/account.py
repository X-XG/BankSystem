import pymysql


class account:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def insert_checking(self, data: dict):
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

    def delet(self):
        pass

    def update(self):
        pass

    def search(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM checking_account WHERE account_id='%s'" % id
        cursor.execute(sql)
        result = dict(
            zip([x[0] for x in cursor.description],
                [x for x in cursor.fetchone()]))
        cursor.close()
        return result

