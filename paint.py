import turtle
import pickle

"""
Mapping functions so we can repeat previous drawings:

	1 = increase_line_width()
	2 = decrease_line_width()
	3 = color()
	4 = shape()
	5 = stamp()
	(x, y) = goto()
"""
LIST = []  # Action sequence memory


def goto(x, y):
    atlas.pendown()
    atlas.goto(x, y)
    LIST.append([x, y])


def clear_screen():
    global i_WIDTH, i_COLORS, i_SHAPES
    i_WIDTH, i_COLORS, i_SHAPES = (0, 0, 0)
    atlas.reset()
    global SHAPES, LIST
    atlas.shape(SHAPES[i_SHAPES])
    LIST = []


def exit_():
    screen.bye()


def increase_line_width():
    global i_WIDTH, WIDTH
    if i_WIDTH < 11:
        i_WIDTH += 1
    atlas.pensize(WIDTH[i_WIDTH])
    LIST.append(1)


def decrease_line_width():
    global i_WIDTH, WIDTH
    if i_WIDTH > 0:
        i_WIDTH -= 1
    atlas.pensize(WIDTH[i_WIDTH])
    LIST.append(2)


def color():
    global i_COLORS, COLORS
    if i_COLORS < 7:
        i_COLORS += 1
    else:
        i_COLORS = 0
    atlas.color(COLORS[i_COLORS])
    LIST.append(3)


def shape():
    global i_SHAPES, SHAPES
    if i_SHAPES < 5:
        i_SHAPES += 1
    else:
        i_SHAPES = 0
    atlas.shape(SHAPES[i_SHAPES])
    LIST.append(4)


def stamp():
    atlas.stamp()
    LIST.append(5)


def repeat():
    global LIST
    LIST_BLOCKED = LIST[::]
    clear_screen()
    for action in LIST_BLOCKED:
        if isinstance(action, (tuple, list)):
            goto(action[0], action[1])
        else:
            if action == 1:
                increase_line_width()
            elif action == 2:
                decrease_line_width()
            elif action == 3:
                color()
            elif action == 4:
                shape()
            elif action == 5:
                stamp()
    
    LIST = LIST_BLOCKED[::]  # Deep copy of the list


def save():
    global LIST
    with open('myDraw.pkl', 'wb') as extr:
        pickle.dump(LIST, extr)


def load():
    with open('myDraw.pkl', 'rb') as intr:
        LIST_LOAD = pickle.load(intr)
    global LIST
    LIST = LIST_LOAD[::]
    repeat()


# Constants
WIDTH = [str(i) for i in range(1, 13)]
i_WIDTH = 0  # Initial width

COLORS = ['black', 'yellow', 'orange', 'red', 'green', 'darkgreen', 'blue', 'purple']
i_COLORS = 0  # Initial color

SHAPES = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
i_SHAPES = 0  # Initial shape

# Window settings
screen = turtle.Screen()
screen.setup(650, 650)
screen.title('Paint Version by eBLDR')

# Turtle settings
atlas = turtle.Turtle()
atlas.pencolor(COLORS[i_COLORS])
atlas.pensize(WIDTH[i_WIDTH])
atlas.shape(SHAPES[i_SHAPES])

# Legend drawing
legend = turtle.Turtle()
legend.hideturtle()
legend.penup()
legend.goto(-315, -315)
legend.write('Intro => new\nEsc => exit\n2/3 => width\n0 => color\n1 => shape\nSpace => stamp\nr => Repeat\ns => Save\no => Load', align='left')

# Keys
screen.onclick(goto, btn=1)
screen.onkey(clear_screen, 'Return')
screen.onkey(exit_, 'Escape')
screen.onkey(increase_line_width, '2')
screen.onkey(decrease_line_width, '3')
screen.onkey(color, '0')
screen.onkey(shape, '1')
screen.onkey(stamp, 'space')
screen.onkey(repeat, 'r')
screen.onkey(save, 's')
screen.onkey(load, 'o')

screen.listen()

screen.mainloop()

print(LIST)  # Only for control
