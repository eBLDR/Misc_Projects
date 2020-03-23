#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Solar system
import math
import random
import sys

import dictionary as dic
import parameters as par
import pygame as pyg
from pygame.locals import *

pyg.init()


class Body:
    def __init__(self, details):
        self.name = details.get('name', '')
        self.color = details.get('color', '')
        self.mass = details.get('mass', 0)
        self.shape = details.get('shape', 0)
        self.radius = details.get('radius', 0)
        self.pos = details.get('init_pos', 0)
        self.vel = details.get('init_vel', 0)


class Master:
    def __init__(self):
        self.bodies_list = []

        self.rgb_colors = {'black': (0, 0, 0),
                           'white': (255, 255, 255),
                           'gray': (128, 128, 128),
                           'blue': (0, 96, 255),
                           'red': (255, 0, 0),
                           'yellow': (255, 255, 0),
                           'green': (0, 128, 0),
                           'orange': (128, 255, 0),
                           'maroon': (128, 0, 0)}

    def gen_known_body(self, details):
        self.bodies_list.append(Body(details))

    def gen_random_planet(self, num):
        for i in range(1, num + 1):
            random_details = {'name': 'Planet %i' % i,
                              'color': 'gray',
                              'mass': random.randint(1, 30) * (10 ** 24),
                              'radius': 1,
                              'init_pos': [random.randint(0, par.W) * par.distance_factor, random.randint(0, par.H) * par.distance_factor],
                              'init_vel': [random.randint(-100000, 100000), random.randint(-100000, 100000)]}

            random_details['shape'] = int(round(random_details['mass'] / (2 * (10 ** 24))))
            if random_details['shape'] < 4:
                random_details['shape'] = 4
            self.bodies_list.append(Body(random_details))

    @staticmethod
    def get_number_of_random_planets():
        while True:
            num_of_random_planets = input('Number of Random Planets = ')
            if num_of_random_planets.isdigit():
                return int(num_of_random_planets)

    @staticmethod
    def dist_bet(r1, r2):
        d_x = r2[0] - r1[0]
        d_y = r2[1] - r1[1]
        mod = float(math.sqrt((d_x ** 2) + (d_y ** 2)))
        dist = [d_x, d_y, mod]
        return dist

    def move(self):
        for b1 in self.bodies_list:
            f_x = 0
            f_y = 0
            for b2 in self.bodies_list:
                if b1 != b2:
                    dist = self.dist_bet(b1.pos, b2.pos)  # [0] d_x, [1] d_y, [2] mod
                    f_x += (par.G * b1.mass * b2.mass / (dist[2] ** 3)) * dist[0]
                    f_y += (par.G * b1.mass * b2.mass / (dist[2] ** 3)) * dist[1]
            a_x = f_x / b1.mass
            a_y = f_y / b1.mass

            b1.pos[0] = b1.pos[0] + b1.vel[0] * par.time_delta + 0.5 * a_x * (par.time_delta ** 2)
            b1.pos[1] = b1.pos[1] + b1.vel[1] * par.time_delta + 0.5 * a_y * (par.time_delta ** 2)

            b1.vel[0] = b1.vel[0] + a_x * par.time_delta
            b1.vel[1] = b1.vel[1] + a_y * par.time_delta

    def orbit(self):
        fps_clock = pyg.time.Clock()

        display_screen = pyg.display.set_mode((par.W, par.H), 0, 32)
        pyg.display.set_caption('Simple Orbit')

        while True:
            display_screen.fill(self.rgb_colors['black'])
            for body in self.bodies_list:
                pyg.draw.circle(display_screen, self.rgb_colors[body.color], (int(round(body.pos[0] / par.distance_factor)),
                                                                              int(round(body.pos[1] / par.distance_factor))),
                                (int(round(body.shape / 2))), 0)

            for event in pyg.event.get():
                if event.type == QUIT:
                    pyg.quit()
                    sys.exit()

            self.move()
            pyg.display.update()
            fps_clock.tick(par.FPS)

    def run(self):
        # Generate known bodies
        try:
            self.gen_known_body(dic.SUN)
            self.gen_known_body(dic.EARTH)
            self.gen_known_body(dic.MARS)
            self.gen_known_body(dic.MOON)
            self.gen_known_body(dic.VENUS)
            self.gen_known_body(dic.JUPITER)
            self.gen_known_body(dic.MERCURY)
        except AttributeError:
            raise AttributeError('Invalid entrance')

        # Generate random bodies
        self.gen_random_planet(self.get_number_of_random_planets())

        self.orbit()


if __name__ == '__main__':
    master = Master()
    master.run()
