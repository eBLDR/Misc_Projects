"""
Times are expressed in minutes.

CSV file format:

label,minutes
label1,minutes1
label2,minutes2
...,...
"""
import argparse
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
    def __init__(self, label, minutes, category=None):
        self.label = label
        self.minutes = minutes
        self.category = category
        self.daily_percentage = minutes * 100 / DAILY_MINUTES

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            label=dict_data.get('label'),
            minutes=int(dict_data.get('minutes', 0)),
            category=dict_data.get('category'),
        )


class ActivityList(list):
    def __init__(self):
        super().__init__()
        self.categories = set()

    def append(self, new_object):
        super().append(new_object)
        self.categories.add(new_object.category)

    def get_all_items_by_category(self, category):
        return [
            object_ for object_ in self if object_.category == category
        ]


class TimeUse:
    def __init__(
            self,
            input_filename,
            auto=True,
            display_unassigned=True,
            group_by_category=False,
    ):
        # Mode `auto` for reading csv file, manual user input otherwise.
        self.auto = auto

        # Enable to generate "unassigned" activity to represent unassigned time
        self.display_unassigned = display_unassigned

        # Enable to render a multi-series pie chart grouping by category
        self.group_by_category = group_by_category

        self.file_manager = FileManager(input_filename)

        self.user_name = ''
        self.minutes_available = DAILY_MINUTES
        self.activities = ActivityList()

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

        self.file_manager.generate_chart_file(
            self.generate_chart_data(),
        )

    def get_user_name(self):
        while not self.user_name:
            if user_name := input('User name: '):
                self.user_name = user_name

    def get_activities_from_csv_file(self):
        for activity in self.file_manager.read_csv_dict_like():
            self.activities.append(
                Activity.from_dict(activity),
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
                category='unassigned',
            ),
        )

    def display_activities(self):
        print('Activities:')
        for activity in self.activities:
            print(f'{activity.label}: {activity.minutes}')

    def generate_chart_data(self):
        pie_chart = pygal.Pie(config=config)
        pie_chart.title = self.user_name

        if not self.group_by_category:
            for activity in self.activities:
                pie_chart.add(
                    activity.label, activity.minutes,
                )

        else:
            self.populate_by_category(pie_chart)

        return pie_chart

    def populate_by_category(self, pie_chart):
        for category in self.activities.categories:
            values = []
            for activity in self.activities.get_all_items_by_category(
                    category,
            ):
                values.append(
                    {
                        'value': activity.minutes,
                        'label': activity.label,
                    }
                )

            pie_chart.add(
                title=category,
                values=values
            )


class FileManager:
    cwd = os.getcwd()

    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.output_filename = self.convert_filename_to_svg(input_filename)

    @staticmethod
    def convert_filename_to_svg(filename):
        return os.path.splitext(filename)[0] + '.svg'

    def read_csv_dict_like(self):
        filepath = os.path.join(self.cwd, self.input_filename)

        if not os.path.isfile(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as csv_file:
            dict_like_data = [
                row for row in csv.DictReader(csv_file)
            ]

        return dict_like_data

    def generate_chart_file(self, chart_data):
        chart_data.render_to_file(
            os.path.join(
                self.cwd,
                self.output_filename,
            ),
        )


def main():
    parser = argparse.ArgumentParser(description='Daily Activity Time')
    parser.add_argument('file', help='Input csv file')
    parser.add_argument(
        '-m',
        '--manual',
        help='Enable to get data from user input instead of csv file',
        action='store_true',
    )
    parser.add_argument(
        '-hu',
        '--hide_unassigned',
        help='Enable to hide auto-generated "unassigned" activity',
        action='store_true',
    )
    parser.add_argument(
        '-g',
        '--group_by_category',
        help='Enable to generate a multi-series chart grouped by category',
        action='store_true',
    )

    args = parser.parse_args()
    input_filename = args.file
    auto = not args.manual
    display_unassigned = not args.hide_unassigned
    group_by_category = args.group_by_category

    time_use = TimeUse(
        input_filename,
        auto=auto,
        display_unassigned=display_unassigned,
        group_by_category=group_by_category,
    )

    time_use.run()


if __name__ == '__main__':
    main()
