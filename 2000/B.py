#https://codeforces.com/problemset/problem/2000/B

import sys

data = sys.stdin.read().split()
n = int(data[0])
offset = 1

for i in range(n):
    res = True
    seats = int(data[offset])
    offset += 1
    taken = set()
    for j in range(seats):
        seat = int(data[offset])
        offset += 1
        if not taken:
            taken.add(seat)
        else:
            taken.add(seat)
            if not (seat - 1 in taken or seat + 1 in taken):
                res = False

    print("yes" if res else "no")
