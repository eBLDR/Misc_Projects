""" - Monty Hall Problem -
Suppose you're on a game show, and you're given the choice of three doors:
Behind one door is a car; behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door,
say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?"
Is it to your advantage to switch your choice?
- Wikipedia """

import random


def get_option(options, prompt):
    while True:
        option = input(prompt).upper()
        if option in options:
            return option
        else:
            print("Invalid option.")


DOORS = ["A", "B", "C"]
ACTIONS = ["H", "S"]  # hold or switch
ROUNDS = 1000  # edit number of rounds to simulate

door_chosen_initially = get_option(DOORS, "Choose a door (A, B, C): ")  # player chooses one door
action = get_option(ACTIONS, "Always switch or hold (S, H)? ")  # player chooses action

wins = 0

input("\nLet's play {} times . . . <return>".format(ROUNDS))

for i in range(1, ROUNDS + 1):
    print("GAME: {:4} --- ".format(i), end='')
    door_chosen = door_chosen_initially
    door_prize = random.choice(DOORS)  # placing the prize
    doors_used = [door_chosen, door_prize]  # used doors at the moment
    doors_avail = [door for door in DOORS if door not in doors_used]  # available doors (not used)
    door_opened = random.choice(doors_avail)  # host opens one door (it's always a empty one and not chosen by player)
    
    if action == 'S':  # if player switches door
        doors_avail = [door for door in DOORS if door not in [door_chosen, door_opened]]
        door_chosen = doors_avail[0]  # will be the only one available
    
    playerWin = (door_chosen == door_prize)  # check if player wins
    
    # displaying stuff
    print("Prize placed in: {} - You chose: {} - Host opened: {}".format(
        door_prize, door_chosen_initially, door_opened), end='')
    
    if action == 'H':
        print(" - You held to: {}".format(door_chosen), end='')
    else:
        print(" - You switched to: {}".format(door_chosen), end='')
    
    if playerWin:
        wins += 1
        print(" - You win (total wins: {})".format(wins), end='')
    
    print()  # new line

print("\nYou won {} game/s out of {}, that's {:.3}%.".format(wins, ROUNDS, (wins * 100 / ROUNDS)))
