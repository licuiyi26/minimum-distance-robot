import re
from itertools import tee, islice, chain

def previous_and_next(movements_array):
    prevs, items, nexts = tee(movements_array, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)


x, y = 0, 0
directions = ["N", "E", "S", "W"]
facing = directions.index("N")  # set the default facing direction of the robot to be north

# set inputs
inputs = "F1,R1,B2,L1,B3"
movements = re.findall(r"[\w']+", inputs)

for previous, move, nxt in previous_and_next(movements):
    if move[0] == "R":
        facing = (facing + int(move[1])) % 4
    elif move[0] == "L":
        facing = (facing - int(move[1])) % 4

    if nxt is not None:
        if facing == 0:
            if nxt[0] == "F":
                y += int(nxt[1])
            elif nxt[0] == "B":
                y -= int(nxt[1])
        elif facing == 1:
            if nxt[0] == "F":
                x += int(nxt[1])
            elif nxt[0] == "B":
                x -= int(nxt[1])
        elif facing == 2:
            if nxt[0] == "F":
                y -= int(nxt[1])
            elif move[0] == "B":
                y += int(nxt[1])
        elif facing == 3:
            if nxt[0] == "F":
                x -= int(nxt[1])
            elif nxt[0] == "B":
                x += int(nxt[1])

print (x,y)