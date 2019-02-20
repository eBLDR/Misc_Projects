import argparse
import os
import random
import time

from multiprocessing import Process

import gui


class Kaizen:
    def __init__(self, interval=60, gui=False):
        # Use GUI - user console if False
        self.gui = gui

        # In seconds, interval between consecutive kaizen
        self.timedelta_seconds = interval * 60

        # Image
        self.image_name = 'BASIC_BG.gif'
        self.image_path = os.path.join(os.getcwd(), self.image_name)

        # Round counter
        self.current_round = 1

        # Exercise mapper
        self.exercises = {'Handstand Hold': {'series': 3,
                                             'seconds': 30},
                          'Rope Skipping': {'series': 3,
                                            'seconds': 60},
                          'Push Ups': {'series': 3,
                                       'repetitions': 15},
                          'Chest Opening': {'series': 1,
                                            'seconds': 180}
                          }

    def init(self):
        os.system('clear')
        if not self.gui:
            print('Let\'s KAIZEN!')

        while True:
            time.sleep(self.timedelta)
            self.round()

    def round(self):
        intro_text = '\nKaizen Time!\nRound # {}'.format(self.current_round)

        exercise = self.get_random_exercise()
        data = self.exercises.get(exercise)

        text = '{}:\n{} x {}'.format(exercise, data['series'], (str(data['seconds']) + '"') if data.get('seconds') else data['repetitions'])
        total_time = data['series'] * data['seconds'] if data.get('seconds') else data['repetitions']

        if not self.gui:
            self.console_round(intro_text, text, total_time)

        else:
            self.gui_round(intro_text, text, total_time)

        self.current_round += 1

    def get_random_exercise(self):
        return random.choice([exercise for exercise in self.exercises.keys()])

    def console_round(self, intro_text, text, total_time):
        print(intro_text)

        self.display_image()

        print(text)
        print('Go!')

        # Kaizen is ongoing...
        time.sleep(total_time)

        input('\n<enter> when you are done!\n')
        print('Good job! Next kaizen will be in {} minutes.\n'.format(self.timedelta_seconds / 60))

    def gui_round(self, intro_text, text, total_time):
        process = Process(target=gui.main, args=(self.image_path, intro_text, text, total_time))
        process.start()
        process.join()

    def display_image(self):
        os.system('see {}'.format(self.image_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kaizen')
    parser.add_argument('-i', '--interval', help='Interval in minutes between two consecutive Kaizen (60 by default)', type=int, default=60)
    parser.add_argument('--gui', help='Activate flag to use GUI (console by default)', action='store_true')
    args = parser.parse_args()

    kaizen = Kaizen(interval=args.interval, gui=args.gui)
    kaizen.init()
