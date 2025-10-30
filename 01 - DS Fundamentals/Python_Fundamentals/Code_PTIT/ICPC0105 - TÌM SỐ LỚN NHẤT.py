n = int(input())

while n > 0:
    x = input()
    y = []
    max_number = 10**19
    current_number = ''
    for i in x:
        if i.isnumeric():
            current_number += i
        elif current_number != '' and int(current_number) < max_number:
            y.append(int(current_number))
            current_number = ''

    if current_number != '' and int(current_number) < max_number:
        y.append(int(current_number))

    print(max(y))

    n -= 1

