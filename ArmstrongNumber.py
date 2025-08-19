num1 = input('enter the number: ')
power=len(num1)
sum = 0
for i in num1:
    sum = sum + int(i)**power

if sum == int(num1):
    print('Armstrong Number')
else:
    print('Not Armstrong Number')


# ______________OR_______________________

num2=int(input('enter the number: '))
arm_num = num2
sum1 = 0
power = len(str(num2))
while num2 > 0:
    digit = num2 % 10
    sum1 = sum1 + (digit**power)
    num2 = num2 // 10

if sum1 == arm_num:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')


# All Armstrong numbers from 1 to given range

upto_range = int(input("Enter range: "))


for num in range(1, upto_range + 1):
    digits = len(str(num))
    power = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        power += digit ** digits
        temp //= 10

    if powers == num:
        print(num)
