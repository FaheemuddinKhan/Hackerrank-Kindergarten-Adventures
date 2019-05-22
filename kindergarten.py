#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(t):
    diagonals = [0] * len(t)
    values = [0] * len(t)
    for idx, currt in enumerate(t):
        diagonals[idx - currt] += 1
        values[0] += int(currt <= idx)
    for idx in range(1, len(t)):
        values[idx] = values[idx-1] - diagonals[idx - 1] + 1
    return values.index(max(values))+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
