s = input()

count_upper = 0
count_lower = 0
for i in s:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1


if count_upper > count_lower:
    upper_s = s.upper()
    print(upper_s)
else:
    lower_s = s.lower()
    print(lower_s)
