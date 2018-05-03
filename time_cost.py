from math import sqrt, atan2, pi

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
    arctan = atan2(ys-yg, xs-xg)
    return arctan

#work on different cases
def calculate_angle(theta_s, theta_g, arctan):
# think of different cases
    a = abs(arctan - theta_s) + abs(arctan - theta_g)
    b = 180 - abs(theta_s - theta_g) + theta_s + 180 - theta_g
    angle = min(a,b)

    print("the angle is: " + str(angle) + "a = " + str(a) + "b = " + str(b))

    return angle

def get_time_cost(xs,ys,xg,yg, theta_s, theta_g):

    global v, w

    d = calculate_distance(xs, ys, xg, yg)
    arctan = calculate_arctan(xs, ys, xg, yg)
    angle = calculate_angle(theta_s, theta_g, arctan)

    time_cost = d + angle

    return time_cost

get_time_cost(0,0,2,2, 30, 60)