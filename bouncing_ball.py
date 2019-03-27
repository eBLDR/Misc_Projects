import random
import turtle


def generate_ball():
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color(random.choice(['limegreen', 'royalblue', 'yellow', 'red', 'orange', 'whitesmoke', 'purple']))
    ball.speed(0)
    ball.penup()
    ball.hideturtle()
    ball.goto(random.randint(width * 0.1, width * 0.9), random.randint(height * 0.3, height * 0.9))
    ball.showturtle()
    ball.dy = 0
    return ball


def generate_ball_container(n):
    return [generate_ball() for _ in range(n)]


window = turtle.Screen()
window.setup(600, 600)
window.bgcolor('black')
window.title('Bouncing Particle Simulator')
window.setworldcoordinates(0, 0, window.window_width(), window.window_height())

# Set up config
width = 600
height = 600
g = 0.15
n_of_balls = 7
window.delay(1)
ball_container = generate_ball_container(n_of_balls)

while True:
    for ball in ball_container:
        ball.dy -= g
        new_y = ball.ycor() + ball.dy
        new_y = 0 if new_y < 0 else new_y
        ball.sety(new_y)

        # Check bounce
        if ball.ycor() == 0:
            ball.dy *= -1

window.mainloop()
