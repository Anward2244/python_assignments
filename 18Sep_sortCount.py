# sorting a list
list1 = [51, 8, 57, 12, 210, 125]
flag = False
count = 0
for j in range(0, len(list1)):
    for i in range(0, len(list1) - 1 - j):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            flag = True
            count +=1
    if flag == False:
        break
print(list1)                                # [8, 12, 51, 57, 125, 210]
print('number of swaps: ', count)           # number of swaps:  4
# time complexity = o(n square)
# space complexity = o(1)






# binary search
def binary_search(list1):
		list1.sort()
					
		low = 0
		high = (len(list1)//2) - 1
		select_element = 12
		while low <= high:
						mid = (low + high)//2
						if list1[mid] == select_element:
							return mid
						elif list1[mid] < select_element:
							low = mid+1
						else:
							high = mid-1
		return -1


list1 = [51, 8, 57, 12, 210, 125]

print(binary_search(list1))
# time complexity = o(n logn)
# space complexity = o(n)