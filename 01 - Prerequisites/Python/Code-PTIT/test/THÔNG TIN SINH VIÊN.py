import os


class Student:
    def __init__(self, id, name, gpa, unearned_credits):
        self.maSV = id
        self.hoTen = name
        self.diemTichLuy = gpa
        self.soTinChi_chuaDat = unearned_credits
        self.duDK_lamBLTN = Student.can_do_dissertation(gpa, unearned_credits)
        self.xepLoai = Student.classify(gpa)

    @staticmethod
    def can_do_dissertation(gpa: float, unearned_credits: int) -> bool:
        if gpa >= 2.8 and unearned_credits <= 5:
            return True
        else:
            return False

    @staticmethod
    def classify(gpa: float) -> str:
        if gpa >= 3.5:
            return 'XUẤT SẮC'
        elif gpa >= 3.2:
            return 'GIỎI'
        elif gpa >= 2.5:
            return 'KHÁ'
        elif gpa >= 2.0:
            return 'TRUNG BÌNH'


students = []
while True:
    try:
        # prompt de thoat khoi vong while
        print('-' * 100)
        cont = input('DO YOU WANT TO ADD STUDENTS? (Enter to continue / Type "n" to stop): ').strip().lower()
        if cont == 'n':
            break

        # nhap thong tin
        masv = input('Nhập mã sinh viên: ').strip()
        if not masv:
            raise ValueError('>>> ERROR: mã sinh viên không được để trống.....')

        hoten = input('Nhập họ và tên: ').strip()
        if not hoten:
            raise ValueError('>>> ERROR: họ và tên không được để trống.....')

        gpa = float(input('Nhập điểm tích lũy: '))
        if gpa < 0:
            raise ValueError('>>> ERROR: điểm tích lũy phải >= 0.....')

        un_credits = int(input('Nhập số tín chỉ chưa đạt: '))

        # dien input vao object r nem vao list
        students.append(Student(masv, hoten, gpa, un_credits))

    except ValueError as e:
        print(e)
        continue

# nhap lua chon
pick = int(input('Nhập lựa chọn: '))

if pick == 1:
    # tao file
    file_name = 'dskl.txt'
    with open(file_name, 'a+', encoding='utf-8') as file:

        # neu file chua ton tai hoac size file = 0 thi nhap header
        if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
            header = '| {:^20} | {:^30} | {:^20} | {:^20} |\n'.format('Mã sinh viên',
                                                                      'Họ và tên',
                                                                      'Điểm tích lũy',
                                                                      'Số tín chỉ chưa đạt')
            file.write(header)

        # nhap du lieu
        for i in students:
            if i.duDK_lamBLTN:
                row = '| {:^20} | {:^30} | {:^20} | {:^20} |\n'.format(i.maSV,
                                                                       i.hoTen,
                                                                       i.diemTichLuy,
                                                                       i.soTinChi_chuaDat)
                file.write(row)

        # sau khi write thi con tro o cuoi file nen can chinh ve 0
        file.seek(0)
        print(file.read())


elif pick == 2:
    # tao file
    file_name = 'xlsv.txt'
    with open(file_name, 'a+', encoding='utf-8') as file:

        # neu file chua ton tai hoac size file = 0 thi nhap header
        if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
            header = '| {:^20} | {:^30} | {:^15} | {:^20} |\n'.format('Mã sinh viên',
                                                                      'Họ và tên',
                                                                      'Điểm tích lũy',
                                                                      'Xếp loại')
            file.write(header)

        # nhap du lieu
        for i in students:
            row = '| {:^20} | {:^30} | {:^15} | {:^20} |\n'.format(i.maSV,
                                                                   i.hoTen,
                                                                   i.diemTichLuy,
                                                                   i.xepLoai)
            file.write(row)

        # sau khi write thi con tro o cuoi file nen can chinh ve 0
        file.seek(0)
        print(file.read())
