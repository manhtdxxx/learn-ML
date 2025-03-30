from datetime import datetime


class Rain:
    def __init__(self, name, start_time, end_time, amount):
        self.maTram = ''
        self.tenTram = name
        self.howLong = ((datetime.strptime(end_time, '%H:%M') -
                        datetime.strptime(start_time, '%H:%M')).seconds / 3600)  # in hour
        self.luongMua = amount

    def getIn4(self):
        return '{} {} {:.2f}'.format(self.maTram, self.tenTram, self.luongMua / self.howLong)


rains = {}  # tạo set chứa cặp tenTram : object
current_maTram = 1
for i in range(int(input())):
    tenTram = input().strip()
    start = input().strip()
    end = input().strip()
    luongMua = int(input().strip())

    if tenTram not in rains:
        # chưa có thì tạo object mới
        rain_object = Rain(tenTram, start, end, luongMua)
        # thêm mới maTram vào object
        rain_object.maTram = 'T{:02d}'.format(current_maTram)
        current_maTram += 1
        # thêm object vào dict
        rains[tenTram] = rain_object
    else:
        # có r thì chỉ gọi object ra thui
        # cộng dồn thời gian mưa và lượng mua dzo!
        rains[tenTram].howLong += ((datetime.strptime(end, '%H:%M') -
                                   datetime.strptime(start, '%H:%M')).seconds / 3600)
        rains[tenTram].luongMua += luongMua


for i in rains:
    print(rains[i].getIn4())
