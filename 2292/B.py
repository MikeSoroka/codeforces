for _ in range(int(input())):
    n, k, p = map(int, input().split())
    scores = sorted(list(map(int, input().split())))
    cur_taken = 0
    scoresum = 0
    res = 0
    for score in scores:
        scoresum += score
        cur_taken += 1

        if cur_taken == k:
            if scoresum < p:
                res += p
            else:
                res += scoresum

            cur_taken = 0
            scoresum = 0

    res += scoresum

    print(res)
