import sys
from pprint import pprint         

f = open(sys.argv[1])
lines = f.readlines()

numbers = []

boards = []
board = []
row = []

for line in lines:
    line = line.rstrip()
    if ',' in line:
        numbers = line.split(',')
    else:
        if line != "":
            for n in line.split():
                row.append([n, False])
            board.append(row)
            row = []
        else:
            if board != []:
                boards.append(board)
                board = []
#pprint(boards)

winning_board = None

for num in numbers:
    print(num)
    for board in boards:
        for rows in board:
            for i in rows:
                if num == i[0]:
                    i[1] = True
    for board in boards:
        winning_board = board
        for rows in board:
            for i in rows:
                if i[1] == False:
                    winning_board = None
            if winning_board is not None:
                break

pprint(winning_board)
