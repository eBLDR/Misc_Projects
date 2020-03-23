import json
import os


class FileManager:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def get_file_path(self, file_name):
        return os.path.join(self.dir_path, file_name)

    @staticmethod
    def file_exists(file_path):
        if os.path.isfile(file_path):
            return True
        else:
            # File does not exist
            raise FileNotFoundError

    def read_file(self, file_name):
        file_path = self.get_file_path(file_name)
        if self.file_exists(file_path):
            with open(file_path, 'r') as json_file:
                try:
                    data = json.load(json_file)
                    return data if data else {}
                except json.decoder.JSONDecodeError:
                    # In case the file is corrupted
                    return {}

    def write_file(self, file_name, data):
        file_path = self.get_file_path(file_name)
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)

    def delete_file(self, file_name):
        file_path = self.get_file_path(file_name)
        if self.file_exists(file_path):
            os.unlink(file_path)

    def get_existing_users(self):
        users = []
        for item in os.listdir(self.dir_path):
            if item.endswith('.json'):
                users.append(item.split('.')[0])
        return users
