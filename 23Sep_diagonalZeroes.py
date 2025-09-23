list1 = [[43, 82, 75, 85],
         [45, 74, 21, 63],
         [65, 15, 54, 18],
         [15, 54, 6, 57]]

for i in range(len(list1)):
    for j in range(len(list1)):
        if (i == j) or (i + j == len(list1) - 1):
            list1[i][j] = 0

print(list1)