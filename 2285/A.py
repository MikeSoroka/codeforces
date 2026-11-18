for _ in range(int(input())):
    n = int(input())

    prime = 1
    composite = 4
    perm = []

    if n < 4:
        print(-1)
    else:
        perm = list(range(1, n+1))
        perm[0], perm[3] = perm[3], perm[0]

        print(" ".join(map(str, perm)))