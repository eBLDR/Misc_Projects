"""
Times are expressed in minutes.
"""
import csv
import os

import pygal
from pygal.style import NeonStyle as Style

# Chart config
config = pygal.Config()
config.style = Style
config.show_legend = True

DAILY_MINUTES = 1440


class TimeExceededException(Exception):
    def __init__(self, used_time, max_time):
        self.msg = f'Used time ({used_time}) exceeds max possible time ({max_time})'


class Activity:
    def __init__(self, label, minutes):
        self.label = label
        self.minutes = minutes
        self.daily_percentage = minutes * 100 / DAILY_MINUTES


class TimeUse:
    # Mode `auto` for reading csv file, manual user input otherwise.
    auto = True

    # Enable to generate "unassigned" activity to represent unassigned time
    display_unassigned = True

    def __init__(self):
        self.file_manager = FileManager()

        self.user_name = ''

        self.minutes_available = DAILY_MINUTES

        self.activities = []

    def run(self):
        self.get_user_name()

        if self.auto:
            self.get_activities_from_csv_file()

            try:
                self.assert_time()
            except TimeExceededException as e:
                print(e.msg)

        else:
            self.get_activities_from_user_input()

        if self.display_unassigned:
            self.generate_unassigned_time_activity()

        self.file_manager.generate_chart(
            self.user_name,
            self.activities,
        )

    def get_user_name(self):
        while not self.user_name:
            if user_name := input('User name: '):
                self.user_name = user_name

    def get_activities_from_csv_file(self):
        for row in self.file_manager.read_csv():
            self.activities.append(
                Activity(
                    label=row[0],
                    minutes=int(row[1]),
                ),
            )

    def get_activities_from_user_input(self):
        while self.minutes_available > 0:
            self.get_activity_from_user_input()

    def get_activity_from_user_input(self):
        print(f'Minutes available: {self.minutes_available}')

        while True:
            label = input('Label: ')
            if label:
                break

        while True:
            minutes = input('Minutes: ')
            if minutes.isdigit() and minutes != '0':
                minutes = int(minutes)

                if minutes <= self.minutes_available:
                    break

                print('Exceeding time!')

        self.activities.append(
            Activity(
                label=label,
                minutes=minutes,
            )
        )

        self.minutes_available -= minutes

    def count_activities_total_time(self):
        total_time = 0
        for activity in self.activities:
            total_time += activity.minutes

        return total_time

    def assert_time(self):
        used_time = self.count_activities_total_time()
        if used_time > DAILY_MINUTES:
            raise TimeExceededException(used_time, DAILY_MINUTES)

    def generate_unassigned_time_activity(self):
        minutes_unassigned = DAILY_MINUTES - self.count_activities_total_time()
        self.activities.append(
            Activity(
                label='unassigned',
                minutes=minutes_unassigned,
            ),
        )

    def display_activities(self):
        print('Activities:')
        for activity in self.activities:
            print(f'{activity.label}: {activity.minutes}')


class FileManager:
    cwd = os.getcwd()
    input_filename = 'daily_activity_time.csv'
    output_filename = 'daily_activity_time_{title}.svg'

    def read_csv(self):
        filepath = os.path.join(self.cwd, self.input_filename)

        with open(filepath, 'r') as csv_file:
            raw_data = [
                row for row in csv.reader(csv_file)
            ]

        return raw_data

    def generate_chart(self, title, activities):
        pie_chart = pygal.Pie(config=config)
        pie_chart.title = title

        for activity in activities:
            pie_chart.add(
                activity.label, activity.minutes,
            )

        filepath = os.path.join(
            self.cwd,
            self.output_filename.format(title=title),
        )
        pie_chart.render_to_file(filepath)


if __name__ == '__main__':
    time_use = TimeUse()
    time_use.run()
