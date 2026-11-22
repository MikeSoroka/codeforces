for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0 and n % 4 != 0:
        print("No")
    else:
        print("Yes")
