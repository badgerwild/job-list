import sys
from termcolor import colored
from logic import job_model
import util as util

job = job_model()

if __name__ == '__main__':

    exit = False

    while not exit:
        print('------------------Welcome to job search app------------------')
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
        print('Add application status: 12 ')
        print('exit: 0')

        choice = input('enter choice: ')
        try:
            int(choice)

        except ValueError:
            print(colored('Please enter an integer', 'yellow'))
            continue

        if int(choice) == 1:
            job.add_job()

        elif int(choice) == 2:
            util.format(job.by_company())

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
            data = job.by_status()
            #TODO make this return to menu in the future
            if data is None:
                print('done')
            elif len(data) <= 0:
                print('Nothing with that status')
            else:
                util.format(data)

        elif int(choice) == 11:
            data = job.no_applied()
            util.format(data)

        elif int(choice) == 12:
            job.add_app_status()

        elif int(choice) == 0:
            sys.exit()

        elif int(choice) < 0 or int(choice) > 12:
            print('Not a valid selection')

        finished = input('are you finished? (y,n): ')

        if finished == 'y':
            exit = True
