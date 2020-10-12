import csv
import os


class FileManager:
    cwd = os.getcwd()

    def __init__(self, input_filename):
        self.input_filename = input_filename

    def convert_filename_to_svg(self, extra):
        return f'{os.path.splitext(self.input_filename)[0]}_{extra.lower()}.svg'

    def read_csv_dict_like(self):
        filepath = os.path.join(self.cwd, self.input_filename)

        if not os.path.isfile(filepath):
            raise FileNotFoundError

        with open(filepath, 'r') as csv_file:
            dict_like_data = [
                row for row in csv.DictReader(csv_file)
            ]

        return dict_like_data

    def generate_chart_file(self, chart_data, extra_filename):
        chart_data.render_to_file(
            os.path.join(
                self.cwd,
                self.convert_filename_to_svg(extra_filename),
            ),
        )
