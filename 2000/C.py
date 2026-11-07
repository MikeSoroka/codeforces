#https://codeforces.com/problemset/problem/2000/C/

for _ in range(int(input())):
    l = int(input())
    template = input().split()

    for __ in range(int(input())):
        s = input()
        if len(s) != l:
            print("no")
            continue

        bijection = {}
        vals = set()
        for i in range(l):
            if template[i] not in bijection and s[i] not in vals:
                bijection[template[i]] = s[i]
                vals.add(s[i])
            elif template[i] in bijection and bijection[template[i]] == s[i]:
                continue
            else:
                print("no")
                break
        else:
            print("yes")

