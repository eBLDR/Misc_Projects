import random
import time


class Stats:
    def __init__(self):
        self.attempts = 3
        self.iq = 0


def assess_answer(stats, correct, user):
    if user == correct:
        print('\nAWESOME! GENIUS AT PLAY!')
        stats.iq += 1
        input('\nEnter for CONTINUE...')
        return True
    else:
        print('\nBIG FAIL...')
        stats.attempts -= 1
        input('\nEnter for CONTINUE...')
        return False


def round_01(stats):
    while stats.attempts > 0:
        print('\nRound 01')
        s = [0, 3, 4, 6, 12, 12, 6, 4, 3, 0]
        print('\n', s, '\n\nL ? R\nC = (L+?+R)')
        pos = random.randint(1, 8)
        x = s[pos]
        sol = x + s[pos - 1] + s[pos + 1]
        print('\n? =', x)
        r = int(input('C = '))
        if assess_answer(stats, r, sol):
            break
        else:
            print('\nAttempts left: ', stats.attempts)
            input('\nEnter for CONTINUE...')


def round_02(stats):
    while stats.attempts > 0:
        print('\nRound 02')
        print('\nB = 6\nI = 27\nK = 33')
        s = ['C', 'D', 'E', 'F', 'G', 'H']
        pos = random.randint(0, 5)
        incognito = s[pos]
        sol = (pos + 3) * 3
        print('\nValor de', incognito, ' ?')
        r = input()
        if assess_answer(stats, r, sol):
            break
        else:
            print('\nAttempts left: ', stats.attempts)
            input('\nEnter for CONTINUE...')


def round_03(stats):
    while stats.attempts > 0:
        print('\nRound 03')
        print('\n1 = v\n2 = w\n3 = x\n4 = y')
        r = input('v = ')
        sol = 1
        if assess_answer(stats, r, sol):
            break
        else:
            print('\nAttempts left: ', stats.attempts)
            input('\nEnter for CONTINUE...')


def round_04(stats):
    while stats.attempts > 0:
        print('\nLast Round')
        print('\nSREVIN_')
        sol = 1
        r = input('_ = ')
        if assess_answer(stats, r, sol):
            break
        else:
            print('\nAttempts left: ', stats.attempts)
            input('\nEnter for CONTINUE...')


def end(stats):
    if stats.attempts == 0:
        print('\nNo more attempts, calculating IQ...')
    elif stats.attempts != 0:
        print('\nEnd ot test, calculating IQ...')
    
    time.sleep(2)
    
    print('\nAproximate Comparative IQ table:')
    print('\n1   -> Stone\n5   -> Slug\n32  -> Bonsai\n69  -> Popcorn')
    print('105 -> PC\n150 -> NOT YOU\n210 -> Nemo')
    input('\nENTER to show IQ...')
    
    print('\nYour exactly IQ is: ', stats.iq)
    
    print('\nSEE YOU!')
    input('\n\tENTER TO EXIT!')


game_stats = Stats()

print('\nEnjoy the Code\nInitial game.attempts: ', game_stats.attempts)
input('\nEnter for START...')

round_01(game_stats)
round_02(game_stats)
round_03(game_stats)
round_04(game_stats)
end(game_stats)
