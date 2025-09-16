
# sorting a list in descending order
list1 = [51, 8, 57, 12, 210, 125]
flag = False

for j in range(0, len(list1)):
    for i in range(0, len(list1) - 1 - j):
        if list1[i] < list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            flag = True

    if flag == False:
        break
print(list1)          # [210, 125, 57, 51, 12, 8]



# sorting strings inside a list based on their lengths
list2 = ['anwar', 'shashavali', 'hussain', 'vishnu', 'dhanush']
flag = False

for j in range(0, len(list2)):
    for i in range(0, len(list2) - 1 - j):
        if len(list2[i]) > len(list2[i + 1]):
            list2[i], list2[i + 1] = list2[i + 1], list2[i]
            flag = True

    if flag == False:
        break
print(list2)           # ['anwar', 'vishnu', 'hussain', 'dhanush', 'shashavali']



# sorting strings inside a list
list2 = ['anwar', 'shashavali', 'hussain', 'vishnu', 'dhanush']
flag = False

for j in range(0, len(list2)):
    for i in range(0, len(list2) - 1 - j):
        if ord(list2[i][0]) > ord(list2[i + 1][0]):
            list2[i], list2[i + 1] = list2[i + 1], list2[i]
            flag = True

    if flag == False:
        break
print(list2)             # ['anwar', 'dhanush', 'hussain', 'shashavali', 'vishnu']



# sorting nested lists based on the first element in each nested list
list3 = [[12, 75], [8, 636], [75, 65, 68], [5, 65, 35]]
flag = False

for j in range(0, len(list3)):
    for i in range(0, len(list3) - 1 - j):
        if list3[i][0] > list3[i + 1][0]:
            list3[i], list3[i + 1] = list3[i + 1], list3[i]
            flag = True

    if flag == False:
        break
print(list3)             # [[5, 65, 35], [8, 636], [12, 75], [75, 65, 68]]