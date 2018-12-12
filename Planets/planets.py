import turtle

# radius is in km, mass in kg

planets = {}

with open('planetsdata.txt', 'r') as data:
    for line in data.read().splitlines():
        name, radius, mass, image = line.split(';')
        planets[name] = {'radius': float(radius),  # adding data to the dictionary
                         'mass': float(mass),
                         'image': image}


def display_all():
    for key in planets.keys():
        display_one(key)


def display_one(key):
    print("{}\t-\tRadius (km): {:7}\tMass (kg): {:10.9}".format(
        key.upper(), planets[key]['radius'], planets[key]['mass']))


def get_planet_from_user():
    for planet in planets.keys():
        print("| {} |".format(planet.capitalize()), end='')
    while True:
        planet = input('\nChoose one planet:\n').lower()
        if planet in planets.keys():
            return planet
        else:
            print('Not valid')


def display_in_screen(drawer, planet):
    font_style = ('Ubuntu Mono', 18, 'bold')
    drawer.goto(0, 90)
    shape_name = 'graphics//{}'.format(planets[planet]['image'])
    screen.register_shape(shape_name)
    drawer.shape(shape_name)
    drawer.stamp()
    drawer.goto(0, -80)
    drawer.write(planet.upper(), font=font_style, align='center')
    drawer.goto(0, -130)
    drawer.write("Radius (km): {:7}".format(planets[planet]['radius']), font=font_style, align='center')
    drawer.goto(0, -170)
    drawer.write("Mass (kg): {:10.9}".format(planets[planet]['mass']), font=font_style, align='center')


user_planet = get_planet_from_user()

# setting screen
screen = turtle.Screen()
width = 500
height = 500
screen.setup(width, height)
screen.title('Planets Data')
screen.setworldcoordinates(-width / 2, -height / 2, width / 2, height / 2)
screen.bgcolor('black')

builder = turtle.Turtle()
builder.hideturtle()
builder.penup()
builder.color('white')

display_in_screen(builder, user_planet)

turtle.done()
