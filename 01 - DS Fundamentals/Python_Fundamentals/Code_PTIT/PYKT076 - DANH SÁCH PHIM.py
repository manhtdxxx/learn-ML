from datetime import datetime


class Film_Genre:
    def __init__(self, id, name):
        self.maTL = 'TL{:03d}'.format(id)
        self.tenTL = name


class Film:
    def __init__(self, id, name, release_date, episodes, genre):
        self.maPhim = 'P{:03d}'.format(id)
        self.tenPhim = name
        self.ngayKhoiChieu = datetime.strptime(release_date, '%d/%m/%Y')  # dùng để sort
        # tra ve format YYYY/DD/MM HH:MM:SS
        self.str_ngayKhoiChieu = release_date  # dùng để in kết quả
        self.soTapPhim = episodes
        self.theLoai = genre  # genre là 1 object chứa maTL, tenTL

    def getIn4(self):
        return '{} {} {} {} {}'.format(self.maPhim, self.theLoai.tenTL, self.str_ngayKhoiChieu,
                                       self.tenPhim, self.soTapPhim)


n, m = map(int, input().split())

genres = {}
for i in range(n):
    tenTl = input()
    genre_object = Film_Genre(i+1, tenTl)
    genres[genre_object.maTL] = genre_object

films = []
for i in range(m):
    maTL2 = input()
    ngayKhoiChieu = input()
    tenPhim = input()
    soTapPhim = int(input())

    films.append(Film(i+1, tenPhim, ngayKhoiChieu, soTapPhim, genres[maTL2]))

# sắp xếp theo thứ tự ưu tiên ngày khởi chiếu tăng dần,
# tên phim sắp xếp theo thứ tự từ điển, số tập phim giảm dần.
films.sort(key=lambda x: (x.ngayKhoiChieu, x.tenPhim, -x.soTapPhim))

for i in films:
    print(i.getIn4())

