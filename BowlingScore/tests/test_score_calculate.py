import unittest

from bowling_score.score import Score


class ScoreCalculateTest(unittest.TestCase):

    def test_only_numbers(self):
        json_data = {
            "1": ["5", "2"],
            "2": ["3", "6"],
            "3": ["8", "1"],
            "4": ["4", "2"],
            "5": ["1", "5"],
            "6": ["7", "1"],
            "7": ["6", "3"],
            "8": ["5", "2"],
            "9": ["5", "3"],
            "10": ["4", "5"],
        }
        expected_points = 78
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_missed(self):
        json_data = {
            "1": ["5", "2"],
            "2": ["3", "6"],
            "3": ["8", "-"],
            "4": ["4", "2"],
            "5": ["-", "5"],
            "6": ["7", "1"],
            "7": ["-", "-"],
            "8": ["5", "2"],
            "9": ["5", "-"],
            "10": ["4", "5"],
        }
        expected_points = 64
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_spare(self):
        json_data = {
            "1": ["5", "/"],
            "2": ["3", "6"],
            "3": ["8", "1"],
            "4": ["4", "/"],
            "5": ["1", "/"],
            "6": ["7", "1"],
            "7": ["6", "/"],
            "8": ["5", "2"],
            "9": ["5", "3"],
            "10": ["4", "5"],
        }
        expected_points = 106
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_strike(self):
        json_data = {
            "1": ["5", "2"],
            "2": ["X"],
            "3": ["8", "1"],
            "4": ["4", "2"],
            "5": ["1", "5"],
            "6": ["X"],
            "7": ["6", "3"],
            "8": ["X"],
            "9": ["5", "3"],
            "10": ["4", "5"],
        }
        expected_points = 110
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_strike_consecutive(self):
        json_data = {
            "1": ["5", "2"],
            "2": ["X"],
            "3": ["X"],
            "4": ["4", "2"],
            "5": ["1", "5"],
            "6": ["X"],
            "7": ["X"],
            "8": ["X"],
            "9": ["5", "3"],
            "10": ["4", "5"],
        }
        expected_points = 149
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_spare_and_strike_consecutive(self):
        json_data = {
            "1": ["5", "/"],
            "2": ["X"],
            "3": ["8", "1"],
            "4": ["X"],
            "5": ["5", "/"],
            "6": ["4", "4"],
            "7": ["X"],
            "8": ["5", "/"],
            "9": ["X"],
            "10": ["4", "5"],
        }
        expected_points = 158
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_round_10_spare(self):
        json_data = {
            "1": ["5", "2"],
            "2": ["3", "6"],
            "3": ["8", "1"],
            "4": ["4", "2"],
            "5": ["1", "5"],
            "6": ["7", "1"],
            "7": ["6", "3"],
            "8": ["5", "2"],
            "9": ["5", "3"],
            "10": ["4", "/", "7"],
        }
        expected_points = 86
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_round_10_strike(self):
        json_data = {
            "1": ["5", "2"],
            "2": ["3", "6"],
            "3": ["8", "1"],
            "4": ["4", "2"],
            "5": ["1", "5"],
            "6": ["7", "1"],
            "7": ["6", "3"],
            "8": ["5", "2"],
            "9": ["5", "3"],
            "10": ["X", "7", "2"],
        }
        expected_points = 88
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_all_missed(self):
        json_data = {
            "1": ["-", "-"],
            "2": ["-", "-"],
            "3": ["-", "-"],
            "4": ["-", "-"],
            "5": ["-", "-"],
            "6": ["-", "-"],
            "7": ["-", "-"],
            "8": ["-", "-"],
            "9": ["-", "-"],
            "10": ["-", "-"],
        }
        expected_points = 0
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )

    def test_perfect_game(self):
        json_data = {
            "1": ["X"],
            "2": ["X"],
            "3": ["X"],
            "4": ["X"],
            "5": ["X"],
            "6": ["X"],
            "7": ["X"],
            "8": ["X"],
            "9": ["X"],
            "10": ["X", "X", "X"],
        }
        expected_points = 300
        self.assertEqual(
            Score().calculate(json_data),
            expected_points,
        )
