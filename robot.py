import re
from itertools import tee, chain


def previous_and_current(movements_array):
    prevs, items = tee(movements_array, 2)
    prevs = chain([None], prevs)
    return zip(prevs, items)


x, y = 0, 0
directions = ["N", "E", "S", "W"]
facing = directions.index("N")  # set the default facing direction of the robot to be north

inputs = input("Please enter a string of commands （e.g. F1,R1,B2,L1,B3）：")
movements = re.findall("['\'F|'\'B|'\'R|'\'L][0-9]+", inputs.upper())  # validation

for previous, move in previous_and_current(movements):
    if previous is not None:
        if previous[0] == "R":
            facing = (facing + int(previous[1:])) % 4
        elif previous[0] == "L":
            facing = (facing - int(previous[1:])) % 4
        else:
            facing = facing  # if previous[0] is "F" or "B", keep the previous direction

        if move[0] == "F":
            if directions[facing] == "N":
                y += int(move[1:])
            elif directions[facing] == "E":
                x += int(move[1:])
            elif directions[facing] == "S":
                y -= int(move[1:])
            elif directions[facing] == "W":
                x -= int(move[1:])
        elif move[0] == "B":
            if directions[facing] == "N":
                y -= int(move[1:])
            elif directions[facing] == "E":
                x -= int(move[1:])
            elif directions[facing] == "S":
                y += int(move[1:])
            elif directions[facing] == "W":
                x += int(move[1:])
        else:
            continue  # if the current item starts "R" and "L", skip it

    else:   # means move[0] is the first element of the array
        facing = 0
        if move[0] == "F":
            y += int(move[1:])
        elif move[0] == "B":
            y -= int(move[1:])
        else:
            continue  # if the first item starts "R" and "L", skip it

print ("Final coordinates: (" + str(x) + "," + str(y) + ")")
distance = abs(x) + abs(y)
print ("The minimum amount of distance to get back to the starting point: " + str(distance) + " unit(s)")