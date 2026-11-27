for _ in range(int(input())):
    a, x, k = map(int, input().split())
    k += 1
    b, n = 0, 0

    while (2 ** (b + 1)) * (n + k) - k < x * ((b + 1) * k + n) + a:
        b += 1

    left = 0
    right = k - 1

    while left < right:
        mid = 1 + (left + right - 1) // 2

        if (2 ** b) * (mid + k) - k < x * (b * k + mid) + a:
            left = mid
        else:
            right = mid - 1

    print((b * k + left) * x + a)
