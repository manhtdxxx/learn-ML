def lucky_num(x):
    for i in str(x):
        if i != '4' and i != '7':
            # and : phải khác cả 4 và 7
            # or : giả sử i == 4 thì i != 7 thì câu if đó sẽ thực thi return False
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    if lucky_num(n):
        print('YES')
    else:
        print('NO')
