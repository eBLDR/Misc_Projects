# DAILY TIME USE
# 1) Time
# 2) Decide how to use time
import pygal


class Topic:
    def __init__(self, label, hours):
        self.label = label
        self.hours = hours


class TimeUse:
    def __init__(self):
        self.hours_available = 24

        self.topics = []  # A list of objects Topic

    def populate_topics(self):
        while self.hours_available > 0:
            self.get_topic_from_user()

    def get_topic_from_user(self):
        print(f'Hours available: {self.hours_available}')

        while True:
            label = input('Label: ')
            if label:
                break

        while True:
            hours = input('Hours: ')
            if hours.isdigit() and hours != '0':
                hours = int(hours)

                if hours <= self.hours_available:
                    break

                print('Exceeding time!')

        self.topics.append(
            Topic(
                label=label,
                hours=hours,
            )
        )

        self.hours_available -= hours

    def display_topics(self):
        print('Topics:')
        for topic in self.topics:
            print(f'{topic.label}: {topic.hours}')

    def generate_chart(self):
        pie_chart = pygal.Pie()
        pie_chart.title = 'Daily Time Use'

        for topic in self.topics:
            pie_chart.add(topic.label, topic.hours)

        pie_chart.render_to_file('daily_time_use.svg')


if __name__ == '__main__':
    time_use = TimeUse()
    time_use.populate_topics()
    time_use.display_topics()
    time_use.generate_chart()
