import sys

cur_num = -1
last_num = cur_num

increases = 0

f = open(str(sys.argv[1]))
lines = f.readlines()

for line in lines:
    cur_num = int(line)
    if last_num < cur_num and last_num != -1:
        increases+=1
    last_num = cur_num

print(increases)