n = int(input())


def is_valid_ipv4(ipv4):
    x = list(map(str, ipv4.split('.')))
    if len(x) != 4:
        return False
    for i in x:
        if not i.isnumeric():
            return False
        if str(int(i)) != i:
            # 012.124.162.0 is not an ip 'cause there is 0 at first position of a number
            # '012' --> 12(int) --> '12'(str) != '012' ==> not an ip
            return False
        if int(i) < 0 or int(i) > 255:
            return False

    return True


while n > 0:
    ipv4 = input()
    check_ip = is_valid_ipv4(ipv4)
    if check_ip:
        print('YES')
    else:
        print('NO')

    n -= 1
