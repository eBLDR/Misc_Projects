from bowling_score.frame import Frame


class Score:
    missed = '-'
    spare = '/'
    strike = 'X'

    consecutive_throws_mapper = {
        spare: 1,
        strike: 2,
    }

    def __init__(self):
        self.json_data = {}
        self.frames = {}
        self.total_points = 0

    def calculate(self, json_data):
        self.json_data = json_data
        self.frames = self.get_frames()
        self.calculate_points()
        return self.total_points

    def get_frames(self):
        return {
            frame_number: Frame(
                frame_number,
                self.json_data[str(frame_number)],
            ) for frame_number in
            sorted(
                [
                    int(frame_number) for frame_number in self.json_data.keys()
                ]
            )
        }

    def calculate_points(self):
        for frame in self.frames.values():
            frame.points += self.get_pin_points(frame)

            # Bonus points
            if frame.number < len(self.frames) and any(
                    [
                        throw in [self.spare, self.strike]
                        for throw in frame.throws
                    ]
            ):
                frame.points += self.get_bonus_points(frame)

            self.total_points += frame.points

    def get_pin_points(self, frame):
        return self.calculate_points_from_throws(frame.throws)

    def get_bonus_points(self, frame):
        return self.calculate_points_from_throws(
            self.get_next_throws(
                frame.number,
                how_many=self.consecutive_throws_mapper[
                    frame.throws[-1]
                ],
            )
        )

    def calculate_points_from_throws(self, throws):
        points = 0

        for position, throw in enumerate(throws):
            points += self.interpret_throw(
                throw,
                previous_throw=throws[position - 1] if position > 0 else None,
            )

        return points

    def interpret_throw(self, throw, previous_throw=None):
        if throw.isdigit():
            return int(throw)

        elif throw == self.missed:
            return 0

        elif throw == self.strike:
            return 10

        elif throw == self.spare and previous_throw:
            return 10 - self.interpret_throw(previous_throw)

    def get_next_throws(self, current_frame_number, how_many):
        throw_generator = self.next_throw_generator(current_frame_number + 1)
        return [
            next(throw_generator) for _ in range(how_many)
        ]

    def next_throw_generator(self, start_frame_number):
        remaining_throws = []

        for frame_number in range(start_frame_number, len(self.frames) + 1):
            remaining_throws += self.frames[frame_number].throws

        for throw in remaining_throws:
            yield throw
