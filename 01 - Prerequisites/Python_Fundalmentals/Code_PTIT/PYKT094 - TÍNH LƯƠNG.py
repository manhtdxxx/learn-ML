def he_so_nhan(nhom: str, nam: int):
    if 1 <= nam <= 3:
        if nhom == 'A':
            return 10
        elif nhom == 'B':
            return 10
        elif nhom == 'C':
            return 9
        else:
            return 8

    elif 4 <= nam <= 8:
        if nhom == 'A':
            return 12
        elif nhom == 'B':
            return 11
        elif nhom == 'C':
            return 10
        else:
            return 9

    elif 9 <= nam <= 15:
        if nhom == 'A':
            return 14
        elif nhom == 'B':
            return 13
        elif nhom == 'C':
            return 12
        else:
            return 11

    else:
        if nhom == 'A':
            return 20
        elif nhom == 'B':
            return 16
        elif nhom == 'C':
            return 14
        else:
            return 13


class Staff:
    def __init__(self, id, name, base_salary, workdays, department_name) -> None:
        self.maNV = id
        # id gồm 5 char: 1 char đầu là nhóm, 2 char sau là số năm, 2 char sau là mã phòng ban
        self.tenNV = name
        self.luongCoBan = base_salary
        self.soNgayCong = workdays
        self.heSoNhan = he_so_nhan(self.maNV[0], int(self.maNV[1:3]))
        self.luongThang = self.tinh_luong()
        self.tenPhongBan = department_name

    def tinh_luong(self):  # có thể chuyển qua static method
        return self.luongCoBan * self.soNgayCong * self.heSoNhan * 10**3

    def getIn4(self):
        return '{} {} {} {}'.format(self.maNV, self.tenNV, self.tenPhongBan, self.luongThang)


department_list = {}
for _ in range(int(input())):
    department = input().split()
    department_id = department.pop(0)
    department_name = ' '.join(department)
    # thêm vào dict
    department_list[department_id] = department_name


staff_list = []
for _ in range(int(input())):
    staff_id = input()
    department_id2 = staff_id[3:]
    staff_name = input()
    base_salary = int(input())
    workdays = int(input())
    # thêm object vào list
    staff_list.append(Staff(staff_id, staff_name, base_salary, workdays,
                            department_list[department_id2]))

#
for i in staff_list:
    print(i.getIn4())


