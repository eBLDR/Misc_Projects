def get_dice_values(dices):
    # Possible dice combinations
    dice_values = []

    if dices == 1:
        for i in range(dice_faces):
            dice_values.append(i + 1)
    elif dices == 2:
        for i in range(dice_faces):
            for j in range(dice_faces):
                dice_values.append([i + 1, j + 1])
                dice_values[-1].sort(reverse=True)  # -1 takes last value
    elif dices == 3:
        for i in range(dice_faces):
            for j in range(dice_faces):
                for k in range(dice_faces):
                    dice_values.append([i + 1, j + 1, k + 1])
                    dice_values[-1].sort(reverse=True)

    return dice_values


def get_atk_num_of_dices(atk_army):
    if atk_army >= 3:
        return 3
    elif atk_army == 2:
        return 2
    elif atk_army == 1:
        return 1
    else:
        return 0


def get_def_num_of_dices(def_army):
    if def_army >= 3:
        return 2
    elif def_army == 2 or def_army == 1:
        return 1
    else:
        return 0


def get_chance(atk_army, def_army):
    atk_kill_two = 0
    atk_kill_one = 0
    eye_for_eye = 0  # Attacker kills one but also loses one
    atk_lose_one = 0
    atk_lose_two = 0

    atk_dices = get_atk_num_of_dices(atk_army)
    def_dices = get_def_num_of_dices(def_army)
    total_combinations = 6 ** (atk_dices + def_dices)

    atk_dice_values = get_dice_values(atk_dices)
    def_dice_values = get_dice_values(def_dices)

    # Value declaration
    for d in range(len(def_dice_values)):
        if def_dices != 1:
            defender_1 = def_dice_values[d][0]
            defender_2 = def_dice_values[d][1]
        else:
            defender_1 = def_dice_values[d]
        for a in range(len(atk_dice_values)):
            if atk_dices != 1:
                attacker_1 = atk_dice_values[a][0]
                attacker_2 = atk_dice_values[a][1]
            else:
                attacker_1 = atk_dice_values[a]

            # Comparative
            atk_killed = 0
            atk_died = 0
            if attacker_1 > defender_1:
                atk_killed += 1
            else:
                atk_died += 1
            if atk_dices != 1 and def_dices != 1:
                if attacker_2 > defender_2:
                    atk_killed += 1
                else:
                    atk_died += 1

                # Partial calculations
                if atk_killed == 2:
                    atk_kill_two += 1
                elif atk_killed == 1 and atk_died == 1:
                    eye_for_eye += 1
                else:
                    atk_lose_two += 1
            else:
                if atk_killed == 1:
                    atk_kill_one += 1
                else:
                    atk_lose_one += 1

    # Probabilities in %
    atk_kill_two_percentage = (atk_kill_two * 100) / total_combinations
    atk_kill_one_percentage = (atk_kill_one * 100) / total_combinations
    eye_for_eye_percentage = (eye_for_eye * 100) / total_combinations
    atk_lose_one_percentage = (atk_lose_one * 100) / total_combinations
    atk_lose_two_percentage = (atk_lose_two * 100) / total_combinations

    return [float('{0:.2f}'.format(atk_kill_two_percentage)), float('{0:.2f}'.format(atk_kill_one_percentage)),
            float('{0:.2f}'.format(eye_for_eye_percentage)), float('{0:.2f}'.format(atk_lose_one_percentage)),
            float('{0:.2f}'.format(atk_lose_two_percentage))]


def display(max_atk_army, max_def_army):
    print('Probability of Atk Kills 2, Atk Kills 1, Atk Kills 1 & Loses 1, \
Atk Loses 1, Atk Loses 2\n')
    for i in range(max_def_army):
        for j in range(max_atk_army):
            atk_army = j + 1
            def_army = i + 1
            result = result_chance['A{0}|D{1}'.format(atk_army, def_army)]
            print('Atk {0} | Def {1} -> {2:2.2f}% | {3:2.2f}% | {4:2.2f}% | {5:2.2f}% | {6:2.2f}%'.format(
                atk_army, def_army, result[0], result[1], result[2], result[3], result[4]))


if __name__ == '__main__':
    # Setting max units / army
    MAX_ATK_ARMY = 3  # Attacker
    MAX_DEF_ARMY = 3  # Defender

    dice_faces = 6  # Dice number of faces

    result_chance = {}

    for i in range(MAX_DEF_ARMY):
        for j in range(MAX_ATK_ARMY):
            ATK_ARMY = j + 1
            DEF_ARMY = i + 1
            result_chance['A{0}|D{1}'.format(ATK_ARMY, DEF_ARMY)] = get_chance(ATK_ARMY, DEF_ARMY)

    display(MAX_ATK_ARMY, MAX_DEF_ARMY)

