import sqlite3


class DAO:
    def add_single_job(self, company, title, level, url, date):
        con = sqlite3.connect('Jobs.db')
        cur = con.cursor()
        job = (company, title, level, url, date)
        cur.execute(
            "INSERT INTO Job(company, title, level, url, post_date) VALUES (?,?,?,?,?)",
            job)
        con.commit()
        con.close()

    def find_company(self, company):
        con = sqlite3.connect('Jobs.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM Job WHERE company=:comp', {'comp': company})
        # DEBUG
        # print(cur.fetchall())
        data = cur.fetchall()
        temp = ['id', 'company', 'title', 'level', 'url', 'date']
        values = {}
        #        print(data[0][5])
        #       print(type(data[0]))
        i = 0
        for x in temp:
            values.update({x: data[0][i]})
            #            print(data[0][i])
            i += 1
            # print(i)
        con.close()
        return values
        # return 'Done'
