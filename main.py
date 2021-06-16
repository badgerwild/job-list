from logic import job_model
#TODO chage to a cleaner dict struture to replicate a case switch statement instead of if elif
if __name__ == '__main__':
    job = job_model()
    exit = False

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
        print('Find job application by status: 10')
        print('Find jobs not applied to yet: 11')

        choice = input('enter choice: ')
        # TODO refactor to abstract logic from main view
        if int(choice) == 1:
            job.add_job()

        elif int(choice) == 2:
            job.by_company()

        elif int(choice) == 3:
            job.apply()

        elif int(choice) == 4:
            job.fix_app_date()

        elif int(choice) == 5:
            job.app_status()

        elif int(choice) == 6:
            job.response_date()

        elif int(choice) == 7:
            job.interviews()

        elif int(choice) == 8:
            job.leet_code()

        elif int(choice) == 9:
            job.code_challenge()

        elif int(choice) == 10:
            job.by_status()

        elif int(choice) == 11:
            job.no_applied()

        finished = input('are you finished? (y,n): ')

        if finished == 'y':
            exit = True
