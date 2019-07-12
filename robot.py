import re
from itertools import tee, islice, chain

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

x,y = 0,0
facing = 0 # set the default facing direction of the robot to be north

# north = 0
# east = 1
# south = 2
# west = 3

# set inputs
inputs = "F1,R1,B2,L1,B3"
movements = re.findall(r"[\w']+", inputs)

for previous, move, nxt in previous_and_next(movements):
    print(previous)
    print(move)
    print(nxt)
