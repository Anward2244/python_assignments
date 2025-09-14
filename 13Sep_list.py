# -------------------------------------------------------------------------------------------------
# Find element at given index in a list
def get_element_by_index(lst, idx):
    if idx < -len(lst) or idx > len(lst) - 1:
        return 'Invalid index'
    return lst[idx]

numbers1 = [1, 2, 34, 52, 68, 7, 4]
pos = int(input('Enter index position: '))
print(get_element_by_index(numbers1, pos))


# -------------------------------------------------------------------------------------------------
# Find sum, max, min using sort()
def list_summary_sort(lst):
    if len(lst) == 0:
        return 'Empty list'

    total = 0
    for num in lst:
        total += num

    lst.sort()
    return f'Sum: {total}, Max: {lst[-1]}, Min: {lst[0]}'

numbers2 = [87, 36, 28, 26, 9, 29, 43, 54]
print(list_summary_sort(numbers2))


# -------------------------------------------------------------------------------------------------
# Find sum, max, min using for loop
def list_summary_loop(lst):
    if lst == []:
        return 'Empty list'

    total = 0
    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
        total += num
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return f'Sum: {total}, Max: {max_val}, Min: {min_val}'

numbers3 = [54, 22, 96, 66, 85, -87, 45, 56]
print(list_summary_loop(numbers3))
