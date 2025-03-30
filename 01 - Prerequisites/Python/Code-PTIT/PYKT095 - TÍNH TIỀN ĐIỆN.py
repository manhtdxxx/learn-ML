class Invoice:
    def __init__(self, id, name, type, pre_index, post_index):
        self.maKH = 'KH{:02d}'.format(id)
        self.tenKH = Invoice.nomalize(name)
        self.ttdm, self.tvdm, self.vat, self.tienDien = Invoice.tinh_tien_dien(type, pre_index, post_index)

    @staticmethod
    def nomalize(name):
        parts = name.split()
        parts = [i.capitalize() for i in parts]
        nomalized_name = ' '.join(parts)
        return nomalized_name

    @staticmethod
    def tinh_tien_dien(type: str, pre: int, post: int):
        rated_power = {'A': 100, 'B': 500, 'C': 200}
        diff = post - pre
        if diff <= rated_power[type]:
            ttdm = diff * 450
            tvdm = 0
            vat = 0
            total = ttdm + tvdm + vat
            return ttdm, tvdm, vat, total

        elif diff > rated_power[type]:
            ttdm = rated_power[type] * 450
            tvdm = (diff - rated_power[type]) * 1000
            vat = ((diff - rated_power[type]) * 1000) // 20
            total = ttdm + tvdm + vat
            return ttdm, tvdm, vat, total

    def getIn4(self):
        return '{} {} {} {} {} {}'.format(self.maKH, self.tenKH, self.ttdm, self.tvdm, self.vat, self.tienDien)

invoices = []
for i in range(int(input())):
    tenkh = input()
    hgd, pre, post = input().split()  # str đó
    pre, post = int(pre), int(post)

    invoices.append(Invoice(i+1, tenkh, hgd, pre, post))


invoices.sort(key=lambda x: -x.tienDien)
for i in invoices:
    print(i.getIn4())