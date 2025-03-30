n_cases = int(input())


def gauss_elimination(matrix_A, matrix_B):
    n = len(matrix_A)  # = len(matrix_B)

    # TAO MA TRAN MO RONG A|B
    matrix_AB = []
    for row in range(n):
        ab = matrix_A[row] + [matrix_B[row]]
        # A la list chua list, B cung phai thanh list chua list
        matrix_AB.append(ab)

    # SAP XEP ROW
    for row in range(n):
        column = row

        max_val_of_column = abs(matrix_AB[row][column])
        row_contains_max_val = row
        for next_row in range(row+1, n):
            if abs(matrix_AB[next_row][column]) > max_val_of_column:
                max_val_of_column = abs(matrix_AB[next_row][column])
                row_contains_max_val = next_row

        matrix_AB[row], matrix_AB[row_contains_max_val] = matrix_AB[row_contains_max_val], matrix_AB[row]

    # TIEN HANH KHU GAUSS
    for row in range(n):
        column = row
        for next_row in range(row+1, n):
            factor = - (matrix_AB[next_row][column] / matrix_AB[row][column])
            matrix_AB[next_row][column] = matrix_AB[row][column] * factor + matrix_AB[next_row][column]



while n_cases > 0:
    n = int(input())  # n_rows
    A_matrix = []
    for _ in range(n):
        a = list(map(int, input().split()))
        A_matrix.append(a)

    B_matrix = list(map(int, input().split()))

    n_cases -= 1
