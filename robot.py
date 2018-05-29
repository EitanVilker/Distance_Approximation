from cs1lib import *
from math import cos, sin


class Robot:

    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.v = 2
        self.w = 1
        self.theta = theta
        self.image_height = 132
        self.image_width = 140
        self.radius = 30

    def draw_robot(self):
        # Note: future testing required to test whether the cx and cy are correct
        draw_circle(self.x, self.y, self.radius)
        draw_line(self.x, self.y, self.x + self.radius * cos(2 * pi - self.theta * pi / 180), self.y + self.radius * sin(2 * pi - self.theta * pi / 180))
