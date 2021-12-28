import os, sys
from pprint import pprint

f = open(sys.argv[1])
lines = f.readlines()
f.close()

coords = []
grid = {}

#print(f"{len(lines)} total lines")

for line in lines:
    line_coord = line.split(" ")
    coord_start = line_coord[0].split(",")
    coord_start = [int(i) for i in coord_start]
    coord_end = line_coord[2].split(",")
    coord_end = [int(i) for i in coord_end]
    
    # For part two, we consider *all* lines.
    coords.append(((coord_start[0], coord_start[1]), (coord_end[0], coord_end[1])))

"""
    For each line:
        iterate from (i, j) to (k, l), increasing the intersection at each (r, t) where r = range(i, j) and t = range(k, l)
        if one has been noted, and placing a marker otherwise
"""
for coord in coords:
    if coord[0][0] == coord[1][0]:
        start = 0
        end = 0
        if coord[0][1] < coord[1][1]:
            start = coord[0][1]
            end = coord[1][1]
        else:
            start = coord[1][1]
            end = coord[0][1]
        #print(f"Marking points from ({coord[0][0]}, {start}) to ({coord[0][0]}, {end})")
        for i in range(start, end+1):
            if (coord[0][0], i) in grid.keys():
                grid[(coord[0][0], i)] += 1
            else:
                grid[(coord[0][0], i)] = 1
            #print(f"Mark = {grid[(coord[0][0], i)]}")
    
    elif coord[0][1] == coord[1][1]:
        start = 0
        end = 0
        if coord[0][0] < coord[1][0]:
            start = coord[0][0]
            end = coord[1][0]
        else:
            start = coord[1][0]
            end = coord[0][0]
        #print(f"Marking points from ({coord[0][1]}, {start}) to ({coord[0][1]}, {end})")
        for i in range(start, end+1):
            if (i, coord[0][1]) in grid.keys():
                grid[(i, coord[0][1])] += 1
            else:
                grid[(i, coord[0][1])] = 1
            #print(f"Mark = {grid[(i, coord[0][1])]}")
    
    else:
        start_x = coord[0][0]
        end_x = coord[1][0]

        start_y = coord[0][1]
        end_y = coord[1][1]

        iter_dir_x = 1
        iter_dir_y = 1
        if (start_x > end_x):
            iter_dir_x = -1
        if (start_y > end_y):
            iter_dir_y = -1

        i = start_x
        j = start_y

        for x in range(start_x, end_x + iter_dir_x, iter_dir_x):
            if (x, j) in grid.keys():
                grid[(x, j)] += 1
            else:
                grid[(x, j)] = 1
            j += iter_dir_y

points = 0

#print(f"{pprint(grid)}")

for c in grid:
    if grid[c] >= 2:
        points += 1

print(points)