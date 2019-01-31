# DICTIONARY OF KNOWN COSMIC BODIES
import math

import parameters as par

SUN = {'name': "Sun",
       'color': 'yellow',
       'shape': 16,
       'mass': 1.989 * (10 ** 30),
       'radius': 6.955 * (10 ** 8),
       'init_pos': [(par.W / 2) * par.distance_factor, (par.H / 2) * par.distance_factor],  # center
       'init_vel': [0, 0]}

MERCURY = {'name': "Mercury",
           'color': 'maroon',
           'shape': 6,
           'mass': 3.301 * (10 ** 23),
           'radius': 2.244 * (10 ** 6),
           'init_pos': [(par.W / 2) * par.distance_factor, (par.H / 2 * par.distance_factor) + (5.791 * (10 ** 10))],  # distance mercury-sun = 5.791x10^10 m
           'init_vel': [math.sqrt(par.G * SUN['mass'] / (5.791 * (10 ** 10))), 0]}  # v_orb = sqrt(Gm/r) ->

VENUS = {'name': "Venus",
         'color': 'green',
         'shape': 8,
         'mass': 4.867 * (10 ** 24),
         'radius': 6.417 * (10 ** 6),
         'init_pos': [(par.W / 2) * par.distance_factor, (par.H / 2 * par.distance_factor) + (1.082 * (10 ** 11))],  # distance venus-sun = 1.082x10^11 m
         'init_vel': [math.sqrt(par.G * SUN['mass'] / (1.082 * (10 ** 11))), 0]}  # v_orb = sqrt(Gm/r) ->

EARTH = {'name': "Earth",
         'color': 'blue',
         'shape': 8,
         'mass': 5.972 * (10 ** 24),
         'radius': 6.371 * (10 ** 6),
         'init_pos': [(par.W / 2) * par.distance_factor, (par.H / 2 * par.distance_factor) + (1.496 * (10 ** 11))],  # distance earth-sun = 1.496x10^11 m
         'init_vel': [math.sqrt(par.G * SUN['mass'] / (1.496 * (10 ** 11))), 0]}  # v_orb = sqrt(Gm/r) -> 29822 m/s

MARS = {'name': "Mars",
        'color': 'red',
        'shape': 8,
        'mass': 6.417 * (10 ** 23),
        'radius': 3.39 * (10 ** 6),
        'init_pos': [(par.W / 2) * par.distance_factor, (par.H / 2 * par.distance_factor) + (2.279 * (10 ** 11))],  # distance mars-sun = 2.279x10^11 m
        'init_vel': [math.sqrt(par.G * SUN['mass'] / (2.279 * (10 ** 11))), 0]}  # v_orb = sqrt(Gm/r) -> 24000 m/s (aprox)

JUPITER = {'name': "Jupiter",
           'color': 'orange',
           'shape': 12,
           'mass': 1.898 * (10 ** 27),
           'radius': 6.991 * (10 ** 7),
           'init_pos': [(par.W / 2) * par.distance_factor, (par.H / 2 * par.distance_factor) + (7.785 * (10 ** 11))],  # distance jupiter-sun = 7.785x10^11 m
           'init_vel': [math.sqrt(par.G * SUN['mass'] / (7.785 * (10 ** 11))), 0]}  # v_orb = sqrt(Gm/r) ->

MOON = {'name': "Moon",
        'color': 'white',
        'shape': 4,
        'mass': 7.348 * (10 ** 22),
        'radius': 1.738 * (10 ** 6),
        'init_pos': [100 * par.distance_factor, 50 * par.distance_factor],  # distance moon-earth = 3'84x10^8 m
        'init_vel': [5500, 12500]}
