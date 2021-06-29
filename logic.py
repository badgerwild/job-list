import datetime

import util
from DAO import DAO


# TODO implement changews to apply table in the select functions
class job_model:
    db = DAO()
    validate = db.status()[0]

    def add_job(self):
        company_name = input('enter company name: ')
        job_title = input('enter job title: ')
        job_level = input('enter job level: ')
        url = input('enter url: ')
        date = input('enter date poasted (yyyy-mm-dd): ')
        self.db.add_single_job(company_name, job_title, job_level, url, date)

    def by_company(self):
        company_name = input('enter company name: ')
        return self.db.find_company(company_name)

    def apply(self):
        company_name = input('enter company name: ')
        util.format(self.db.find_company(company_name))
        apply_to = input('enter job id from list: ')
        status = ''
        while status not in self.validate:
            print(self.validate)
            status = input('enter a valid status: ')
        date = str(datetime.date.today())
        cover_letter = input('Did you apply with a cover letter?(y, n) ')
        b_cover_letter = 0
        if str(cover_letter) == 'y':
            b_cover_letter = 1

        platform = input(
            'Enter the name of the application plaform (use \'company site\' for application on company website'
        )
        self.db.apply(apply_to, status, date, b_cover_letter, platform)

    def fix_app_date(self):
        date = input('enter date applied (yyyy-mm-dd): ')
        job_id = input('enter job id: ')
        self.db.update_date(job_id, str(date))

    def app_status(self):
        job_id = input('enter job id: ')
        status = input('Enter application status')
        while status not in self.validate:
            print(self.validate)
            status = input('enter a valid status: ')
        self.db.update_status(job_id, status)

    def response_date(self):
        job_id = input('enter job id: ')
        response_date = input("Enter response date")
        self.db.update_response_date(job_id, response_date)

    def interviews(self):
        job_id = input('enter job id: ')
        interviews = input('enter number of interviews: ')
        self.db.update_number_of_interviews(job_id, interviews)

    def leet_code(self):
        job_id = input('enter job id:')
        self.db.leet_code(job_id, 1)

    def code_challenge(self):
        job_id = input('enter job id')
        self.db.code_challenge(job_id, 1)

    def by_status(self):
        status = input('enter status ')
        if status not in self.validate:
            print("enter a valid selection from the following", self.validate)
            return
        return self.db.find_status(status)

    def no_applied(self):
        return self.db.not_applied()

    def add_app_status(self):
        status = input('Enter a new job application status')
        self.db.add_status(str(status))
