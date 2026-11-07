#https://codeforces.com/problemset/problem/2000/D/

for _ in range(int(input())):
    res = 0
    length = int(input())
    scores = list(map(int, input().split()))
    pref = [0]
    for i in range(length):
        pref.append(pref[-1] + scores[i])

    labels = input()
    l = 0
    r = length - 1

    while True:
        while l < length and labels[l] != "L":
            l += 1
        while r >= 0 and labels[r] != "R":
            r -= 1

        if l >= r:
            break
        res += pref[r + 1] - pref[l]
        l += 1
        r -= 1

    print(res)
