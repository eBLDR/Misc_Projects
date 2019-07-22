from random import randint


def get_random(num):
    l = []
    for i in range(num):
        l.append(randint(1, 6))
    l.sort(reverse=True)
    return l


def combat_simulation(a, d):
    if a == 1:
        attacker_dices = 1
    elif a == 2:
        attacker_dices = 2
    else:
        attacker_dices = 3
    if d <= 2:
        defender_dices = 1
    else:
        defender_dices = 2
    attacker = get_random(attacker_dices)
    defender = get_random(defender_dices)
    dead_attacker = 0
    dead_defender = 0
    if attacker[0] > defender[0]:
        dead_defender += 1
    else:
        dead_attacker += 1
    if attacker_dices >= 2 and defender_dices >= 2:
        if attacker[1] > defender[1]:
            dead_defender += 1
        else:
            dead_attacker += 1

    return dead_attacker, dead_defender


def battle_simulation(a, d):
    while a > 0 and d > 0:
        dead_a, dead_d = combat_simulation(a, d)
        a -= dead_a
        d -= dead_d
    if a > 0:
        return 'Attack'
    elif d > 0:
        return 'Defense'


if __name__ == '__main__':
    number_attackers = 7
    number_defenders = 6
    result = {
        'Attack': 0,
        'Defense': 0
    }

    for i in range(100000):
        r = battle_simulation(number_attackers, number_defenders)
        result[r] += 1

    print('Attacker won: {} battles.\nDefender won: {} battles.'.format(result['Attack'], result['Defense']))

