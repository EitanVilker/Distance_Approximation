from time_cost import *
from robot import *
from math import cos, sin, atan2
from cs1lib import *

TIMESTEP = 1
counter = 0
step = 0


def calculate_arctan(xs, ys, xg, yg):
    arctan = (atan((ys-yg)/(xs-xg)))
    if arctan < 0:
        arctan = - arctan
    return arctan


def animation(theta_f, theta_s, theta_g, xs, ys, xg, yg, angle1, angle2, robot):
    global counter, step

    clear()

    robot.draw_robot()
    if counter % 10000 == 0:
        print("step: " + str(step))
        print("x: " + str(robot.x) + ", y: " + str(robot.y))
        print("angle: " + str(robot.theta))

    # Rotate robot
    if step == 0:
        if theta_f > theta_s:
            robot.theta += TIMESTEP * robot.w
            if robot.theta >= angle1:
                step = 1
        elif angle1 < theta_s:
            robot.theta -= TIMESTEP * robot.w
            if robot.theta <= angle1:
                step = 1
        else:
            step = 1

    if step == 0:

        if theta_s - robot.w < robot.theta < theta_s + robot.w:
            step = 1
        else:
            robot.theta += TIMESTEP * robot.w


    # Move straight
    if step == 1:
        print('theta f' + str(theta_f))

        robot.x += cos(theta_f) * TIMESTEP * robot.v
        robot.y -= sin(theta_f) * TIMESTEP * robot.v

        if xs < xg and robot.x >= xg:
            step = 2
            #if ys < yg and robot.y >= yg:
                #step = 2
            #elif ys > yg and robot.y >= yg:
                #step = 2
        elif xs > xg and robot.x <= xg:
            step = 2
            #if ys < yg  and robot.y >= yg:
                #step = 2
            #elif ys > yg and robot.y >= yg:
                #step = 2

    # Rotate robot again
    if step == 2:
        if theta_g - robot.w < robot.theta < theta_g + robot.w:
            step = 3
        else:
            if theta_g < theta_f:
                robot.theta -= TIMESTEP*robot.w
            else:
                robot.theta += TIMESTEP * robot.w


def cost_animation(theta_s, theta_g, xs, ys, xg, yg):

    commands = get_time_cost(xs,ys,xg,yg, theta_s, theta_g)
    robot = Robot(xs, ys, theta_s)
    theta_f = calculate_arctan(xs, ys, xg, yg)

    if commands[0] == 'CW':
        angle1 = commands[3]
    else:
        angle1 = - commands[3]
    if commands[1] == 'CW':
        angle2 = commands[4]
    else:
        angle2 = - commands[4]

    def main():
        animation(theta_f, theta_s, theta_g, xs, ys, xg, yg, angle1, angle2, robot)

    start_graphics(main, width=400, height=400)

cost_animation(0, 90, 200, 200, 300, 100)


