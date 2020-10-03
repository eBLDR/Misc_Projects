"""
Times are expressed in minutes.

CSV file format:

label[str],category[str],flag[bool],minutes[int/float]
label1,category1,true,minutes1
label2,category1,false,minutes2
...,...
"""
import pygal
from data.activity import Activity, ActivityList
from data.constants import DAILY_MINUTES
from data.file_manager import FileManager
from pygal.style import NeonStyle as Style

# Chart config
config = pygal.Config()
config.style = Style
config.show_legend = True


class TimeExceededException(Exception):
    def __init__(self, used_time, max_time):
        self.msg = f'Used time ({used_time}) exceeds max possible time ({max_time})'


class TimeUse:
    def __init__(
            self,
            input_filename,
            auto=True,
            display_unassigned=True,
    ):
        # Mode `auto` for reading csv file, manual user input otherwise.
        self.auto = auto

        # Enable to generate "unassigned" activity to represent unassigned time
        self.display_unassigned = display_unassigned

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

        self.generate_data_charts()

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

    def generate_data_charts(self):
        self.generate_by_activity()
        self.generate_by_category()
        self.generate_by_flag()

    def generate_by_activity(self):
        """Generate a simple pie chart."""
        type_ = 'Activities'
        pie_chart = pygal.Pie(config=config)
        pie_chart.title = type_

        for activity in self.activities:
            pie_chart.add(
                activity.label, activity.daily_percentage,
            )

        self.file_manager.generate_chart_file(
            pie_chart,
            type_,
        )

    def generate_by_category(self):
        """Generate a multi-series pie chart grouping by category."""
        type_ = 'Categories'
        pie_chart = pygal.Pie(config=config)
        pie_chart.title = type_

        for category in self.activities.categories:
            values = []
            for activity in self.activities.get_all_items_by_category(
                    category,
            ):
                values.append(
                    {
                        'value': activity.daily_percentage,
                        'label': activity.label,
                    }
                )

            pie_chart.add(
                title=category,
                values=values,
            )

        self.file_manager.generate_chart_file(
            pie_chart,
            type_,
        )

    def generate_by_flag(self):
        """Generate a multi-series pie chart grouping by category."""
        type_ = 'Flag'
        pie_chart = pygal.Pie(config=config)
        pie_chart.title = type_

        true_time = 0
        false_time = 0
        none_time = 0

        for activity in self.activities:
            if activity.flag is True:
                true_time += activity.daily_percentage
            elif activity.flag is False:
                false_time += activity.daily_percentage
            elif activity.flag is None:
                none_time += activity.daily_percentage

        mapper = (
            ('true', true_time),
            ('false', false_time),
            ('none', none_time),
        )

        for label, value in mapper:
            pie_chart.add(
                label, value
            )

        self.file_manager.generate_chart_file(
            pie_chart,
            type_,
        )
