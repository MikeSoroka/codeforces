INF = float("inf")

for _ in range(int(input())):
    n = int(input())
    perm = list(map(int, input().split()))

    if n == 1:
        print(1)
    else:
        res = 0

        indmap = {i: -1 for i in range(1, n + 1)}

        mins = []
        minrange = {i: [-INF, INF] for i in range(1, n + 1)}
        for index, val in enumerate(perm):
            indmap[val] = index

            while mins and val < mins[-1][1]:
                lastind, lastval = mins.pop()
                minrange[lastval][1] = index - lastind - 1


            if mins:
                minrange[val][0] = index - mins[-1][0] - 1
            mins.append([index, val])

        leftmost = perm[0]
        r = minrange[leftmost][1]
        if r == INF:
            res += n
        else:
            res += r + 1
        minrange.pop(leftmost)


        rightmost = perm[-1]
        l = minrange[rightmost][0]
        if l == -INF:
            res += n
        else:
            res += l + 1
        minrange.pop(rightmost)

        for key in minrange:
            l, r = minrange[key]
            if l == 0:
                if r == INF:
                    res += n - indmap[key]
                else:
                    res += r + 1
            elif r == 0:
                if l == -INF:
                    res += 1 + indmap[key]
                else:
                    res += l + 1
            else:
                res += 2

        print(res)
