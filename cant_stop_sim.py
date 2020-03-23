# Can't Stop board game simulation
import random


class Simulator:
    def __init__(self, rounds=100000, display_logs=False):
        self.rounds = rounds
        self.display_logs = display_logs

        self.columns_to_conquer_for_win = 3

        self.columns_per_number = {2: 3,
                                   3: 5,
                                   4: 7,
                                   5: 9,
                                   6: 11,
                                   7: 13,
                                   8: 11,
                                   9: 9,
                                   10: 7,
                                   11: 5,
                                   12: 3}

        self.column_counter = None
        self.columns_conquered = None

        self.result_set = []

        self.statistics = {}

    def init_game_stats(self):
        self.column_counter = {n: 0 for n in self.columns_per_number.keys()}
        self.columns_conquered = []

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def get_dice_set(self, n=4):
        return [self.roll_dice() for _ in range(n)]

    @staticmethod
    def get_combinations(dice_set):
        return {1: (dice_set[0] + dice_set[1], dice_set[2] + dice_set[3]),
                2: (dice_set[0] + dice_set[2], dice_set[1] + dice_set[3]),
                3: (dice_set[0] + dice_set[3], dice_set[1] + dice_set[2])}

    def token_progress(self, columns):
        for number in columns:
            self.column_counter[number] += 1

        for column in self.column_counter.keys():
            if self.column_counter[column] >= self.columns_per_number[column] and column not in self.columns_conquered:
                self.column_counter[column] = self.columns_per_number[column]
                self.columns_conquered.append(column)

                if self.display_logs:
                    print('Conquered column', column)

    def game(self):
        self.init_game_stats()
        while len(self.columns_conquered) < self.columns_to_conquer_for_win:
            dice_set = self.get_dice_set()
            combinations = self.get_combinations(dice_set)
            progress_in = combinations[random.randint(1, len(combinations.keys()))]
            self.token_progress(progress_in)

            if self.display_logs:
                print('Progressing in', progress_in)

        self.result_set.append(self.columns_conquered)

    def simulate(self):
        for i in range(self.rounds):
            self.game()

    def get_statistics(self):
        for result in self.result_set:
            for column in result:
                self.statistics.setdefault(column, 0)
                self.statistics[column] += 1

    def display_statistics(self):
        for column in sorted(self.statistics.keys()):
            print('Column {} was in winning combination {} times.'.format(column, self.statistics[column]))

    def run(self):
        self.simulate()
        self.get_statistics()
        self.display_statistics()

    def report_dice_combinations(self):
        report = {}
        for i in range(self.rounds):
            dice_set = self.get_dice_set()
            combinations = self.get_combinations(dice_set)
            uniques = []
            for combination in combinations.values():
                for number in combination:
                    if number not in uniques:
                        uniques.append(number)

            for result in uniques:
                report.setdefault(result, 0)
                report[result] += 1

        for number in sorted(report.keys()):
            percentage = report[number] / self.rounds * 100
            print('Number {} has appeared in {:.5}% of throws.'.format(number, percentage))


if __name__ == '__main__':
    simulator = Simulator()
    simulator.report_dice_combinations()
    print('#' * 10)
    simulator.run()
