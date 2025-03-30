n_cases = int(input())

while n_cases > 0:
    # n : tổng số người chuyển đến
    # c : sức chứa khu đô thị 1
    # d : sức chứa khu đô thị 2
    # A[i] : mức độ giàu có của người thứ i
    n, c, d = list(map(int, input().split()))
    A = list(map(int, input().split()))

    c, d = sorted([c, d])  # để chia list cho dễ
    sorted_A = sorted(A, reverse=True)  # sắp xếp giảm dần để loại bỏ những người có A thấp

    # nhung nguoi co A cao hon se duoc xep vao khu do thi nho hon
    s1 = 0
    for i in sorted_A[:c]:
        s1 += i
    m1 = s1 / c

    # nhung nguoi co A thap hon se duoc xep vao khu do thi lon hon
    s2 = 0
    for j in sorted_A[c:c+d]:
        s2 += j
    m2 = s2 / d

    #
    m = m1 + m2
    print('{:.6f}'.format(m))

    n_cases -= 1
