from termcolor import colored
import util as util


def add_menu(job):
    local_exit = False
    while not local_exit:
        print('----------Add Job------------')
        print('Add single job: 1')
        print('Add application status: 2 ')
        print('exit: 0')
        # TODO make this a function to clean up the code in other function
        choice = input('enter choice: ')
        try:
            int(choice)
        except ValueError:
            print(colored('Please enter an integer', 'yellow'))
            continue
        if int(choice) == 1:
            job.add_job()
        elif int(choice) < 0 or int(choice) > 5:
            print('Not a valid selection')
        finished = input('are you finished? (y,n): ')
        if finished == 'y':
            local_exit = True


def search_menu(job):
    local_exit = False
    while not local_exit:
        print('----------Search for jobs------------')
        print('Find jobs by companay: 1')
        print('Find job application by status: 2')
        print('Find jobs not applied to yet: 3')
        print('exit: 0')
        choice = input('enter choice: ')
        try:
            int(choice)
        except ValueError:
            print(colored('Please enter an integer', 'yellow'))
            continue
        if int(choice) == 2:
            util.format(job.by_company())
        elif int(choice) == 5:
            job.app_status()
        elif int(choice) == 11:
            data = job.no_applied()
            util.format(data)
        elif int(choice) < 0 or int(choice) > 5:
            print('Not a valid selection')
        finished = input('are you finished? (y,n): ')
        if finished == 'y':
            local_exit = True


def update_menu(job):
    local_exit = False
    while not local_exit:
        print('----------Update Job information------------')
        print("Update application date: 1")
        print('Update application status: 2 ')
        print('Update response date: 3')
        print('Update number of interviews: 4 ')
        print('update if leet code: 5')
        print('Update if code challenge: 6')
        print('exit: 0')
        choice = input('enter choice: ')
        try:
            int(choice)
        except ValueError:
            print(colored('Please enter an integer', 'yellow'))
            continue
        if int(choice) == 4:
            job.fix_app_date()
            # what does this do?
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
            # TODO make this return to menu in the future
            if data is None:
                print('done')
            elif len(data) <= 0:
                print('Nothing with that status')
            else:
                util.format(data)
        elif int(choice) == 12:
            job.add_app_status()
        elif int(choice) < 0 or int(choice) > 5:
            print('Not a valid selection')
        finished = input('are you finished? (y,n): ')
        if finished == 'y':
            local_exit = True


def apply_menu(job):
    local_exit = False
    while not local_exit:
        print('----------Update Job information------------')
        print('Apply to Job: 1')
        print('exit: 0')
        choice = input('enter choice: ')
        try:
            int(choice)
        except ValueError:
            print(colored('Please enter an integer', 'yellow'))
            continue
        if int(choice) == 3:
            job.apply()
        elif int(choice) < 0 or int(choice) > 5:
            print('Not a valid selection')
        finished = input('are you finished? (y,n): ')
        if finished == 'y':
            local_exit = True
