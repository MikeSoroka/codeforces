for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    cnt = {}
    res = 0
    left = 0
    right = n - k + 1 # right - excl

    for i in range(right):
        if nums[i] not in cnt:
            cnt[nums[i]] = 0

        cnt[nums[i]] += 1

    while True:
        if len(cnt.keys()) == 1:
            res += 1

        cnt[nums[left]] -= 1
        if cnt[nums[left]] == 0:
            cnt.pop(nums[left])
        left += 1
        right += 1

        if right > n:
            break
        if nums[right - 1] not in cnt:
            cnt[nums[right - 1]] = 0
        cnt[nums[right - 1]] += 1

    print(res)
