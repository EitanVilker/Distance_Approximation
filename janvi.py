from math import sqrt, atan2, pi


#constants
v = 1 # velocity
w = 1 # angular velocity

def calculate_distance(xs, ys, xg, yg):
    d = sqrt((xs-xg)*(xs-xg) + (ys-yg)*(ys-yg))
    return d

def calculate_arctan(xs, ys, xg, yg):
    arctan = (atan2(ys-yg, xs-xg))*360/(2*pi)
    return arctan


#in 90 and 270 degrees, where it doesn't matter to move c or cc, made it move that orientation is forwards
def calculate_direction(tS, tG, tF):
    if (tS - tF) <= 90:
        print("1) clockwise 2) forward")
        if 180 >= (tG - tF) > 0:
            print("3) counterclockwise. Final: forwards")
            return (tS - tF) + ()
        if 360 > (tG - tF) > 180:
            print("3) clockwise. Final: forwards")
        if (tG - tF) == (0 or 360):
            print("3) none. Final: fowards")

    if 180 > (tS - tF) > 90:
        print("1) counterclockwise 2) backwards")
        if 180 >= (tG - tF) > 0:
            print("3) clockwise. Final: forwards")
        if 360 > (tG - tF) > 180:
            print("3) counterclockwise. Final: forwards")
        if (tG - tF) == (0 or 360):
            print("3) none. Final: fowards")

    if 270 > (tS - tF) > 180:
        print("1) clockwise 2) backwards")
        if 180 >= (tG - tF) > 0:
            print("3) clockwise. Final: forwards")
        if 360 > (tG - tF) > 180:
            print("3) counterclockwise. Final: forwards")
        if (tG - tF) == (0 or 360):
            print("3) none. Final: fowards")

    if 360 > (tS - tF) >= 270:
        print("1) counterclockwise 2) forward")
        if 180 >= (tG - tF) > 0:
            print("3) counterclockwise. Final: forwards")
        if 360 > (tG - tF) > 180:
            print("3) clockwise. Final: forwards")
        if (tG - tF) == (0 or 360):
            print("3) none. Final: fowards")

    #boundary cases
    if (tS - tF) == (0 or 360):
        print("1) none 2) forward")
    if (tS - tF) == 180:
        print("1) none 2) backwards")

    #NOTE: for second turn, the rotation is only dependent on whether initially backwards/forwards

    #def calculate_direction_efficiency(tS, tF, tG):


def calculate_distance(xS, yS, xG, yG, tS, tG):
    tF = calculate_arctan(xS, yS, xG, yG)
    calculate_direction(tS, tG, tF) #prints directions taken


#if turn right, straight, turn right is the fastest forwards. turn left, back, turn left is fastest backwards.
