import datetime
from DAO import DAO

db = DAO()

exit = False
validae = db.status()

while not exit:
    print('Welcome to job search app')
    print('Add single job: 1')
    print('Find jobs by companay: 2')
    print('Apply to Job: 3')

    choice = input('enter choice: ')
#TODO refactor to abstract logic from main view
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
        while status not in validae:
            print(validae)
            status = input('enter a valid status: ')
        date = datetime.date
        db.apply(apply_to, status, date)

    finished = input('are you finished? (y,n): ')

    if finished == 'y':
        exit = True
