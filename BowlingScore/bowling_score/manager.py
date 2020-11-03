from bowling_score.file_manager import FileManager
from bowling_score.output_display import OutputDisplay
from bowling_score.score import Score


class Manager:
    def __init__(self):
        self.file_manager = FileManager()
        self.score = Score()
        self.output_display = OutputDisplay()

    def main(self):
        total_points = self.score.calculate(
            self.file_manager.read_json(),
        )
        self.output_display.display(total_points)
