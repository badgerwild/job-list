import sys
from termcolor import colored
from logic import job_model
import util as util
import menu_util as menu

if __name__ == '__main__':
    job = job_model()
    exit = False
    while not exit:
        print('------------------Welcome to job search app------------------')
        print('Add: 1')
        print('Search: 2')
        print('Update: 3')
        print('Apply: 4')
        print('exit: 0')
        choice = input('enter choice: ')
        try:
            int(choice)
        except ValueError:
            print(colored('Please enter an integer', 'yellow'))
            continue
        if int(choice) == 1:
            menu.add_menu(job)
        elif int(choice) == 2:
            menu.search_menu(job)
        elif int(choice) == 3:
            menu.update_menu(job)
        elif int(choice) == 4:
            menu.apply_menu(job)
        elif int(choice) == 0:
            sys.exit()
        elif int(choice) < 0 or int(choice) > 5:
            print('Not a valid selection')
        finished = input('are you finished? (y,n): ')
        if finished == 'y':
            exit = True
