n_cases = int(input())
while n_cases > 0:
    n = int(input())
    x = list(map(int, input().split()))

    count = 0
    for i1 in range(len(x)-2):
        for i2 in range(i1+1, len(x)-1):
            z = -(x[i1] + x[i2])
            if z in x[i2+1:len(x)]:
                count += 1

    print(count)

    n_cases -= 1
