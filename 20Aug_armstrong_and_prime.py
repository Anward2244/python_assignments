# All Armstrong numbers in given range
initial_range = int(input('enter starting range: '))
upto_range = int(input("Enter ending range: "))


for num in range(initial_range, upto_range + 1):
    digits = 0
    power = 0
    temp = num

    while temp > 0: #for getting number of digits in a number
        digits += 1
        temp //= 10

    temp = num

    while temp > 0:
        digit = temp % 10
        power += digit ** digits
        temp //= 10

    if power == num:
        print(num)


# prime numbers in given range

initial_range = int(input('enter starting range: '))
upto_range = int(input("Enter ending range: "))

for num in range(initial_range, upto_range+1):
    s=0
    for i in range(1,num+1):
        if(num%i==0):
            s=s+1
    if(s==2):
        print(num)