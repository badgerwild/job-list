import sqlite3


class DAO:
    def connect(self):
        con = sqlite3.connect('Jobs.db')
        cur = con.cursor()
        return con, cur

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
        con = sqlite3.connect('Jobs.db')
        cur = con.cursor()
        application = (job_id, status, date)
        cur.execute(
            "INSERT INTO Application(job_id, status, submit_date) VALUES (?,?,?)",
            application)
        con.commit()
        con.close()

    def update_date(self, job_id, date):
        con, cur = self.connect()
        data = (date, job_id)
        cur.execute(
            "UPDATE Application SET response_date=? WHERE job_id=?", data
        )
        con.commit()
        con.close()

    def update_status(self, job_id, status):
        con, cur = self.connect()
        data = (job_id, status)
        cur.execute(
            "UPDATE Application SET status=? WHERE job_id=?", data
        )
        con.commit()
        con.close()

    def update_response_date(self, job_id, date):
        con, cur = self.connect()
        data = (job_id, date)
        cur.execute(
            "UPDATE Application SET response_date=? WHERE job_id=?", data
        )
        con.commit()
        con.close()

    def update_number_of_interviews(self, job_id, number):
        con, cur = self.connect()
        data = (job_id, number)
        cur.execute(
            "UPDATE Application SET number_of_interviews=? WHERE job_id=?", data
        )
        con.commit()
        con.close()

    def leet_code(self, job_id, leet):
        con, cur = self.connect()
        data = (job_id, leet)
        cur.execute(
            "UPDATE Application SET leet_code=? WHERE job_id=?", data
        )
        con.commit()
        con.close()

    def code_challenge(self, job_id, value):
        con, cur = self.connect()
        data = (job_id, value)
        cur.execute(
            "UPDATE Application SET leet_code=? WHERE job_id=?", data
        )
        con.commit()
        con.close()

    def status(self):
        con = sqlite3.connect('Jobs.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM status')
        return cur.fetchall()

    # TODO test on the DB
    def find_status(self, status):
        con, cur = self.connect()
        cur.execute(
            "SELECT * FROM Jobs WHERE job_id IN (SELECT job_id FROM Application WHERE status=?)", status
        )
        data = cur.fetchall()
        values = self.make_dict(data)
        return values

