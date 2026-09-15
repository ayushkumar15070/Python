import math
import os
import random
import re
import sys

def gridlandMetro(n, m, k, track):
    rows = {}   
    for r, start, end in track:
        if r not in rows: 
            rows[r] = []

        rows[r].append((start, end))

    occupied = 0
    for intervals in rows.values():
        intervals.sort()
        current_start, current_end = intervals[0]
        for start, end, in intervals[1:]:
            if start <= current_end + 1:
                current_end = max(current_end, end)

            else:
                occupied = occupied + current_end - current_start + 1

                current_start = start
                current_end = end
        occupied = occupied + current_end - current_start + 1

    return n * m - occupied


if __name__ == "__main__":
    fptr  = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    track = []
    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')
    fptr.close()
