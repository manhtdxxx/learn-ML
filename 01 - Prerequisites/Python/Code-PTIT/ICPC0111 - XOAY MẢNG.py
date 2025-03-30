n_cases = int(input())
while n_cases > 0:
    n, d = map(int, input().split())
    x = list(map(int, input().split()))

    last_x = x[:d]
    first_x = x[d:]

    new_x = first_x + last_x
    new_x = map(str, new_x)
    new_x = ' '.join(new_x)
    print(new_x)

    n_cases -= 1
