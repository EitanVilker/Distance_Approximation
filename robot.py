from cs1lib import *


class Robot:

    image = load_image(filename)

    def __init__(self, x, y, r, vx, vy, w, theta):
        self.x = x;
        self.y = y;
        self.r = r;
        self.vx = vx;
        self.vy = vy;
        self.w = w;
        self.theta = theta

    def step(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep
        self.theta += self.w * timestep

    def draw_robot(self):
        set_fill_color(0, 0, 1)
        draw_image(image, self.x, self.y, self.r, cx, cy, self.theta)