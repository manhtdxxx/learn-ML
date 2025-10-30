n = int(input())
def min_max_sum(p, q, x1, x2):
    p, q, x1, x2 = map(str, [p, q, x1, x2])
    x1 = x1.replace(p,q)
    x2 = x2.replace(p,q)
    return int(x1) + int(x2)

while n > 0:
    p, q = list(map(int, input().split()))
    x = list(map(int,input().split()))

    if len(x) > 1:
        x1, x2 = x[0], x[1]
    else:
        x1 = x[0]
        x2 = int(input())

    y1 = min_max_sum(p, q, x1, x2)
    y2 = min_max_sum(q, p, x1, x2)
    print(min(y1, y2), max(y1, y2))

    n -= 1