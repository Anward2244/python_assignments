# 1. Check if the given matrix is an identity matrix------------------------------------------
matrix1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

is_identity = True
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        if (i == j and matrix1[i][j] != 1) or (i != j and matrix1[i][j] != 0):
            is_identity = False
            break
print("1. Identity Matrix:", is_identity)


# 2. Add 2 matrices-----------------------------------------------------------------
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_add = []
for i in range(len(m1)):
    row = []
    for j in range(len(m1)):
        row.append(m1[i][j] + m2[i][j])
    result_add.append(row)
print("\n2. Matrix Addition:", result_add)


# 3. Sum of diagonal elements---------------------------------------------
sum_diag = 0
for i in range(len(m1)):
    sum_diag += m1[i][i]
print("\n3. Sum of Diagonal Elements:", sum_diag)


# 4. Matrix Multiplication------------------------------------------------
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_mul = []
for i in range(len(a)):
    row = []
    for j in range(len(b)):
        s = 0
        for k in range(len(b)):
            s += a[i][k] * b[k][j]
        row.append(s)
    result_mul.append(row)
print("\n4. Matrix Multiplication:", result_mul)
