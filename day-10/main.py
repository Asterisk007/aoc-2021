import os, sys
from typing import Match

f = open(sys.argv[1])
lines = f.readlines()

error_score = 0

right_paren_score = 3
right_square_score = 57
right_curly_score = 1197
right_angle_score = 25137

bracket_scores = {"(": 1, "[": 2, "{": 3, "<": 4}

char_pair = {"(": ")", "[": "]", "{": "}", "<": ">"}

completed_pairs = []
p2_scores = []

for line in lines:
    stack = []
    for char in line:
        if len(stack) == 0 or char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            if char_pair[stack[-1]] == char:
                stack.pop()
            else:
                if char == ')':
                    error_score += right_paren_score
                elif char == ']':
                    error_score += right_square_score
                elif char == '}':
                    error_score += right_curly_score
                elif char == '>':
                    error_score += right_angle_score
                stack = []
                break

    if stack:
        p2_score = 0
        while len(stack) > 0:
            p2_score = (p2_score*5) + bracket_scores[stack.pop()]
        p2_scores.append(p2_score)
    
print(error_score)
print(f"{len(p2_scores)} scores with middle {sorted(p2_scores)[len(p2_scores)//2]}")