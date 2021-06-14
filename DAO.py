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
        data = cur.fetchall()
        values = self.make_dict(data)
        con.close()
        return values

    def make_dict(self, data):
        keys = ['id', 'company', 'title', 'level', 'url', 'date']
        values = []
        for j in data:
            values.append(dict(zip(keys, j)))
        return values

    def apply(self, job_id, status, date):
        con = sqlite3.connect('Application')
        cur = con.cursor()
        application = (job_id, status, date)
        cur.execute(
            "INSERT INTO Application(job_id, status, submit_date) VALUES (?,?,?)",
            application)
        con.commit()
        con.close()

    def status(self):
        con = sqlite3.connect('Jobs.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM status')
        return cur.fetchall()
