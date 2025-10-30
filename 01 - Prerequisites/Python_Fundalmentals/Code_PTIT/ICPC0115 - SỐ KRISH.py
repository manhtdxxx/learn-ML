def factorial(x):
    if x == 0:  # giai thua cua 0 la 1
        return 1
    else:
        return x * factorial(x - 1)

n_cases = int(input())
while n_cases > 0:
    x = int(input())

    factorial_of_digits = []
    for i in str(x):
        i = factorial(int(i))
        factorial_of_digits.append(i)

    if x == sum(factorial_of_digits):
        print('Yes')
    else:
        print('No')

    n_cases -= 1