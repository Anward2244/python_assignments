# 1. Check if numbers in a list have duplicate digits
def has_duplicate_digits(lst):
    result = []
    for num in lst:
        n = num   # handle negatives
        seen = set()
        duplicate = False
        while n > 0:
            digit = n % 10
            if digit in seen:
                duplicate = True
                break
            seen.add(digit)
            n //= 10
        result.append(duplicate)
    return result


# 2. Sum of all numbers in a matrix
def sum_of_matrix(matrix):
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total



# Problem 1
numbers = [202, 89, 112, 88]
print("# Duplicate Digits Check")
print("Input:", numbers)
print("Output:", has_duplicate_digits(numbers))

# Problem 2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\n# Sum of Matrix")
print("Matrix:", matrix)
print("Sum:", sum_of_matrix(matrix))
