file1 = open('.\\txt\\DATA1.in', 'r', encoding='utf-8')
file2 = open('.\\txt\\DATA2.in', 'r', encoding='utf-8')
# lúc nộp chỉ nhập path là tên file thôi nhé, code PTIT bị ngu!!!

text1 = file1.read().strip().lower()
text2 = file2.read().strip().lower()

list1 = []
list2 = []
current_text1 = ''
current_text2 = ''

# XỬ LÝ TEXT1
for i in text1:
    if i in '.!?;,':
        current_text1 = current_text1.strip()
        if len(current_text1) > 0:
            # current_text1 += i  # bình thường sẽ thêm dấu câu nhma trong TH này thì không
            list1.append(current_text1)
        current_text1 = ''
    elif i == '\n':
        current_text1 = current_text1.strip()
        if len(current_text1) > 0:
            list1.append(current_text1)
        current_text1 = ''
    else:
        current_text1 += i

# append dòng text cuối khi current text vẫn còn do k nằm trong TH 1,2
current_text1 = current_text1.strip()
if len(current_text1) > 0:
    list1.append(current_text1)

# XỬ LÝ TEXT2
for i in text2:
    if i in '.!?;,':
        current_text2 = current_text2.strip()
        if len(current_text2) > 0:
            current_text2 += i
            list2.append(current_text2)
        current_text2 = ''
    elif i == '\n':
        current_text2 = current_text2.strip()
        if len(current_text2) > 0:
            list2.append(current_text2)
        current_text2 = ''
    else:
        current_text2 += i

# append dòng text cuối khi current text vẫn còn do k nằm trong TH 1,2
current_text2 = current_text2.strip()
if len(current_text2) > 0:
    list2.append(current_text2)


# để tạo list
modified_text1 = ' '.join(list1)
modified_text2 = ' '.join(list2)

# chuyển từ list qua set để loại phần tử trùng nhau
split_text1 = set(modified_text1.split())
split_text2 = set(modified_text2.split())

#
only_in_text1 = split_text1.difference(split_text2)
only_in_text2 = split_text2.difference(split_text1)

# sắp xếp a,b,c... & đưa về list
only_in_text1 = sorted(only_in_text1)
only_in_text2 = sorted(only_in_text2)

# in kết quả
only_in_text1 = ' '.join(only_in_text1)
only_in_text2 = ' '.join(only_in_text2)

print(only_in_text1)
print(only_in_text2)
