# https://codeforces.com/problemset/problem/2000/E/

from heapq import heappush, heappop

for _ in range(int(input())):
    rows, cols, k = map(int, input().split())
    gorillas = int(input())
    heights = sorted(map(int, input().split()), reverse = True)
    res = 0

    pq = []
    for i in range(rows):
        for j in range(cols):
            heappush(pq, - (min(k, i + 1) + min(0, rows - i - k)) * (min(k, j + 1) + min(0, cols - j - k)))

    for height in heights:
        tmp = heappop(pq)
        res -= height * tmp

    print(res)
