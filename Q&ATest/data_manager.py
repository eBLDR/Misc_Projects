import json

FILENAME = 'data.json'


class Data_Manager:
    def __init__(self):
        self.filename = FILENAME
        self.data = []

        self.init_manager()

    def init_manager(self):
        self.read_file()

    def read_file(self):
        with open(self.filename, 'r') as file:
            self.data = json.load(file)['data']



