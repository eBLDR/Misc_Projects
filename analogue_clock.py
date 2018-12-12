import turtle
import time
from datetime import datetime


def draw_minute_mark(turt, distance, angle):
    # Minute marks
    turt.penup()
    turt.home()
    turt.setheading(angle)
    turt.forward(distance)
    turt.pendown()
    turt.forward(10)


def draw_hour_mark(turt, distance, angle):
    # Hour marks
    draw_minute_mark(turt, distance, angle)
    turt.penup()
    turt.forward(15)
    turt.stamp()


def draw_clock(turt, distance):
    # Draw full clock sphere w/ marks
    angle = 0
    while angle < 360:
        draw_minute_mark(turt, distance, angle)
        angle += 360 / 60
    angle_h = 0
    while angle_h < 360:
        draw_hour_mark(turt, distance, angle_h)
        angle_h += 360 / 12


def draw_hands(turt, thickness, length, angle):
    # Draw clock's hand
    turt.penup()
    turt.home()
    turt.left(angle)
    turt.pendown()
    turt.pensize(thickness)
    turt.forward(length)
    turt.penup()


# Setting the window
window = turtle.Screen()
window.setup(600, 600)
window.bgcolor('black')
window.title('Analogue Clock by eBLDR')

# Setting turtles' objects
atlas = turtle.Turtle()
atlas.speed('fastest')
atlas.shape('triangle')
atlas.hideturtle()
atlas.color('green')

cronos = turtle.Turtle()
cronos.speed('fastest')
cronos.hideturtle()
cronos.color('white')

# Drawing clock
draw_clock(atlas, 200)

# Looping to draw clock's hands
while True:
    time_now = datetime.now()  # Getting time
    
    # Finding angles for hands
    angle_hour = (time_now.hour * (-30) + 90) + time_now.minute / (-2)
    angle_minute = time_now.minute * (-6) + 90
    angle_second = time_now.second * (-6) + 90
    
    # Drawing
    draw_hands(cronos, '10', 120, angle_hour)
    draw_hands(cronos, '4', 180, angle_minute)
    draw_hands(cronos, '1', 180, angle_second)
    
    time.sleep(0.8)  # May differ for optimal performance depending on hardware
    cronos.clear()
    
    window.listen()  # It will raise a terminator error on exit
