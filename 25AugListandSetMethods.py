# List Methods_______________________________________________________________________

# append()
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert()
fruits = ["apple", "banana"]
fruits.insert(1, "grape")
print(fruits)  # ['apple', 'grape', 'banana']

# extend()
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]

# remove()
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']

# pop()
fruits = ["apple", "banana", "cherry"]
print(fruits.pop())  # cherry
print(fruits)        # ['apple', 'banana']

# clear()
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # []

# index()
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1

# count()
list1 = [1, 2, 2, 3, 2]
print(list1.count(2))  # 3

# sort()
list2 = [4, 1, 7, 3]
list2.sort()
print(list2)  # [1, 3, 4, 7]

# reverse()
list3 = [1, 2, 3]
list3.reverse()
print(list3)  # [3, 2, 1]

# shallow copy

import copy
a = [[1, 2], [3, 4]]
b = a   # OR b = a.copy()
b[0][0] = 99
print(a)  # [[99, 2], [3, 4]]
print(b)  # [[99, 2], [3, 4]]

# deep copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99
print(a)  # [[1, 2], [3, 4]]
print(b)  # [[99, 2], [3, 4]]


# Set Methods________________________________________________________________


# add()
nums = {1, 2, 3}
nums.add(4)
print(nums)  # {1, 2, 3, 4}

# remove()
nums = {1, 2, 3}
nums.remove(2)
print(nums)  # {1, 3}

# discard()
nums = {1, 2, 3}
nums.discard(5)  # no error
print(nums)  # {1, 2, 3}

#pop()
nums = {1, 2, 3}
print(nums.pop())  # could be 1/2/3 (random)

# clear()
nums = {1, 2, 3}
nums.clear()
print(nums)  # set()

# union()
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# intersection()
a = {1, 2}
b = {2, 3}
print(a.intersection(b))  # {2}

# difference()
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))  # {1, 3}

# symmetric_difference()
a = {1, 2, 3}
b = {2, 4}
print(a.symmetric_difference(b))  # {1, 3, 4}

# issubset() / issuperset()
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True
print(b.issuperset(a)) # True

# isdisjoint()
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True
