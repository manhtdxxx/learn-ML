class Contestant:
    def __init__(self, id, name, theory_score, practice_score):
        self.maTS = 'TS0{}'.format(id)  # vcc đề ncc
        self.tenTS = name
        self.diemLyThuyet = self.normalize_score(theory_score)
        self.diemThucHanh = self.normalize_score(practice_score)
        self.diemTB = (self.diemLyThuyet + self.diemThucHanh) / 2
        self.xepLoai = self.classify(self.diemTB)

    def normalize_score(self, score: float):
        str_score = str(score)
        if score > 10:
            new_score = str_score[0] + '.' + str_score[1]
            return float(new_score)
        else:
            return score

    def classify(self, avg_score: float):
        if avg_score < 5:
            return "TRUOT"
        elif 5 <= avg_score < 8:
            return "CAN NHAC"
        elif 8 <= avg_score <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    def getIn4(self):
        return '{} {} {:.2f} {}'.format(self.maTS, self.tenTS, self.diemTB, self.xepLoai)


contestants = []
for i in range(int(input())):
    name = input()
    dlt = float(input())
    dth = float(input())

    contestants.append(Contestant(i+1, name, dlt, dth))

# sắp xếp theo điểm trung bình giảm dần
contestants.sort(key=lambda x: -x.diemTB)

for i in contestants:
    print(i.getIn4())