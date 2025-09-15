# 1. reversing a string

# method 1
name1 = "Anwar Dudekula"
print(name1[::-1])

# method 2
name1 = "Anwar Dudekula"
new_name = ''
for i in name1:
    new_name = i + new_name
print(new_name)

# method 3
name1 = "Anwar Dudekula"
new_name = ''
for i in range(len(name1) - 1, -1, -1):
    new_name = new_name + name1[i]
print(new_name)
# ________________________________________________________________________

# 2. Sum of digits of each number in the given list
def sum_of_digits_list(list1):
    result = []
    for i in list1:
        s = 0
        while i > 0:
            s += i % 10
            i //= 10
        result.append(s)
    return result
# ___________________________________________________________________________

# 3. Find max digit in a given number
def max_digit_number(num1):
    max_d = 0
    while num1 > 0:
        digit = num1 % 10
        if digit > max_d:
            max_d = digit
        num1 //= 10
    return max_d
# ___________________________________________________________________________

# 4. Find max digit for every number in a given list
def max_digit_list(list1):
    result = []
    for i in list1:
        max_d = 0
        while i > 0:
            digit = i % 10
            if digit > max_d:
                max_d = digit
            i //= 10
        result.append(max_d)
    return result



list1 = [15, 863, 578, 75, 63]

print("Sum of digits for each number in list", sum_of_digits_list(list1))

num1 = int(input("Enter a number: "))
print("Max digit in given number:", max_digit_number(num1))

print("Max digit for every number in list: ", max_digit_list(list1))
