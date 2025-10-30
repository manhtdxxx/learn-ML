n = int(input('Nhập vào số lượng phần tử trong dãy số: '))
x = [int(i) for i in input('Nhập vào dãy số: ').split()]
empty = []

for i in x :
    if len(empty) == 0:
        empty.append(i)
    else:
        if (empty[-1] + i) % 2 == 0:
            empty.pop(-1)
        else:
            empty.append(i)

print(len(empty))