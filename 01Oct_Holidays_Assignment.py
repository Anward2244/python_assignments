#------------------------ Easy ---------------------------

# 1. check if a number is even or odd
num1 = int(input('enter the number: '))
if num1 == 0:
    print('zero')
elif num1 % 2 == 0:
    print(num1, 'is even')
else:
    print(num1, 'is odd')


# 2. finding max and min element in list
list2 = [54, 5, 78, 21, 478]
print('min element: ', min(list2))
print('max element: ', max(list2))


# 3. reversing a string without slicing
str3 = 'Reverse'
new_str = ''
for i in str3:
    new_str = i + new_str
print(new_str)


# 4. check if a string is palindrome or not
str4 = input('enter a word: ')
if len(str4) == 1:
    print('invalid')
elif str4 == str[::-1]:
    print('palindrome')
else:
    print('not a palindrome')


# 5. factorial of a number
num5 = int(input('enter a number: '))
fact = 1
for i in range(1, num5 + 1):
    fact = fact * i
print('factorial of', num5, 'is', fact)


# 6. count the frequency of each character in a string
str6 = 'agjergnergj'
for i in str6:
    print(i, str6.count(i))


# 7. print second largest number in a list
list7 = [54, 5, 78, 21, 478]
list7.sort()
print(list7[-2])


# 8. find how many vowels and consonants in a string
str8 = 'Mahavatar Narasimha'
vowels_count = 0
cons_count = 0
for i in str8:
    if i in 'AEIOUaeiou':
        vowels_count +=1
    elif  i not in 'AEIOUaeiou' and (('a'<= i <='z') or ('A'<= i <='Z')):
        cons_count += 1
print('vowels = ', vowels_count)
print('consonants = ', cons_count)


# 9. sum of digits of a number
num9 = int(input('enter a number: '))
sum = 0
while num9 > 0:
    digit = num9 % 10
    sum += digit
    num9 = num9 // 10
print(sum)


# 10. multiplication table
num10 = 16
for i in  range(1, 11):
    print(num10, 'X', i, '=', num10*i)


# 11. Find the longest word in a sentence
def longest_word(sentence):
    longest = None
    words = sentence.split()
    for i in words:
        for j in words:
            if i > j:
                longest = i
    return longest

print(longest_word("Python is amazing language"))


# 12. removing duplicates from list
list12 = [54, 5, 78, 21, 478, 54, 75, 21]
print(list(set(list12)))


# 13. sorting list
list1 = [51, 8, 57, 12, 210, 125]
flag = False
for j in range(0, len(list1)):
    for i in range(0, len(list1) - 1 - j):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            flag = True
    if flag == False:
        break
print(list1)


# 14. merge two lists into a single sorted list
a = [54, 5, 78, 21, 478]
b = [51, 8, 57, 12, 210, 125]
a.extend(b)
a.sort()
print(a)


# 15. check if a number is prime or not
def check_prime(num):
    if num <= 1:
        return 'not a prime number'
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 'not a prime number'

    return 'prime number'

print(check_prime(num))


#-------------------------- Medium -----------------------------------------

# 1. Find all pairs in a list that sum up to a target value
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

nums = [2, 4, 3, 7, 5, -1]
print("Pairs with sum 6:", find_pairs(nums, 6))


# 2. Rotate a list by k positions
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

lst = [1, 2, 3, 4, 5]
k = 2
print("2 positions:", rotate_list(lst, k))


# 3. Find the missing number in a list of consecutive integers
def find_missing(lst):
    missing = []
    for i in range(1, max(lst) + 1):
        if i not in lst:
            missing.append(i)
    return missing

lst = [1, 2, 3, 5, 6, 8]
print("Missing number:", find_missing(lst))


# 4. Check if two strings are anagrams
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(anagram("listen", "silent"))


# 5. Count the number of words in a sentence
def count_words(sentence):
    return len(sentence.split())

print(count_words("Python is fun to learn"))


# 6. Remove all duplicate words from a sentence
def remove_duplicate_words(sentence):
    words = sentence.split()
    result = []
    for w in words:
        if w not in result:
            result.append(w)
    return " ".join(result)

print(remove_duplicate_words("this is is a test test"))


# 7. Invert a dictionary (keys become values)
def invert_dict(d):
    return {v: k for k, v in d.items()}

d = {"a": 1, "b": 2, "c": 3}
print(invert_dict(d))


# 8. Find the intersection of two lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(intersection([1,2,3,4], [3,4,5,6]))


# 9. Print the transpose of a matrix
def transpose(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i < j:
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))


# 10. Implement bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# 11. Find the first non-repeating character in a string
def first_non_repeating(s):
    for i in s:
        for j in s:
            if i != j:
                return j
    return None

print(first_non_repeating("swiss"))


# 12. Find the longest word in a sentence
def longest_word(sentence):
    longest = None
    words = sentence.split()
    for i in words:
        for j in words:
            if i > j:
                longest = i
    return longest

print(longest_word("Python is amazing language"))


# 13. Find the second smallest number in a list
def second_smallest(lst):
    unique = sorted(set(lst))
    return unique[1]

print(second_smallest([4,1,7,3,1,5]))


# 14. Check if a number is an Armstrong number
def is_armstrong(num):
    num2 = num
    sum1 = 0
    power = len(str(num2))
    while num2 > 0:
        digit = num2 % 10
        sum1 = sum1 + (digit**power)
        num2 = num2 // 10

    if sum1 == num:
        return 'Armstrong Number'
    else:
        return 'Not Armstrong Number'

print(is_armstrong(153))
print(is_armstrong(564))
