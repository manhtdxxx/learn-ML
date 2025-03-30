from datetime import datetime


class Invoice:
    def __init__(self, id, name, room, start_date, end_date, extra_service):
        self.id = 'KH{:02d}'.format(id)
        self.hoTen = name
        self.soPhong = room

        # strptime(string, format) : string to datetime
        self.soNgay = (datetime.strptime(end_date, "%d/%m/%Y") -
                       datetime.strptime(start_date, "%d/%m/%Y")).days + 1

        #
        price = {'1': 25, '2': 34, '3': 50, '4': 80}
        floor = str(room)[0]
        self.tongTien = self.soNgay * price[floor] + extra_service

    def getIn4(self):
        return '{} {} {} {} {}'.format(self.id, self.hoTen, self.soPhong, self.soNgay, self.tongTien)


list_invoice = []
for i in range(int(input())):
    name = input().strip()
    soPhong = int(input().strip())
    date1 = input().strip()
    date2 = input().strip()
    extra = int(input().strip())

    list_invoice.append(Invoice(i+1, name, soPhong, date1, date2, extra))

list_invoice.sort(key=lambda x: -x.tongTien)

for i in list_invoice:
    print(i.getIn4())
