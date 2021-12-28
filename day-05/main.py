import os, sys

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

    if (coord_start[0] == coord_end[0] or
            coord_start[1] == coord_end[1]):
        coords.append(((coord_start[0], coord_start[1]), (coord_end[0], coord_end[1])))

#print(f"{len(coords)} lines that are strictly horizontal or vertical")

"""
    For each line:
        if x coordinates are equal:
            iterate from (x, i) to (x, j), increasing the intersection at each k where k = range(i, j)
            if one has been noted, and placing a marker otherwise
        else:
            iterate from (i, y) to (j, y), increasing the intersection at each k where k = range(i, j)
            if one has been noted, and placing a marker otherwise
"""
for coord in coords:
    #print(f"Line at {coord[0]} to {coord[1]}")
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
    else:
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

points = 0

for c in grid:
    if grid[c] >= 2:
        points += 1

print(points)