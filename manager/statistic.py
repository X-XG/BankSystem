import pymysql
import calendar


class statistic:

    def __init__(self) -> None:
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1',
                                  database='BankSystem')

    def sum(self, branch_name):

        def result2dict(result):
            return dict(
                zip([x[0] for x in cursor.description], [x for x in result]))

        result_list = []
        for i in range(1, 13):
            result_list.append({
                'month': calendar.month_name[i],
                'loan_sum': 0,
                'account_sum': 0,
                'checking_num': 0,
                'saving_num': 0
            })

        cursor = self.db.cursor()

        # loan_sum
        sql = " SELECT  MONTH(loan_date) AS month,\
                        SUM(loan_money) AS loan_sum \
                        FROM loan \
                        WHERE YEAR(loan_date)=2022 AND branch_name='%s' \
                        GROUP BY month \
                        ORDER BY month" % branch_name

        cursor.execute(sql)
        temp_list = list(map(result2dict, cursor.fetchall()))
        for x in temp_list:
            index = x['month'] - 1
            result_list[index]['loan_sum'] = x['loan_sum']

        #account_sum
        sql = " SELECT  MONTH(open_date) AS month,\
                        SUM(balance) AS account_sum \
                        FROM ( \
                            SELECT account_id, balance, open_date \
                            FROM saving_account \
                            WHERE branch_name='%s' \
                            UNION \
                            SELECT account_id, balance, open_date \
                            FROM checking_account \
                            WHERE branch_name='%s' \
                        ) \
                        AS account_all \
                        WHERE YEAR(open_date)=2022 \
                        GROUP BY month \
                        ORDER BY month" % (branch_name, branch_name)

        cursor.execute(sql)
        temp_list = list(map(result2dict, cursor.fetchall()))
        for x in temp_list:
            index = x['month'] - 1
            result_list[index]['account_sum'] = x['account_sum']

        # checking num
        sql = " SELECT  MONTH(open_date) AS month,\
                        COUNT(*) AS checking_num \
                        FROM checking_account \
                        WHERE YEAR(open_date)=2022 AND branch_name='%s' \
                        GROUP BY month \
                        ORDER BY month" % branch_name
        cursor.execute(sql)
        temp_list = list(map(result2dict, cursor.fetchall()))
        for x in temp_list:
            index = x['month'] - 1
            result_list[index]['checking_num'] = x['checking_num']

        # saving num
        sql = " SELECT  MONTH(open_date) AS month,\
                        COUNT(*) AS saving_num \
                        FROM saving_account \
                        WHERE YEAR(open_date)=2022 AND branch_name='%s' \
                        GROUP BY month \
                        ORDER BY month" % branch_name
        cursor.execute(sql)
        temp_list = list(map(result2dict, cursor.fetchall()))
        for x in temp_list:
            index = x['month'] - 1
            result_list[index]['saving_num'] = x['saving_num']

        cursor.close()

        loan_sum     = 0
        account_sum  = 0
        checking_num = 0
        saving_num   = 0
        for x in result_list:
            loan_sum     += x['loan_sum'    ]
            account_sum  += x['account_sum' ]
            checking_num += x['checking_num']
            saving_num   += x['saving_num'  ]
        
        result_list.append({
            'month'       : 'Total',
            'loan_sum'    : loan_sum,
            'account_sum' : account_sum,
            'checking_num': checking_num,
            'saving_num'  : saving_num  
        })

        return result_list
