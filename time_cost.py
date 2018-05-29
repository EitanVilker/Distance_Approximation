from math import sqrt, atan, pi, sin, cos

# today:
# 1: add cases to code
# 2: test code and see if we can find pattern that connects things for angles
# 3: figure out how to plot

#constants
v = 1 # velocity
w = 1 # angular velocity

start_greater = True
turn1 = "no turn"
turn2 = "no turn"
direction = "no move"

def calculate_distance(xs,ys, xg,yg):
    d = sqrt((xs-xg)*(xs-xg) + (ys-yg)*(ys-yg))
    return d

def dist_origin(xs,ys, xg, yg):
    global start_greater

    ds = sqrt(xs*xs + ys*ys)
    dg = sqrt(xg*xg + yg*yg)
    if ds < dg:
        start_greater = False
    return start_greater

def calculate_arctan(xs,ys, xg, yg):
    arctan = (atan((ys-yg)/( xs-xg)))*360/(2*pi)
    #print(arctan)
    if arctan < 0:
        arctan = - arctan
    #print(arctan)
    return arctan

#work on different cases
def calculate_angle(theta_s, theta_g, arctan, dist_origin):

    global turn1, turn2, direction

    if theta_s > 0 and theta_g > 0:

        a = abs(arctan - theta_s) + abs(arctan - theta_g)
        b = arctan + abs(180-theta_s) + arctan + abs(180-theta_g)

        if min(a,b) == a:

            if start_greater:
                direction = "B"
            else:
                direction = "F"

            if arctan > theta_s:
                turn1 = 'CCW'
            elif arctan < theta_s:
                turn1 = 'CW'
            if arctan > theta_g:
                turn2 = 'CW'
            elif arctan < theta_g:
                turn2 = 'CCW'
        else:

            if start_greater:
                direction = "F"
            else:
                direction = "B"


            if arctan > theta_s:
                turn1 = 'CW'
            elif arctan < theta_s:
                turn1 = 'CCW'
            if arctan > theta_g:
                turn2 = 'CCW'
            elif arctan < theta_g:
                turn2 = 'CW'

    else:
        a = abs(arctan - theta_s) + abs(arctan - theta_g)
        b = abs(180 + theta_s - arctan) + abs(180 + theta_g - arctan)

        if min(a,b) == a:

            if start_greater:
                direction = "B"
            else:
                direction = "F"


            if  arctan > abs(theta_s):
                turn1 = 'CW'
            elif arctan < abs(theta_s):
                turn1 = 'CCW'
            if arctan > abs(theta_g):
                turn2 = 'CCW'
            elif arctan < abs(theta_g):
                turn2 = 'CW'
        else:
            if start_greater:
                direction = "F"
            else:
                direction = "B"

            if abs(180 - arctan) > abs(theta_s):
                turn1 = 'CW'
            elif abs(180 -arctan)< abs(theta_s):
                turn1 = 'CCW'
            if abs(180 - arctan) > abs(theta_g):
                turn2 = 'CCW'
            elif abs(180 - arctan) < abs(theta_g):
                turn2 = 'CW'

    angle = min(a, b)
    if min(a,b) == a:
        turn1_angle = abs(arctan - theta_s)
        turn2_angle = abs(arctan - theta_g)
    else:
        if theta_s > 0 and theta_g > 0:
            turn1_angle = arctan + abs(180-theta_s)
            turn2_angle = arctan + abs(180-theta_g)
        else:
            turn1_angle = abs(180 + theta_s - arctan)
            turn2_angle = abs(180 + theta_g - arctan)

    # for simulation
    commands = [turn1,direction,turn2,turn1_angle, turn2_angle]
    return commands

    # uncomment if plotting
    # return angle

def get_time_cost(xs,ys,xg,yg, theta_s, theta_g):

    global v, w

    d = calculate_distance(xs, ys, xg, yg)
    arctan = calculate_arctan(xs, ys, xg, yg)
    dist_origin(xs,ys,xg,yg)
    commands = calculate_angle(theta_s, theta_g, arctan, dist_origin)

    time_cost = d + commands[3] + commands[4]

    print('Timecost: ' + str(time_cost) + '; ' + commands[0] + ' for ' + str(commands[3]) +'; ' + commands[1] + ' for ' + str(d) +'; ' + commands[2] + ' for ' + str(commands[4]))

    commands.append(d)
    # if plotting
    #return time_cost
    return commands

# testing different cases
get_time_cost(4,4,1,1,-160, -130)  # give counter + forward +  counter
get_time_cost(4,4,1,1, -160, -160) # give counter + forward + clockwise
get_time_cost(1,1,4,4,-160, -130)  # give counter + backward + counter
get_time_cost(1,1,4,4,30,80)   # counter + forward + clockwise
get_time_cost(1,5,4,4, 50, 40) #clockwise, forward, clockwise
sin(45)
cos(45)
