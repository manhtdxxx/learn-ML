n_cases = int(input())
while n_cases > 0:
    n = int(input())
    x = list(map(int, input().split()))

    min_sum = 0
    for _ in range(3):
        min_i = min(x)
        min_sum += min_i
        x.remove(min_i)

    print(min_sum)

    n_cases -= 1
