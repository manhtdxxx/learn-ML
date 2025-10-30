import math

for _ in range(int(input())):
    deposit, interest, target = map(float, input().split())
    n = math.log(target / deposit, 1 + interest / 100)  # interest đang ở dạng %
    n = math.ceil(n)
    print(n)