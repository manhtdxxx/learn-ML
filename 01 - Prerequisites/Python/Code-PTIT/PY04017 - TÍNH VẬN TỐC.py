"""
Cuộc đua xe đạp bắt đầu từ 6h00 với độ dài quãng đường đua là 120 Km
"""
from datetime import datetime


class Biker:
    def __init__(self, name, unit, end_time):
        self.id = Biker.get_id(name, unit)
        self.name = name
        self.unit = unit
        self.time = (datetime.strptime(end_time, '%H:%M') -
                     datetime.strptime('6:00', '%H:%M')).seconds / 3600  # 1h = 3600s
        self.velocity = round(120 / self.time)

    @staticmethod
    def get_id(name: str, unit: str):
        id = ''
        for i in unit.split():
            id += i[0]
        for i in name.split():
            id += i[0]
        return id

    def getIn4(self):
        return '{} {} {} {} Km/h'.format(self.id, self.name, self.unit, self.velocity)


bikers = []
for _ in range(int(input())):
    name = input()
    unit = input()
    end_time = input()  # định dạng h:mm

    bikers.append(Biker(name, unit, end_time))

# xếp theo thành tích, time càng nhỏ thì về đích càng sớm
# nếu sắp xếp theo end_time thì phải đổi format từ str --> time
bikers.sort(key=lambda x: x.time)

for i in bikers:
    print(i.getIn4())
