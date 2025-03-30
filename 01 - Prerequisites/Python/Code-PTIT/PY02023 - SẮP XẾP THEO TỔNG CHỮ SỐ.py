n_cases = int(input())


def sum_of_digits(number):
    return sum(int(digits) for digits in str(number))


while n_cases > 0:
    n = int(input())
    numbers = list(map(int, input().split()))

    sorted_numbers = sorted(numbers, key=lambda x: (sum_of_digits(x), x))
    for i in sorted_numbers:
        print(i, end=' ')
    print()

    n_cases -= 1
