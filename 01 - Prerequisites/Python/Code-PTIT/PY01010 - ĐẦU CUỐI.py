for _ in range(int(input())):
    x = int(input())
    x = str(x)
    if x[0] == x[-2] and x[1] == x[-1]:
        print('YES')
    else:
        print('NO')
