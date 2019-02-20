import time
import turtle


def main(image_path, intro_text, text, total_time):
    def bye_(x, y):
        screen.bye()

    # Screen
    screen = turtle.Screen()
    screen.setup(1800, 1200, 0, 0)
    screen.title('Kaizen')

    cursor = turtle.Turtle()
    cursor.hideturtle()
    cursor.speed(0)
    cursor.penup()

    # Image shape
    screen.register_shape(image_path)
    cursor.shape(image_path)
    # cursor.shapesize(0.5, 0.5)

    # Print image
    cursor.goto(-380, 0)
    cursor.stamp()

    # Texts
    intro_text_font_style = ('Ubuntu Mono', 52, 'bold')
    text_font_style = ('Ubuntu Mono', 36, 'bold')

    text_x_align = 500

    cursor.goto(text_x_align, 200)
    cursor.write(intro_text, font=intro_text_font_style, align='center')

    cursor.goto(text_x_align, 0)
    cursor.write(text, font=text_font_style, align='center')

    cursor.goto(text_x_align, -150)
    cursor.write('GO!', font=intro_text_font_style, align='center')

    # Kaizen is ongoing...
    time.sleep(total_time)

    cursor.goto(text_x_align, -300)
    cursor.write('Good job! Click to continue.', font=text_font_style, align='center')

    # Done - listen for click to exit
    screen.onclick(bye_, btn=1)
    screen.listen()
    screen.mainloop()
