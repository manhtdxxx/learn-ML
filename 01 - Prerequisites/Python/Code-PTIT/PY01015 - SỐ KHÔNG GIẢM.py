def is_so_k_giam(x: int):
    x = str(x)
    for i in range(len(x)-1):
        if int(x[i+1]) < int(x[i]):
            return False
    return True


for _ in range(int(input())):
    x = int(input())
    if is_so_k_giam(x):
        print('YES')
    else:
        print('NO')