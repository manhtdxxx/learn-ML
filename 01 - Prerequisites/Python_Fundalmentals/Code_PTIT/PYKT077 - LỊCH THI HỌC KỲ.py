from datetime import datetime

so_mon_hoc, so_ca_thi = map(int, input().split())

info_mh = {}  # dict

for i in range(so_mon_hoc):
    x = input()
    info_mh[x] = input()


class Schedule:
    def __init__(self, id_ca_thi, id_mh, name_mh, date, time, id_group):
        self.id_ca_thi = 'T{:03d}'.format(id_ca_thi)
        # 3d: 3 chu so nguyen, khi k du 3 chu so thi se fill 0 de thanh so nguyen 3 chu so
        self.id_mh = id_mh
        self.name_mh = name_mh
        self.date = date
        self.time = time
        self.id_group = id_group

        day, month, year = map(int, date.split('/'))
        hour, minute = map(int, time.split(':'))
        self.dateTime = datetime(year, month, day, hour, minute)  # dung thu vien datetime

    def show(self):
        return '{} {} {} {} {} {}'.format(self.id_ca_thi, self.id_mh, self.name_mh, self.date, self.time, self.id_group)


list_ca_thi = []
for i in range(so_ca_thi):
    x = input().split()
    list_ca_thi.append(Schedule(i + 1, x[0], info_mh[x[0]], x[1], x[2], x[3]))

list_ca_thi.sort(key=lambda a: (a.dateTime, a.id_ca_thi))

for i in list_ca_thi:
    print(i.show())
