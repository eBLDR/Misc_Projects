import json
import os


class FileManager:
    file_path = os.path.join(os.getcwd(), 'bowling_score', 'score.json')

    def read_json(self):
        with open(self.file_path) as json_file:
            content = json.load(json_file)

        return content
