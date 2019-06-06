import turtle
import random

DISTANCE = 10


def move_up(cursor):
    cursor.setheading(90)
    cursor.forward(DISTANCE)


def move_down(cursor):
    cursor.setheading(270)
    cursor.forward(DISTANCE)


def move_left(cursor):
    cursor.setheading(180)
    cursor.forward(DISTANCE)


def move_right(cursor):
    cursor.setheading(0)
    cursor.forward(DISTANCE)


def random_draw(cursor):
    opt = [move_up, move_down, move_left, move_right]

    n = 0
    while n < 10000:
        random.choice(opt)(cursor)
        n += 1


def get_input():
    action = input('Move:\n>>> ')

    return action


def main():
    screen = turtle.Screen()
    screen.setup(1200, 1200)

    cursor = turtle.Turtle()
    cursor.speed(0)

    # Main loop
    while True:
        action = get_input()

        if action == 'w':
            move_up(cursor)
        elif action == 's':
            move_down(cursor)
        elif action == 'a':
            move_left(cursor)
        elif action == 'd':
            move_right(cursor)

        elif action == 'r':
            random_draw(cursor)

        elif action == 'q':
            break

    turtle.done()


main()
