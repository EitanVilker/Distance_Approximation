from time_cost import *
from robot import *
from math import cos, sin, atan2
from cs1lib import *

TIMESTEP = 1
counter = 0
step = 0


def calculate_arctan(xs, ys, xg, yg):
    arctan = (atan2(ys-yg, xs-xg))*360/(2*pi)
    if arctan < 0:
        arctan = - arctan
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
    else:
        return 0


def calculate_second_rotation(theta_g, theta_f):
    if 180 >= (theta_g - theta_f) > 0:
        print("3) clockwise. Final: forwards")
        return theta_f - theta_g
    if 360 > (theta_g - theta_f) > 180:
        return theta_g - theta_f
        print("3) counterclockwise. Final: forwards")
    if (theta_g - theta_f) == (0 or 360):
        print("3) none. Final: forwards")
        return 0
    else:
        return 0


def animation(theta_f, xs, ys, xg, yg, angle1, angle2, robot):
    global counter, step

    clear()

    robot.draw_robot()
    if counter % 10000 == 0:
        print("step: " + str(step))
        print("x: " + str(robot.x) + ", y: " + str(robot.y))
        print("angle: " + str(robot.theta))

    # Rotate robot
    if step == 0:
        if angle1 > 0:
            robot.theta += TIMESTEP * robot.w
            if robot.theta >= angle1:
                step = 1
        elif angle1 < 0:
            robot.theta -= TIMESTEP * robot.w
            if robot.theta <= angle1:
                step = 1
        else:
            step = 1

    # Move straight
    if step == 1:
        robot.x += cos(theta_f) * TIMESTEP * robot.vx
        robot.y += sin(theta_f) * TIMESTEP * robot.vy
        if xs < xg and robot.x >= xg:
            if ys < yg and robot.y >= yg:
                step = 2
            elif ys > yg and robot.y >= yg:
                step = 2
        elif xs > xg and robot.x <= xg:
            if ys < yg and robot.y >= yg:
                step = 2
            elif ys > yg and robot.y >= yg:
                step = 2

    # Rotate robot again
    if step == 2:
        if angle2 > 0:
            robot.theta += TIMESTEP * robot.w
            if robot.theta >= angle2:
                step = 3
        elif angle2 < 0:
            robot.theta -= TIMESTEP * robot.w
            if robot.theta <= angle2:
                step = 3
        else:
            step = 3


def cost_animation(theta_s, theta_g, xs, ys, xg, yg):

    robot = Robot(xs, ys, theta_s)
    theta_f = calculate_arctan(xs, ys, xg, yg)
    angle1 = calculate_initial_rotation(theta_s, theta_f)
    angle2 = calculate_second_rotation(theta_g, theta_f)

    def main():
        animation(theta_f, xs, ys, xg, yg, angle1, angle2, robot)

    start_graphics(main, width=400, height=400)


cost_animation(30, 0, 20, 100, 50, 100)

