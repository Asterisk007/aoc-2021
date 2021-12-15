import sys

f = open(sys.argv[1])
lines = f.readlines()

grid = []
folds = []

# Data parsing
for line in lines:
    if ',' in line:
        coord = line.rstrip().split(",")
        grid.append((int(coord[0]), int(coord[1])))
    elif line.rstrip() != '':
        fold = line.rstrip().split("=")
        folds.append((fold[0][-1], int(fold[1])))

max_x = 0
max_y = 0

# Getting max coordinates to create a sufficiently large list
for (x, y) in grid:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

# And making the list
char_grid = [[ '.' for i in range(max_x+1) ] for j in range(max_y+1) ]

# Each coordinate is a dot that needs to be marked appropriately for
# proper code display. Put them onto the grid.
for (x, y) in grid:
    char_grid[y][x] = '#'

counter = 0
total_dots = 0

"""
    For each fold:
        If the fold is a Y-axis fold, iterate from the fold line to the end
        of the grid. For each character in each line, if the character is a '#',
        replace the appropriate mirrored cell on the grid. Chop off the rest of the
        grid once the fold is completed.

        If the fold is an X-axis fold, iterate over the length of the grid.
        For each character in each line from the start of the fold line to the length of the line,
        if the character is a '#', replace the appropriate mirrored cell on the grid.
        Chop off the rest of the grid once the fold is completed.
    
    Part one wants the number of '#' characters remaining once the first fold is completed,
    hence the extra logic
"""
for fold in folds:
    if fold[0] == "y":
        for i in range(fold[1], len(char_grid)):
            for j in range(0, len(char_grid[i])):
                if (char_grid[i][j] == '#' or char_grid[len(char_grid)-i-1][j] == '#'):
                    char_grid[len(char_grid)-i-1][j] = '#'
        char_grid[fold[1]:] = []
    elif fold[0] == "x":
        for i in range(0, len(char_grid)):
            for j in range(fold[1], len(char_grid[i])):
                if (char_grid[i][j] == '#' or char_grid[i][len(char_grid[i])-j-1] == '#'):
                    char_grid[i][len(char_grid[i])-j-1] = '#'
        for i in range(0, len(char_grid)):
            char_grid[i][fold[1]:] = []
    
    # For part one
    if counter == 0:
        for row in char_grid:
            for i in row:
                if i == '#':
                    total_dots += 1
        counter = 1

print(f"Part one: {total_dots}")

print("Part two:")
for row in char_grid:
    for char in row:
        if char == "#":
            print(char, end="")
        else:
            print(" ", end="")
    print()
