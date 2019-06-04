import turtle
from datetime import datetime

SCREEN_SIZE = 600
CLOCK_SIZE = SCREEN_SIZE * (2 / 3)


def draw_clock(cursor):
    # Draw full clock sphere w/ marks
    radius = CLOCK_SIZE / 2

    cursor.penup()
    cursor.goto(0, - radius)
    cursor.setheading(0)
    cursor.pendown()
    cursor.circle(radius)

    for angle in range(0, 360, 6):
        if angle % 30 == 0:
            draw_time_mark(cursor, radius, angle, hour=True)
        else:
            draw_time_mark(cursor, radius, angle)


def draw_time_mark(cursor, distance, angle, hour=False):
    cursor.penup()
    cursor.goto(0, 0)
    cursor.setheading(angle)
    cursor.forward(distance)
    cursor.pendown()
    cursor.backward(25 if hour else 10)


def draw_hand(cursor, length, angle):
    cursor.clear()
    cursor.penup()
    cursor.goto(0, 0)
    cursor.setheading(90)
    cursor.right(angle)
    cursor.pendown()
    cursor.forward(length)


def draw_hand_seconds(cursor, seconds):
    angle_second = seconds * 6
    draw_hand(cursor, 150, angle_second)


def draw_hand_minutes(cursor, minutes):
    angle_minute = minutes * 6
    draw_hand(cursor, 120, angle_minute)


def draw_hand_hours(cursor, hours, minutes):
    angle_hour = hours * 30 + minutes / 2
    draw_hand(cursor, 90, angle_hour)


def cursor_generator(thickness=1):
    # Setting turtles' objects
    cursor = turtle.Turtle()
    cursor.speed(0)
    cursor.hideturtle()
    cursor.color('white')
    cursor.pensize(thickness)

    return cursor


def main():
    # Setting the window
    window = turtle.Screen()
    window.setup(SCREEN_SIZE, SCREEN_SIZE)
    window.bgcolor('black')
    window.title('Analogue Clock by eBLDR')

    atlas = cursor_generator()

    cronus_hour = cursor_generator(thickness=5)
    cronus_minute = cursor_generator(thickness=3)
    cronus_second = cursor_generator()

    # Init
    draw_clock(atlas)

    past = datetime.now()

    draw_hand_seconds(cronus_second, past.second)
    draw_hand_minutes(cronus_minute, past.minute)
    draw_hand_hours(cronus_hour, past.hour, past.minute)

    # Looping to draw clock's hands
    while True:
        now = datetime.now()

        if now.second != past.second:
            draw_hand_seconds(cronus_second, now.second)

            if now.minute != past.minute:
                draw_hand_minutes(cronus_minute, now.minute)
                draw_hand_hours(cronus_hour, now.hour, now.minute)

            past = now


main()
