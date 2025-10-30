from datetime import datetime


class Gamer:
    def __init__(self, id, name, start_time, end_time):
        self.maNC = id
        self.tenNC = name
        self.howLong = (datetime.strptime(end_time, '%H:%M') -
                        datetime.strptime(start_time, '%H:%M'))
        # tra ve hh:mm:ss
        parts = str(self.howLong).split(':')
        self.hour = int(parts[0])  # để str thì 01, 02, 03 ...
        self.minute = int(parts[1])  # sang int thì 1, 2, 3

    def getIn4(self):
        return '{} {} {} gio {} phut'.format(self.maNC, self.tenNC, self.hour, self.minute)


gamers = []
for _ in range(int(input())):
    id = input()
    name = input()
    start = input()
    end = input()
    gamers.append(Gamer(id, name, start, end))


gamers.sort(key=lambda x: -x.howLong)

for i in gamers:
    print(i.getIn4())
