class Player:
    # Constant
    init_elo_points = 1000

    def __init__(self, elo_points=None):
        self.elo_points = elo_points or self.init_elo_points

    def update_elo_points(self, delta_elo_points):
        self.elo_points += delta_elo_points


class ELOCalculator:
    # Constant
    K = 32

    decimal_points = 2

    def calculate_expected_score(self, player_a, player_b):
        return round(
            1 / (1 + 10 ** ((player_b.elo_points - player_a.elo_points) / 400)),
            self.decimal_points,
        )

    def calculate_delta_points(self, expected_score, actual_score):
        return round(self.K * (actual_score - expected_score), self.decimal_points)


def simulate(player_a_elo_points=None, player_b_elo_points=None):
    player_a = Player(elo_points=player_a_elo_points)
    player_b = Player(elo_points=player_b_elo_points)
    elo_calculator = ELOCalculator()

    print(f'Matching:\nPlayer A ({player_a.elo_points}) vs Player B ({player_b.elo_points})')
    print('- ' * 10)

    player_a_expected_score = elo_calculator.calculate_expected_score(player_a, player_b)
    player_b_expected_score = elo_calculator.calculate_expected_score(player_b, player_a)

    print('Expected scores:')
    print(f'Player A: {player_a_expected_score}')
    print(f'Player B: {player_b_expected_score}')
    print('- ' * 10)

    print('[Assuming player A wins one match]')
    player_a_actual_score = 1
    player_b_actual_score = 0
    player_a_delta_points = elo_calculator.calculate_delta_points(player_a_expected_score, player_a_actual_score)
    player_b_delta_points = elo_calculator.calculate_delta_points(player_b_expected_score, player_b_actual_score)

    print('Delta points:')
    print(f'Player A: {player_a_delta_points}')
    print(f'Player B: {player_b_delta_points}')
    print('- ' * 10)

    player_a.update_elo_points(player_a_delta_points)
    player_b.update_elo_points(player_b_delta_points)
    print('Final ELO points:')
    print(f'Player A ({player_a.elo_points})')
    print(f'Player B ({player_b.elo_points})')


if __name__ == '__main__':
    simulate(
        player_a_elo_points=1050,
        player_b_elo_points=None,
    )
