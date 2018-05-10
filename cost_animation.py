from cs1lib import *
from time_cost import *
from robot import *


TIMESTEP = 1

robot = Robot(200, 200, 5, 10, 10, 5, 45)


def main():
    robot.draw_robot()
    robot.step(TIMESTEP)

start_graphics(main)


