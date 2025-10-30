def sum_digits(x: int):
    total = 0
    for i in str(x):
        total += int(i)
    return total


def check(x: int):
    x = str(x)
    for i in range(len(x)-1):
        if abs(int(x[i+1]) - int(x[i])) != 2:
            return False
    return True


for _ in range(int(input())):
    x = int(input())
    if sum_digits(x) % 10 == 0 and check(x):
        print('YES')
    else:
        print("NO")

