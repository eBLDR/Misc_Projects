import random
import string
# import sys
from os import system
from time import sleep


def progress_bar(blocks=50):
    """
    Dynamic progress bar.
    """
    # blocks_delta = int(100 / blocks + 1)
    percentage_delta = int(100 / blocks)
    for i in range(1, blocks + 1):
        # Using carriage return "\r" to replace last printed line
        output = '\r[{blocks}{arrow}{blank}] {percentage}%'.format(
            blocks='=' * i,
            arrow='>' if i < blocks else '',
            blank=' ' * (blocks - i),
            percentage=percentage_delta * i
        )

        print(output, end='')

        # Using sys.stdout
        # sys.stdout.write('\r')
        # sys.stdout.write('[{:20}] {}%'.format('=' * i, 5 * i))
        # sys.stdout.flush()

        sleep(0.25)


def stars(times=10):
    """
    Display random stars on std output.
    :param times: <int> iterations
    """
    chance = 0.04  # The higher the denser
    sleep_time = 0.5
    size = range(80)

    for t in range(times):
        system('clear')
        matrix = [
            ['*' if random.random() < chance else ' ' for _ in size]
            for __ in size
        ]

        for row in matrix:
            for char in row:
                print(char, end=' ')
            print()

        sleep(sleep_time)

    system('clear')


def random_chars(times=300):
    """
    Output random text with increasing speed.
    :param times: <int> iterations
    """
    char_set = list(
        string.punctuation + string.digits + string.ascii_letters
        + string.punctuation + (' ' * 10)
    )
    chars = len(char_set)

    for i in range(1, times):
        random.shuffle(char_set)
        tmp = ''.join(char_set[:chars - random.randint(1, chars - 10)]) * 3
        print(tmp)

        if i < 200:
            sleep(1 / i)
        else:
            sleep(1 / 200)

    system('clear')


def fill_with_char(char='#', times=2500):
    """
    Output character "pyramidally" filling the screen with increasing speed.
    :param char: <str> character to be used
    :param times: <int> iterations
    """
    for i in range(1, times):
        print(char * i)
        sleep(1 / i)


if __name__ == '__main__':
    progress_bar()
