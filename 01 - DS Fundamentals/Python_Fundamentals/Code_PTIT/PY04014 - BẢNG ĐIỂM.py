from math import ceil
from decimal import Decimal, ROUND_HALF_UP

class Student:
    def __init__(self, id, name, components):
        self.maHocSinh = 'HS{:02d}'.format(id)
        self.hoTen = name
        self.diemTB = Student.calculate_diemTB(components)
        self.xepLoai = Student.calculate_rank(components)

    @staticmethod
    def calculate_diemTB(components):
        diemTB = components[0] * 2 + components[1] * 2
        for i in range(2, 10):
            diemTB += components[i]
        diemTB = diemTB / 12
        return ceil(diemTB*100) / 100

    @staticmethod
    def calculate_rank(components):
        if Student.calculate_diemTB(components) >= 9:
            return "XUAT SAC"
        elif Student.calculate_diemTB(components) >= 8:
            return "GIOI"
        elif Student.calculate_diemTB(components) >= 7:
            return "KHA"
        elif Student.calculate_diemTB(components) >= 5:
            return "TB"
        else:
            return "YEU"

    def get_info(self):
        return '{} {} {:.1f} {}'.format(self.maHocSinh, self.hoTen, self.diemTB, self.xepLoai)


list_student = []
for i in range(int(input())):
    name = input()
    components = list(map(float, input().split()))
    list_student.append(Student(i+1, name, components))

# sắp xếp theo điểm trung bình giảm dần, mã học sinh tăng dần
list_student.sort(key=lambda x: (-x.diemTB, x.maHocSinh))

for i in list_student:
    print(i.get_info())
