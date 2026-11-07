#https://codeforces.com/contest/2000/problem/A

import sys

data = sys.stdin.read().split()
for i in range(1, int(data[0]) + 1):
    curr = data[i]
    if len(curr) > 2 and curr[0] == '1' and curr[1] == '0' and curr[2] != '0' and (len(curr) > 3 or curr[2] != '1'):
        print("yes")
    else:
        print("no")