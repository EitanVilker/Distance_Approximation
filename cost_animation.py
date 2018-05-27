from cs1lib import *
from time_cost import *
from robot import *
from math import cos, sin

TIMESTEP = 1

robot = Robot(200, 200, 5, 10, 10, 5, 45)
step = 0;


def calculate_arctan(xs, ys, xg, yg):
    arctan = (atan2(ys-yg, xs-xg))*360/(2*pi)
    return arctan


def calculate_initial_rotation(theta_s, theta_f):
    if (theta_s - theta_f) <= 90:
        print("1) clockwise 2) forward")
        return -(theta_s - theta_f)

    if 180 > (theta_s - theta_f) > 90:
        print("1) counterclockwise 2) backwards")
        return theta_s - theta_f

    if 270 > (theta_s - theta_f) > 180:
        print("1) clockwise 2) backwards")
        return -(theta_s - theta_f)

    if 360 > (theta_s - theta_f) >= 270:
        print("1) counterclockwise 2) forward")
        return theta_s - theta_f

    # Boundary cases
    if (theta_s - theta_f) == (0 or 360):
        print("1) none 2) forward")
        return 0

    if (theta_s - theta_f) == 180:
        print("1) none 2) backwards")
        return 0


def calculate_second_rotation(theta_g, theta_f):
    if 180 >= (theta_g - theta_f) > 0:
        print("3) clockwise. Final: forwards")
        return theta_f - theta_g
    if 360 > (theta_g - theta_f) > 180:
        return theta_g - theta_f
        print("3) counterclockwise. Final: forwards")
    if (theta_g - theta_f) == (0 or 360):
        print("3) none. Final: fowards")
        return 0


def main(theta_s, theta_g, xs, ys, xg, yg):
    global step
    # theta_s = 30
    # theta_g = 45
    # xs = 10
    # ys = 30
    # xg = 25
    # yg = 20
    theta_f = calculate_arctan(xs, ys, xg, yg)

    robot.draw_robot()
    robot.step(TIMESTEP)
    if step == 0:
        angle = calculate_initial_rotation(theta_s, theta_f)
        if angle > 0:
            robot.theta += TIMESTEP * robot.w
            if robot.theta >= angle:
                step = 1
        elif angle < 0:
            robot.theta -= TIMESTEP * robot.w
            if robot.theta <= angle:
                step = 1
        else:
            step = 1

    if step == 1:
        # Move straight
        robot.x += robot.vx * cos(theta_f) * TIMESTEP
        robot.y += robot.vy * sin(theta_f) * TIMESTEP
        if xg - 0.1 < robot.x < xg + 0.1 and yg - 0.1 < robot.y < yg + 0.1:
            step = 2

    if step == 2:
        angle = calculate_second_rotation(theta_g, theta_f)
        if angle > 0:
            robot.theta += TIMESTEP * robot.w
            if robot.theta >= angle:
                step = 3
        elif angle < 0:
            robot.theta -= TIMESTEP * robot.w
            if robot.theta <= angle:
                step = 3
        else:
            step = 3


start_graphics(main)


