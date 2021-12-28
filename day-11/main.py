import sys
from pprint import pprint

class Octopus:
    power = 0
    flashes = 0
    neighbors = []
    def __init__(self, p) -> None:
        self.power = p
        self.flashes = 0
        self.neighbors = []
    def flash(self, op):
        if self.power > 9:
            self.flashes += 1
            self.power = 0
            for neighbor in self.neighbors:
                op[neighbor].increase_power(op)
    def increase_power(self, op):
        self.power += 1
        #if self.power > 9:
        #    self.flash(op)
    def __str__(self) -> str:
        return f"Power: {self.power}; Flashes: {self.flashes}; Neighbors: {self.neighbors}"
    def __repr__(self) -> str:
        return self.__str__()


assert len(sys.argv) == 2

f = open(sys.argv[1])
lines = f.readlines()

op = {}
x = 0
y = 0
max_x = 0

for line in lines:
    for i in line.rstrip():
        i = int(i)
        op[(x, y)] = Octopus(i)
        x += 1
    if max_x == 0:
        max_x = x
    x = 0
    y += 1

max_y = y

x = 0
y = 0

# Corners
op[(0,0)].neighbors.extend([(1, 0), (0, 1), (1, 1)])
op[(max_x-1, 0)].neighbors.extend([(max_x-2, 0), (max_x-2, 1), (max_x-1, 1)])
op[(0, max_y-1)].neighbors.extend([(0, max_y-2), (1, max_y-2), (1, max_y-1)])
op[(max_x-1, max_y-1)].neighbors.extend([(max_x-2, max_y-2), (max_x-2, max_y-1), (max_x-1, max_y-2)])

# Top and bottom edges
for i in range(1, max_x-1):
    op[i, 0].neighbors.extend([(i-1, 0), (i+1, 0), (i-1, 1), (i, 1), (i+1, 1)])
    op[i, max_y-1].neighbors.extend([(i-1, max_y-1), (i+1, max_y-1), (i-1, max_y-2), (i, max_y-2), (i+1, max_y-2)])

# left and right edges
for i in range(1, max_y-1):
    op[0, i].neighbors.extend([(0, i-1), (0, i+1), (1, i), (1, i-1), (1, i+1)])
    op[max_x-1, i].neighbors.extend([(max_x-1, i-1), (max_x-2, i-1), (max_x-2, i), (max_x-2, i+1), (max_x-1, i+1)])

# The rest (middle area)
for j in range(1, max_y-1):
    for i in range(1, max_x-1):
        top_left = (i-1, j-1)
        top = (i, j-1)
        top_right = (i+1, j-1)
        left = (i-1, j)
        right = (i+1, j)
        bottom_left =(i-1, j+1)
        bottom = (i, j+1)
        bottom_right = (i+1, j+1)
        
        op[(i, j)].neighbors.extend([top_left, top, top_right, left, right, bottom_left, bottom, bottom_right])

#pprint(op, indent=4)

# Calculate flashes for 100 iterations
for i in range(0, 100):
    for p in op:
        op[p].increase_power(op)
    for p in op:
        op[p].flash(op)


total_flashes = 0

for p in op:
    total_flashes += op[p].flashes

print(total_flashes)
