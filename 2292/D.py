for _ in range(int(input())):
    n = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    costs = list(zip(left, right))
    diff = 0
    dp = [[0, 0] for i in range(n + 1)]

    for i in range(n - 1, -1, -1):
        x, y = costs[i]
        dp[i][0] = max(dp[i + 1][0] + x - y, dp[i + 1][1])
        dp[i][1] = min(dp[i + 1][1] + y - x, dp[i + 1][0])

    diff = dp[0][0]

    if diff > 0:
        print("Sunny")
    elif diff < 0:
        print("Aubrey")
    else:
        print("Draw")
