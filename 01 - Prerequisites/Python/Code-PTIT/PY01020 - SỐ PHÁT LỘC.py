for _ in range(int(input())):
    n = int(input())
    n = str(n)
    if n[len(n)-1] == '6' and n[len(n)-2] == '8':
        print('YES')
    else:
        print('NO')