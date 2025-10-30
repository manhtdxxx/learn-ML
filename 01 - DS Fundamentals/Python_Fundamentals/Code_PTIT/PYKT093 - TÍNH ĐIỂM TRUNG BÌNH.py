import math
class Student:
    def __init__(self, id, name, average_score):
        self.id = 'SV{:02d}'.format(id)
        self.name = self.nomalized_name(name)
        self.average_score = average_score
        self.rank = 0

    def nomalized_name(self, name):
        name_split = name.strip().split()
        name_join = ' '.join(name_split).title()
        return name_join

    def show(self):
        return '{} {} {:.2f} {}'.format(self.id, self.name, self.average_score, self.rank)


student_list = []
n_students = int(input())
for i in range(n_students):
    name = input()
    score_1 = int(input())
    score_2 = int(input())
    score_3 = int(input())

    average_score = (score_1*3 + score_2*3 + score_3*2) / 8
    average_score = math.ceil(average_score*100) / 100
    # VD khi dùng round: 4.125 sẽ làm tròn thành 4.12, ceil sẽ làm tròn lên 4.13
    student_list.append(Student(i+1, name, average_score))

# sap xep theo av_score, neu av_score bang nhau thi xep theo id
student_list.sort(key=lambda a: (- a.average_score, a.id))

# rank
student_list[0].rank = 1
for i in range(1, len(student_list)):
    if student_list[i].average_score == student_list[i - 1].average_score:
        student_list[i].rank = student_list[i - 1].rank
    elif student_list[i].average_score < student_list[i - 1].average_score:
        student_list[i].rank = i + 1

# print
for i in student_list:
    print(i.show())


