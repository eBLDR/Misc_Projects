
# NATO Phonetic Alphabet

import random

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nato = ['ALPHA', 'BRAVO', 'CHARLIE', 'DELTA', 'ECHO', 'FOXTROT',
        'GOLF', 'HOTEL', 'INDIA', 'JULIETT', 'KILO', 'LIMA',
        'MIKE', 'NOVEMBER', 'OSCAR', 'PAPA', 'QUEBEC', 'ROMEO',
        'SIERRA', 'TANGO', 'UNIFORM', 'VICTOR', 'WHISKEY', 'X-RAY',
        'YANKEE', 'ZULU']

TOTAL_VALUES = len(abc)

# building the dictionary
NATO = {}
if len(abc) == len(nato):
    for letter, word in zip(abc, nato):
        NATO[letter] = word


def play(dic, keyList):
    Quit = False
    points = 0
    for key in keyList:
        if Quit:
            break
        while True:
            answer = input('{} is '.format(key)).upper()
            if answer == 'SKIP':
                print(dic[key])
                break
            elif answer == 'QUIT':
                Quit = True
                break
            elif answer == dic[key]:
                break
    else:
        end_game(points)
        

def end_game(points):
    print('COMPLETED\n{0:2} of {1:2}'.format(points, TOTAL_VALUES))


def sorted_version(dic):
    """
    To return sorted key list
    """
    return sorted(dic.keys())


def random_version(dic):
    """
    To return a random key list
    """
    key_list = list(dic.keys())  # to create a new copy
    random.shuffle(key_list)
    return key_list


def main(dic):
    while True:
        print('SKIP to skip an entry\nQUIT to quit game\n-- Select mode --')
        mode = input('SORTED or RANDOM: ').upper()
        if mode == 'SORTED':
            index_list = sorted_version(dic)
            play(NATO, index_list)
        elif mode == 'RANDOM':
            key_list = random_version(dic)
            play(NATO, key_list)
        elif mode == 'QUIT':
            break


if __name__ == '__main__':
    main(NATO)
