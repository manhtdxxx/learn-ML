class Invoice:
    def __init__(self,  id, name, quantity, price, discount):
        self.maMatHang = id
        self.tenMatHang = name
        self.soLuong = quantity
        self.donGia = price
        self.chietKhau = discount
        self.tongTien = Invoice.tinh_tien(quantity, price, discount)

    @staticmethod
    def tinh_tien(soLuong, donGia, chietKhau):
        return soLuong * donGia - chietKhau

    def getIn4(self):
        return '{} {} {} {} {} {}'.format(self.maMatHang, self.tenMatHang,
                                          self.soLuong, self.donGia,
                                          self.chietKhau, self.tongTien)

invoices = []
for i in range(int(input())):
    id = input()
    name = input()
    quantity = int(input())
    price = int(input())
    discount = int(input())

    invoices.append(Invoice(id, name, quantity, price, discount))


invoices.sort(key=lambda x: -x.tongTien)

for i in invoices:
    print(i.getIn4())
    print()