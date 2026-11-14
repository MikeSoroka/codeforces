# https://codeforces.com/problemset/problem/2000/F/

INF = float('inf')


def line_costs(a, b):
    cost = [0]
    total = 0
    while a > 0 and b > 0:
        if a == 1 and b == 1:
            total += 1
            cost += [total, total]
            break
        if a <= b:
            total += a
            b -= 1
        else:
            total += b
            a -= 1
        cost.append(total)
    return cost


for _ in range(int(input())):
    num_rectangles, target = map(int, input().split())
    rectangles = []
    for rect in range(num_rectangles):
        rectangles.append(list(map(int, input().split())))

    costs = [line_costs(a, b) for a, b in rectangles]

    table = [[0] * num_rectangles]
    for points in range(1, target + 1):
        dp = [INF] * num_rectangles
        for i in range(num_rectangles):
            cost = costs[i]
            best = dp[i - 1] if i > 0 else INF
            for q in range(1, min(points, len(cost) - 1) + 1):
                if i > 0:
                    before = table[points - q][i - 1]
                else:
                    before = 0 if q == points else INF
                if before + cost[q] < best:
                    best = before + cost[q]
            dp[i] = best
        table.append(dp)

    answer = table[target][num_rectangles - 1]
    print(answer if answer != INF else -1)