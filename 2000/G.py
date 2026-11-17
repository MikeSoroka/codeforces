from heapq import heappush, heappop

adj = []



def is_fit(start, n, call_start, call_end, limit):
    pq = [(start, 1)]
    dists = [-1] * (n + 1)

    while pq:
        cur_dist, cur_node = heappop(pq)
        if dists[cur_node] != -1:
            continue
        if cur_dist > limit:
            return False
        if cur_node == n:
            return True


        dists[cur_node] = cur_dist

        for neig, d1, d2 in adj[cur_node]:
            if dists[neig] != -1:
                continue
            if cur_dist + d1 <= call_start or cur_dist >= call_end:
                new_dist = cur_dist + d1
            else:
                new_dist = min(cur_dist + d2, call_end + d1)
            heappush(pq, (new_dist, neig))

    return False

for _ in range(int(input())):
    crosses, roads = map(int, input().split())
    limit, call_begin, call_end = map(int, input().split())
    adj = [[] for i in range(crosses + 1)]
    for _ in range(roads):
        x, y, d1, d2 = map(int, input().split())
        adj[x].append((y, d1, d2))
        adj[y].append((x, d1, d2))
    left = 0
    right = limit

    while left < right:
        mid = left + (right - left + 1) // 2

        if is_fit(mid, crosses, call_begin, call_end, limit):
            left = mid
        else:
            right = mid - 1

    if is_fit(left, crosses, call_begin, call_end, limit):
        print(left)
    else:
        print(-1)

