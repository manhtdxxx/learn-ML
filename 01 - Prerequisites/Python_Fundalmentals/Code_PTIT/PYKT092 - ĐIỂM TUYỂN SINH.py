class Candidate:
    def __init__(self, id, name, score, ethnic, area):
        self.maTS = 'TS{:02d}'.format(id)
        self.hoTen = Candidate.nomalized(name)
        self.danToc = ethnic
        self.khuVuc = area

        priority_area = {1: 1.5, 2: 1, 3: 0}
        if self.danToc == 'Kinh':
            self.tongDiem = score + priority_area[area]
        else:
            self.tongDiem = score + priority_area[area] + 1.5

        if self.tongDiem >= 20.5:
            self.trangThai = 'Do'
        else:
            self.trangThai = 'Truot'

    @staticmethod
    def nomalized(name):
        parts = name.split()
        parts = [i.capitalize() for i in parts]
        nomalized_name = ' '.join(parts)
        return nomalized_name

    def getIn4(self):
        return '{} {} {:.1f} {}'.format(self.maTS, self.hoTen, self.tongDiem, self.trangThai)


candidates = []
for i in range(int(input())):
    name = input()
    diem_thi = float(input())
    dan_toc = input()
    khu_vuc = int(input())  # 1,2,3

    candidates.append(Candidate(i+1, name, diem_thi, dan_toc, khu_vuc))

candidates.sort(key=lambda x: (-x.tongDiem, x.maTS))

for i in candidates:
    print(i.getIn4())