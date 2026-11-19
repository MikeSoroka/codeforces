for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    for num in nums:
        if num < n:
            print(n)
            break
    else:
        print(0)
