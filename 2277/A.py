from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))


    if n == 0:
        print(0)
    else:
        cn = Counter(nums)
        mex = 0
        under_mex = 0

        while True:
            if mex not in cn:
                print(mex)
                break
            elif cn[mex] + under_mex < k:
                print(mex)
                break
            else:
                diff = k - cn[mex]
                cn[mex] = max(0, cn[mex] - k)

                under_mex -= diff
                mex += 1
