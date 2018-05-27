from cs1lib import *


class Robot:

    def __init__(self, x, y, theta):
        self.x = x;
        self.y = y;
        self.r = 3;
        self.vx = 1;
        self.vy = 1;
        self.w = 2;
        self.theta = theta
        self.image = load_image("circle_with_radius.gif")

    def step(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep
        self.theta += self.w * timestep

    def draw_robot(self):
        # Note: future testing required to test whether the cx and cy are correct
        draw_image(self.image, self.x, self.y, self.x + self.r, self.y + self.r, self.theta)