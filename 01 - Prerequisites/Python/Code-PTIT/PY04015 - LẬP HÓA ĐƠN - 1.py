class Invoice:
    def __init__(self, id, name, pre_amount, post_amount):
        self.maSo = 'KH{:02d}'.format(id)
        self.hoTen = name
        self.tongTien = Invoice.tinhTien(pre_amount, post_amount)

    @staticmethod
    def tinhTien(pre_amount, post_amount):
        diff = post_amount - pre_amount
        if diff <= 50:
            total = diff * 100
            return total * 1.02
        elif 50 < diff <= 100:
            total = 50*100 + (diff-50)*150
            return total * 1.03
        else:
            total = 50*100 + 50*150 + (diff-100)*200
            return total * 1.05

    def get_info(self):
        return '{} {} {:.0f}'.format(self.maSo, self.hoTen, self.tongTien)


list_invoice = []
for i in range(int(input())):
    name = input()
    pre = int(input())
    post = int(input())
    #
    list_invoice.append(Invoice(i+1, name, pre, post))

# tổng số tiền giảm dần
list_invoice.sort(key=lambda x: (-x.tongTien, x.maSo))

#
for i in list_invoice:
    print(i.get_info())
