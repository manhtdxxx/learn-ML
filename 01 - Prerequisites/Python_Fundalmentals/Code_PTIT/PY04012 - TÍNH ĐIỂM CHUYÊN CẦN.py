class Student:
    def __init__(self, maSV, hoTen, lop, tick):
        self.maSV = maSV
        self.hoTen = hoTen
        self.lop = lop
        self.diemCC = Student.tinh_diemCC(tick)

    @staticmethod
    def tinh_diemCC(tick):
        diemCC = 10
        for i in tick:
            if i == 'v':
                diemCC -= 2
            elif i == 'm':
                diemCC -= 1
        if diemCC <= 0:
            return '0 KDDK'
        return diemCC

    def getIn4(self):
        return '{} {} {} {}'.format(self.maSV, self.hoTen, self.lop, self.diemCC)


n = int(input())

students = []
for _ in range(n):
    masv1 = input()
    hoten1 = input()
    lop1 = input()
    students.append({'maSV': masv1, 'hoTen': hoten1, 'lop': lop1})

ticks = {}
for _ in range(n):
    masv2, tick = input().split()
    ticks[masv2] = tick

for i in students:
    masv3 = i['maSV']
    hoten3 = i['hoTen']
    lop3 = i['lop']
    tick3 = ticks[masv3]

    student_object = Student(masv3, hoten3, lop3, tick3)
    print(student_object.getIn4())
