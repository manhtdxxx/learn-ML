for _ in range(int(input())):
    s = input()
    a = []
    for i in range(0, len(s)-1, 2):
        x = s[i]*int(s[i+1])
        a.append(x)

    a = ''.join(a)
    print(a)