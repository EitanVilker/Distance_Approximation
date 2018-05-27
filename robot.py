from cs1lib import *


class Robot:

    def __init__(self, x, y, theta):
        self.x = x;
        self.y = y;
        self.vx = 1;
        self.vy = 1;
        self.w = 2;
        self.theta = theta
        self.image = load_image("circle_with_radius.gif")
        self.image_height = 132
        self.image_width = 140

    def step(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep
        self.theta += self.w * timestep

    def draw_robot(self):
        # Note: future testing required to test whether the cx and cy are correct
        draw_image(self.image, self.x, self.y, self.x + self.image_width, self.y + self.image_height, self.theta)