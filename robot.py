x,y = 0,0 # current direction
direction = 0 # set the default direction of the robot to be north

# north = 0
# east = 1
# south = 2
# west = 3

# set inputs
movements = "F1,R1,B2,L1,B3"
movements = re.findall(r"[\w']+", inputs)

for move in movements:
    print(move[0])