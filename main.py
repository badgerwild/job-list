import datetime
from DAO import DAO


if __name__ == '__main__':
    db = DAO()
    exit = False
    validate = db.status()[0]

    while not exit:
        print('Welcome to job search app')
        print('Add single job: 1')
        print('Find jobs by companay: 2')
        print('Apply to Job: 3')
        print("Update application date: 4")
        print('Update application status: 5 ')
        print('Update response date: 6')
        print('Update number of interviews: 7 ')
        print('update if leet code: 8')
        print('Update if code challenge: 9')


        choice = input('enter choice: ')
    # TODO refactor to abstract logic from main view
        if int(choice) == 1:
            print('Yes!!')
            company_name = input('enter company name: ')
            job_title = input('enter job title: ')
            job_level = input('enter job level: ')
            url = input('enter url: ')
            date = input('enter date poasted (yyyy-mm-dd: ')
            db.add_single_job(company_name, job_title, job_level, url, date)

        elif int(choice) == 2:
            company_name = input('enter company name: ')
            print(db.find_company(company_name))

        elif int(choice) == 3:
            company_name = input('enter company name: ')
            print(db.find_company(company_name))
            apply_to = input('enter job id from list: ')
            status = ''
            while status not in validate:
                print(validate)
                status = input('enter a valid status: ')
            date = str(datetime.date.today())
            db.apply(apply_to, status, date)

        elif int(choice) == 4:
            date = input('enter date applied (yyyy-mm-dd): ')
            job_id = input('enter job id: ')
            db.update_date(job_id, str(date))

        elif int(choice) == 5:
            job_id = input('enter job id: ')
            status = input('Enter application status')
            while status not in validate:
                print(validate)
                status = input('enter a valid status: ')
            db.update_status(job_id, status)

        elif int(choice) == 6:
            job_id = input('enter job id: ')
            response_date = input("Enter response date")
            db.update_response_date(job_id, response_date)

        elif int(choice) == 7:
            job_id = input('enter job id: ')
            interviews = input('enter number of interviews: ')
            db.update_number_of_interviews(job_id, interviews)

        elif int(choice) == 8:
            job_id = input('enter job id:')
            db.leet_code(job_id, 1)

        elif int(choice) == 9:
            job_id = input('enter job id')
            db.code_challenge(job_id, 1)


        finished = input('are you finished? (y,n): ')

        if finished == 'y':
            exit = True
