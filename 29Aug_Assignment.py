# checking the given number is palindrome or not

num1 = int(input('enter the number: '))
temp = num1
reverse_num = 0

while num1 > 0:
    digit = num1 % 10
    reverse_num = reverse_num * 10 + digit
    num1 = num1 // 10
print(reverse_num)

if reverse_num == temp:
    print('palindrome')
else:
    print('not palindrome')



#print even digits in a number

num1 = int(input('enter the number: '))
sum = 0
while num1 > 0:
    digit = num1 % 10
    if digit % 2 == 0:
        print(digit)
    num1 = num1 // 10



# print prime digits in a number

num2 = int(input('enter the number: '))
list1 = [2, 3, 5, 7]
while num2 > 0:
    digit = num2 % 10
    if digit in list1:
        print(digit)
    num2 = num2 // 10



# checking the given number is perfect number or not
num3 = int(input('enter the number:'))
sum = 0
for i in range(1, num3):
    if num3 % i == 0:
        sum +=i

if sum == num3:
    print('perfect number')
else:
    print('not a perfect number')
