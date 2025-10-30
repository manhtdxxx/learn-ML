class Invoice:
    def __init__(self, so_phong, ma_toa_nha, ten_chu_ho, so_kwh):
        self.so_phong = so_phong
        self.ma_toa_nha = ma_toa_nha
        self.ten_chu_ho = ten_chu_ho
        self.so_kwh = so_kwh
        self.tong_tien = Invoice.tong_tien(so_kwh)

    @staticmethod
    def tong_tien(so_kwh):
        if so_kwh <= 100:
            tien_dien = so_kwh * 1450
        elif 100 < so_kwh <= 150:
            tien_dien = 100 * 1450 + (so_kwh - 100) * 1750
        else:
            tien_dien = 100 * 1450 + 50 * 1750 + (so_kwh - 150) * 2000

        return tien_dien + 0.1 * tien_dien

    def getIn4(self):
        return '{} {} {} {} {}'.format(self.so_phong, self.ma_toa_nha, self.ten_chu_ho, self.so_kwh, self.tong_tien)


def normalize_name(name: str):
    parts = name.strip().split()
    parts = [i.capitalize() for i in parts]
    new_name = ' '.join(parts)
    return new_name


def is_name(name: str):
    name = normalize_name(name)
    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True


invoices = []
while True:
    try:
        # prompt to continue or not
        print('-' * 100)
        cont = input('DO YOU WANT TO CONTINUE? (Enter to continue / Type "n" to stop): ').strip().lower()
        if cont == 'n':
            break
        #
        soPhong = input('Nhập số phòng: ').strip()
        if not soPhong:
            raise ValueError('>>> ERROR: Số phòng phải không được để trống...')
        if not soPhong.isdigit() or len(soPhong) != 3 or int(str(soPhong)[-1]) <= 0 or int(str(soPhong)[0]) <= 0:
            raise ValueError('>>> ERROR: Số phòng có định dạng số xxx...')
        #
        maToaNha = input('Nhập mã tòa nhà: ').strip()
        maToaNha = maToaNha[0:2].upper() + maToaNha[2:]
        if not maToaNha:
            raise ValueError('>>> ERROR: Mã tòa nhà không được để trống...')
        if maToaNha[0:2] != 'CT' or len(maToaNha) != 3:
            raise ValueError('>>> ERROR: Mã tòa nhà có định dạng CT{x}...')
        #
        tenChuHo = input('Nhập tên chủ hộ: ').strip()
        tenChuHo = normalize_name(tenChuHo)
        if not tenChuHo:
            raise ValueError('>>> ERROR: Tên chủ hộ không được để trống...')
        if not is_name(tenChuHo):
            raise ValueError('>>> ERROR: Tên chủ hộ không chứa số...')
        #
        soKWh = int(input('Nhập số KWh tiêu thụ: ').strip())
        if int(soKWh) < 0:
            raise ValueError('>>> ERROR: Số KWh phải lớn hơn hoặc bằng 0...')

        # thêm object vào list
        invoices.append(Invoice(soPhong, maToaNha, tenChuHo, soKWh))

    except ValueError as e:  # nếu xảy ra value error thì thực thi câu lệnh except
        print(e)  # e là ValueError tương ứng với các lệnh raise trên
        continue  # vì lỗi nên bỏ qua vòng while này và lặp vòng tiếp


# LẬP TABLE XUẤT FILE TXT
if len(invoices) > 0:
    txt = open('../txt/dsdien.txt', 'w+', encoding='utf-8')
    # tạo header
    header = '| {:^10} | {:^10} | {:^17} | {:^10} | {:^17} |'.format('Số phòng', 'Mã tòa nhà',
                                                                     'Tên chủ hộ', 'Số Kwh',
                                                                     'Tổng tiền')
    txt.write(header + '\n')
    # nhập dữ liệu
    for i in invoices:
        row = '| {:^10} | {:^10} | {:^17} | {:^10} | {:^17} |'.format(i.so_phong, i.ma_toa_nha,
                                                                      i.ten_chu_ho, i.so_kwh,
                                                                      i.tong_tien)
        txt.write(row + '\n')

    # ghi xong thì con trỏ cuối file nên phải seek về 0 để đọc
    txt.seek(0)
    print(txt.read())
