for _ in range(int(input())):
    s = input()
    count = 1
    encoded_s = ''
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            count += 1
        else:
            encoded_s += str(count)
            encoded_s += s[i]
            count = 1

    # chèn th cuối
    encoded_s += str(count)
    encoded_s += s[len(s)-1]

    print(encoded_s)