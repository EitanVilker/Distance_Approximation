from math import sqrt, atan, pi

# today:
# 1: add cases to code
# 2: test code and see if we can find pattern that connects things for angles
# 3: figure out how to plot

#constants
v = 1 # velocity
w = 1 # angular velocity

def calculate_distance(xs,ys, xg,yg):
    d = sqrt((xs-xg)*(xs-xg) + (ys-yg)*(ys-yg))
    return d

def calculate_arctan(xs,ys, xg, yg):
    arctan = (atan((ys-yg)/( xs-xg)))*360/(2*pi)
    #print(arctan)
    if arctan < 0:
        arctan = - arctan
    print(arctan)
    return arctan

#work on different cases
def calculate_angle(theta_s, theta_g, arctan):

    turn1 = 'no turn'
    turn2 = 'no turn'

    if theta_s > 0 and theta_g > 0:
        a = abs(arctan - theta_s) + abs(arctan - theta_g)
        b = arctan + abs(180-theta_s) + arctan + abs(180-theta_g)

        if min(a,b) == a:
            if arctan > theta_s:
                turn1 = 'counterclockwise'
            elif arctan < theta_s:
                turn1 = 'clockwise'
            if arctan > theta_g:
                turn2 = 'clockwise'
            elif arctan < theta_g:
                turn2 = 'counterclockwise'
        else:
            if arctan > theta_s:
                turn1 = 'clockwise'
            elif arctan < theta_s:
                turn1 = 'counterclockwise'
            if arctan > theta_g:
                turn2 = 'counterclockwise'
            elif arctan < theta_g:
                turn2 = 'clockwise'

        print(turn1 + ' ' + turn2)
    else:
        a = abs(arctan - theta_s) + abs(arctan - theta_g)
        b = abs(180 + theta_s - arctan) + abs(180 + theta_g - arctan)

        if min(a,b) == a:
            if 180 - arctan > abs(theta_s):
                turn1 = 'clockwise'
            elif arctan < abs(theta_s):
                turn1 = 'counterclockwise'
            if arctan > abs(theta_g):
                turn2 = 'counterclockwise'
            elif arctan < abs(theta_g):
                turn2 = 'clockwise'
        else:
            if abs(180 - arctan) > abs(theta_s):
                turn1 = 'clockwise'
            elif abs(180 -arctan)< abs(theta_s):
                turn1 = 'counterclockwise'
            if abs(180 - arctan) > abs(theta_g):
                turn2 = 'counterclockwise'
            elif abs(180 - arctan) < abs(theta_g):
                turn2 = 'clockwise'
        print(turn1 + ' ' + turn2)

    angle = min(a, b)

    print("the angle is: " + str(angle) + ";  a = " + str(a) + ";  b = " + str(b))

    return angle

def get_time_cost(xs,ys,xg,yg, theta_s, theta_g):

    global v, w

    d = calculate_distance(xs, ys, xg, yg)
    arctan = calculate_arctan(xs, ys, xg, yg)
    angle = calculate_angle(theta_s, theta_g, arctan)

    time_cost = d + angle

    print('Timecost ' + str(time_cost))
    return time_cost

# testing different cases
get_time_cost(4,4,1,1,-160, -130)  # give counter + forward +  counter
get_time_cost(4,4,1,1, -160, -160) # give counter + backward + clockwise
get_time_cost(1,1,4,4,-160, -130)  # give counter + backward + counter

