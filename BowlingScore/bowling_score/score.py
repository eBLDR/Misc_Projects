from bowling_score.frame import Frame


class Score:
    special_characters = {
        '-': 0,  # Missed
        '/': 1,  # Spare
        'X': 2,  # Strike
    }

    def __init__(self, json_data):
        self.json_data = json_data
        self.total_points = 0

    def calculate_points(self):
        for frame in self.get_frames_iterator():
            # TODO:
            pass

    def get_points(self):
        self.calculate_points()
        return self.total_points

    def get_frames_iterator(self):
        return [
            Frame(
                frame_number,
                self.json_data[str(frame_number)],
            ) for frame_number in
            sorted(
                [
                    int(frame_number) for frame_number in self.json_data.keys()
                ]
            )
        ]
