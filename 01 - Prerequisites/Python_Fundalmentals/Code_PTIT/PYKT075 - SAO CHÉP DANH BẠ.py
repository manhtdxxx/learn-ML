file_01 = open('.\\txt\\SOTAY.txt', 'r', encoding='utf-8')
r = file_01.read()

x = []
for i in r.split('\n'):
    if len(i) > 0:  # LOẠI BỎ DÒNG TRỐNG
        x.append(i)


class Person:
    def __init__(self, d, m, y, name, contact):
        self.d = d
        self.m = m
        self.y = y
        self.name = name
        self.contact = contact

        list_name = name.split()  # TÁCH HỌ, ĐỆM, TÊN CHÍNH THÀNH LIST
        self.first_name = list_name[-1]  # LẤY TÊN CHÍNH
        self.last_middle_name = ' '.join(list_name[:len(x)-1])  # LẤY HỌ, ĐỆM

    def show(self):
        return '{}: {} {}/{}/{}'.format(self.name, self.contact, self.d, self.m, self.y)


y = []  # chua objects cua class person
current_date = ''
index_x = 0
while index_x < len(x):  # k dung for vi khong muon co dinh step
    if '/' in x[index_x]:  # neu chuoi chua date
        current_date = x[index_x].split()[1]  # bo chu 'ngay'
        # current_date += ... (cong don lai) khac voi current_date = ... (tao moi)

        index_x += 1  # date, name, contact, name, contact, date, name, contact, date, ....
    else:
        day, month, year = map(int, current_date.split('/'))  # tach ngay thang nam
        y.append(Person(day, month, year, x[index_x], x[index_x + 1]))

        index_x += 2


y.sort(key=lambda a: (a.first_name, a.last_middle_name))

with open('.\\txt\\DIENTHOAI.txt', 'w', encoding='utf-8') as file_02:
    for person in y:
        file_02.write(person.show() + '\n')
