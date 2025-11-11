# numbers between a range generator
def range_num(start, end):
    curr = start
    while curr <= end:
        temp = curr
        curr += 1
        yield temp

no1 = range_num(2,5)
print(next(no1)) # 2
print(next(no1)) # 3
print(next(no1)) # 4
print(next(no1)) # 5
print(next(no1)) # StopIteration



# infinite fibonacci series using generators
def fibo():
    a1 = 0
    a2 = 1
    while True:
        yield a1
        a1, a2 = a2, a1 + a2
num1 = fibo()
print(next(num1))  # 0
print(next(num1))  # 1
print(next(num1))  # 1
print(next(num1))  # 2
print(next(num1))  # 3
print(next(num1))  # 5
print(next(num1))  # 8
print(next(num1))  # 13



