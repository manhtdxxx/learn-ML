n_cases = int(input())
while n_cases > 0:
    n = int(input())
    x = list(map(int, input().split()))

    max_sum = 0
    for _ in range(3):
        max_i = min(x)
        max_sum += max_i
        x.remove(max_i)

    print(max_sum)

    n_cases -= 1
