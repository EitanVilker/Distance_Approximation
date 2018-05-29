from math import sqrt, atan2, pi, atan, degrees


#constants
v = 1 # velocity
w = 1 # angular velocity

def calculate_distance(xs, ys, xg, yg):
    d = sqrt((xs-xg)*(xs-xg) + (ys-yg)*(ys-yg))
    return d

def calculate_arctan(xs, ys, xg, yg):
    #print("arctan2: " + str(degrees(atan2(yg-ys, xg-xs))))
    #print("actan: " + str(degrees(atan((yg-ys)/(xg-xs)))))
    # arctan = degrees(atan2((yg-ys),(xg-xs))) #unit: degrees
    arctan = degrees(atan((yg-ys)/(xg-xs)))
    return arctan

# output total time taken, along with directions of path
def calculate_timecost(xs,ys,xg,yg, tS, tG):
    switch = False
    if xs > xg:
        switch = True

    tF = calculate_arctan(xs,ys,xg,yg)
    #route = calculate_direction(tS, tG, tF)
    route = calculate_direction_efficiently(tS, tF, tG, switch)
    return (abs(route[0])*w + abs(route[1])*w) + calculate_distance(xs,ys,xg,yg)*v


#in 90 and 270 degrees, where it doesn't matter to move c or cc, made it move that orientation is forwards
def calculate_direction(tS, tG, tF):
    turns = [-1, -1]
    print("tS: " + str(tS))
    print("tF: " + str(tF))
    print("tG: " + str(tG))

    if 0 < (tS - tF) <= 90:
        turns[0] = tS - tF
        print("1) clockwise 2) forward")
        if 180 >= (tG - tF) > 0:
            turns[1] = tG - tF
            print("3) counterclockwise. Final: forwards")

        if 360 > (tG - tF) > 180:
            turns[1] = 360 + tF - tG
            print("3) clockwise. Final: forwards")

        if (tG - tF) == (0 or 360):
            turns[1] = 0
            print("3) none. Final: fowards")

    if 180 > (tS - tF) > 90:
        turns[0] = tF - tS - 180
        print("1) counterclockwise 2) backwards")

        if 180 >= (tG - tF) > 0:
            turns[1] = tF + 180 - tG
            print("3) clockwise. Final: forwards")

        if 360 > (tG - tF) > 180:
            turns[1] = tG - tF - 180
            print("3) counterclockwise. Final: forwards")

        if (tG - tF) == (0 or 360):
            turns[1] = 0
            print("3) none. Final: fowards")

    if 270 > (tS - tF) > 180:
        turns[0] = 360 + tF - tS
        print("1) clockwise 2) backwards")

        if 180 >= (tG - tF) > 0:
            turns[1] = tF + 180 - tG
            print("3) clockwise. Final: forwards")

        if 360 > (tG - tF) > 180:
            turns[1] = tG - tF - 180
            print("3) counterclockwise. Final: forwards")

        if (tG - tF) == (0 or 360):
            turns[1] = 0
            print("3) none. Final: fowards")

    if 360 > (tS - tF) >= 270:
        turns[0] = tF + 360 - tS
        print("1) counterclockwise 2) forward")

        if 180 >= (tG - tF) > 0:
            turns[1] = tG - tF
            print("3) counterclockwise. Final: forwards")

        if 360 > (tG - tF) > 180:
            turns[1] = 360 + tF - tG
            print("3) clockwise. Final: forwards")

        if (tG - tF) == (0 or 360):
            turns[1] = 0
            print("3) none. Final: fowards")

    #boundary cases
    if (tS - tF) == 0 or (tS - tF) == 360:
        turns[0] = 0
        print("1) none 2) forward")
    if (tS - tF) == 180:
        turns[0] = 0
        print("1) none 2) backwards")
    if (tG - tF) == 0 or tG - tF == 360:
        turns[1] = 0
        print("3) none. Final: fowards")

    return turns


# start = how much need to rotate before can move forward
def calculate_direction_efficiently(tS, tF, tG, switch):
    turn1 = None  # turn1 --> true is clockwise (f = cc)
    direction = None  # direction --> true is forwards (f = back)
    turn2 = None  # turn 2 --> true is clockwise (f = cc)
    turns = [-1, -1]

    start = tS - tF
    if tS - tF < 0:
        start = tS - tF + 360


    if 0 < start <= 90:  # option 1: 1) clockwise 2) forward
        turns[0] = tS - tF % 360
        turn1 = True
        direction = True

    if 180 > start > 90: #option 2: 1) counterclockwise 2) backwards
        turns[0] = tF - tS - 180 % 360
        turn1 = False
        direction = False

    if 270 > start > 180: #option 3: 1) clockwise 2) backwards
        turns[0] = tF - tS + 360 % 360
        turn1 = True
        direction = False

    if 360 > start >= 270: #option 4: 1) counterclockwise 2) forward
        turns[0] = tF - tS + 360 % 360
        turn1 = False
        direction = True

    #step 2 & 3 have the same, second angle. step 2 & 3 combine into:

    final = tG - tF
    if tG - tF < 0:
        final = tG - tF + 360

    if (direction == False): # when vehicle enters backwards
        if 180 >= final > 0: # 3) clockwise. Final: forwards
            turns[1] = (tF - tG + 180) % 360
            turn2 = True

        if 360 > final > 180: # 3) counterclockwise. Final: forwards
            turns[1] = (tG - tF - 180) % 360
            turn2 = False

    #step 1 & 4 have the same, second angle. step 1 & 4 combine into:
    if (direction == True): # when vehicle enters forwards
        if 180 >= final > 0: # 3) counterclockwise. Final: forwards
            turns[1] = tG - tF % 360
            turn2 = False

        if 360 > final > 180: # 3) clockwise. Final: forwards
            turns[1] = (360 + tF - tG) % 360
            turn2 = True

    # boundary cases
    if (tS - tF) == 0 or (tS - tF) == 360: # 1) none 2) forward
        turns[0] = 0
        turn1 = None # ERROR TO BE FIXED
        direction = True
    if (tS - tF) == 180: # 1) none 2) backwards
        turns[0] = 0
        turn1 = None
        direction = False
    if tG - tF == 0 or tG - tF == 360: # 3) none. Final: fowards
        turns[1] = 0
        turn2 = None

    # if tS > tF, everything opposite
    if switch:
        turn1 = not turn1
        turn2 = not turn2
        direction = not direction

    #print directions
    if turn1 == True:
        print("1) clockwise")
    if turn1 == False:
        print("1) counterclockwise")
    if turn1 == None:
        print("1) don't turn")
    if direction == True:
        print("2) forwards")
    if direction == False:
        print("2) backwards")
    if turn2 == True:
        print("3) clockwise")
    if turn2 == False:
        print("3) counterclockwise")
    if turn2 == None:
        print("3) don't turn")

    print("turn 1: " + str(turns[0]))
    print("turn 2: " + str(turns[1]))

    return turns

#TESTING... ALL SUCCESSFUL CASES
#print("------")
#print(calculate_timecost(1,1,4,4, 30, 80))
#print("------")
#print(calculate_timecost(4,4,1,1, 30, 80))
#print(calculate_timecost(1,1,4,4, 50, 40))
#print(calculate_timecost(1, 1, 4, 4, -160, -130))
#print(calculate_timecost(1, 1, 4, 4, -160, -160))
#print(calculate_timecost(1, 5, 4, 4, 50, 40))
print(calculate_timecost(100, 100, 200, 200, 0, 10))


