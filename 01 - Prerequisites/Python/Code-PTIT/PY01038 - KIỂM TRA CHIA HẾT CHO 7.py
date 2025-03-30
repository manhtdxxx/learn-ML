def solve(x: int):
    if x % 7 == 0:
        return x
    for _ in range(1000):
        x += int(str(x)[::-1])
        if x % 7 == 0:
            return x
    return -1


for _ in range(int(input())):
    x = int(input())
    print(solve(x))
