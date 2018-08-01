# Set of common dice tools for board games

from random import randint


def dice_roll(dices=1, faces=6, sum_=False):
    results = [randint(1, faces) for n in range(dices)]
    results.sort()
    if sum_:
        results.append(sum(results))

    return results


def dice_greater_or_equal_than(dice_set, n):
    count = 0
    for dice in dice_set:
        count += 1 if dice >= n else 0

    return count


def compare_dices(dice_set_1, dice_set_2):
    if len(dice_set_1) == len(dice_set_2):
        return tuple([(n, m) for n, m in zip(dice_set_1, dice_set_2)])


for i in range(10):
    s_1 = dice_roll(dices=2)
    s_2 = dice_roll(dices=2)
    print(s_1, s_2)
    print(compare_dices(s_1, s_2))

print(dice_greater_or_equal_than(dice_roll(dices=10), 5))

