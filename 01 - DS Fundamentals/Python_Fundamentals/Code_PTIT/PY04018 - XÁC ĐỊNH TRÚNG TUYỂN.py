"""
Mã xét tuyển gồm 2 thành phần:
    Chữ cái đầu tiên ứng với môn học: A là Toán, B là Lý và C là Hóa;
    tiếp theo là 1 chữ số thể hiện mã ưu tiên.
"""


class Teacher:
    def __init__(self, maGV, hoTen, maXetTuyen, diemTinHoc, diemChuyenMon):
        self.maGV = 'GV{:02d}'.format(maGV)
        self.hoTen = hoTen

        mon_hoc = {'A': 'TOAN', 'B': 'LY', 'C': 'HOA'}
        self.monHoc = mon_hoc[maXetTuyen[0]]

        diem_uu_tien = {'1': 2.0, '2': 1.5, '3': 1.0, '4': 0.0}
        self.tongDiem = diemTinHoc*2 + diemChuyenMon + diem_uu_tien[maXetTuyen[1]]

        if self.tongDiem >= 18:
            self.ketQua = 'TRUNG TUYEN'
        else:
            self.ketQua = 'LOAI'

    def getIn4(self):
        return '{} {} {} {:.1f} {}'.format(self.maGV, self.hoTen, self.monHoc, self.tongDiem, self.ketQua)


teachers = []
for i in range(int(input())):
    name = input()
    id_xt = input()
    diem_tin = float(input())
    diem_chuyen_mon = float(input())

    teachers.append(Teacher(i+1, name, id_xt, diem_tin, diem_chuyen_mon))


teachers.sort(key=lambda x: -x.tongDiem)

for i in teachers:
    print(i.getIn4())