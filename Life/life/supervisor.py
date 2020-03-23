import os
import sys

from collections import OrderedDict

from life.datamanager import DataManager
from life.filemanager import FileManager
from life import settings


class Supervisor:
    def __init__(self):
        self.existing_users = []
        self.user_name = ''
        self.file_name = ''
        self.sections = ['home', 'relatives', 'partner', 'friends', 'occupation']

        self.menu_options = OrderedDict()

        self.menu_options['list'] = {'func': self.list_all_entries,
                                     'repr': '[\033[1;33mList\033[0m] all entries.'}
        self.menu_options['add'] = {'func': self.add_entry,
                                    'repr': '[\033[1;33mAdd\033[0m] new entry.'}
        self.menu_options['delete'] = {'func': self.delete_entry,
                                       'repr': '[\033[1;33mDelete\033[0m] existing entry.'}
        self.menu_options['save'] = {'func': self.save_data,
                                     'repr': '[\033[1;32mSave\033[0m] data to file.'}
        self.menu_options['remove'] = {'func': self.delete_user,
                                       'repr': '[\033[1;31mRemove\033[0m] user.'}
        self.menu_options['exit'] = {'func': self.exit_,
                                     'repr': '[\033[1;34mExit\033[0m] app.'}

        # Engines
        self.file_manager = None
        self.data_manager = None
        self.image_engine = None

    def exit_(self, auto_save=True):
        if auto_save:
            self.save_data()
        print('Exiting...')
        sys.exit()

    def run(self):
        self.initialise()
        while True:
            option = self.get_menu_option()
            self.menu_options[option]['func']()
            input('\n<enter>')

    def initialise(self):
        os.system('clear')
        print('### ## #  LIFE  # ## ###\n')
        self.file_manager = FileManager(settings.DATA_PATH)
        self.data_manager = DataManager(self.sections)
        # self.image_engine =

        self.existing_users = self.file_manager.get_existing_users()
        self.set_user_name()
        self.file_name = self.user_name + '.json'
        self.load_data()

    # User management
    def set_user_name(self):
        print('Existing users:\n- {}\n'.format('\n- '.join(self.existing_users)))
        while True:
            user_name = input('User name:\n> ').lower()
            if user_name:
                if user_name not in self.existing_users:
                    if input('Create new user \033[1;34m{}\033[0m [y/*]:\n> '.format(user_name)).lower() == 'y':
                        self.user_name = user_name
                        print('New user \033[1;34m{}\033[0m created.'.format(user_name))
                        break
                else:
                    self.user_name = user_name
                    print('\nLogged as user \033[1;34m{}\033[0m.'.format(user_name))
                    break

    def delete_user(self):
        if input('Are you sure to delete user \033[1;31m{}\033[0m [y/n]:\n> '.format(self.user_name)).lower() =='y':
            self.file_manager.delete_file(self.file_name)
            print('User and corresponding data deleted.')
            self.exit_(auto_save=False)

    # Data management
    def load_data(self):
        if self.user_name in self.existing_users:
            self.data_manager.data = self.file_manager.read_file(self.file_name)
            print('Data loaded from file.')
        else:
            self.data_manager.data = {}

    def save_data(self):
        self.file_manager.write_file(self.file_name, self.data_manager.data)
        print('\nData saved to file.')

    # Menu options
    def get_menu_option(self):
        menu_str = '{0}{1}{0}'.format(settings.SEP, '\n'.join(self.menu_options[key]['repr'] for key in self.menu_options.keys()))
        print(menu_str)
        while True:
            option = input('> ').lower()
            if option in self.menu_options.keys():
                return option

    def list_all_entries(self):
        self.data_manager.list_all_entries(self.sections)

    def add_entry(self):
        self.data_manager.add_entry()

    def delete_entry(self):
        self.data_manager.delete_entry()
