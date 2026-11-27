def gcd(a, b):
    a, b= max(a, b), min(a, b)
    while b > 0:
        a %= b
        a, b = b, a

    return a


for _ in range(int(input())):
    l, a, b = map(int, input().split())
    ga = gcd(l, a)
    gb = gcd(b, l)

    print(l // (ga * gb // gcd(ga, gb)))
