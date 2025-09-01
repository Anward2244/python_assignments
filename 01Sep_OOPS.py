class Calculator:
    def add(self, a, b):
        print(a + b)
    def sub(self, a, b):
        print(a - b)
    def mul(self, a, b):
        print(a * b)
    def div(self, a, b):
        print('cannot divisible with zero') if (b == 0) else print(a / b)
    def floor(self, a, b):
        print('cannot divisible with denomiator as zero') if (b == 0) else print(a // b)
    def rem(self, a, b):
        print('cannot divisible with denominator as zero') if (b == 0) else print(a % b)
    
    def details1(self):
        print("model number: ", calc.model_num, "\nmade in: ", calc.made_in)
    def details2(self):
        print("color: ",det.color, "\ndiscount: ", det.discount)

calc = Calculator()
det = Calculator()

calc.model_num = "X123"
calc.made_in = "India"
det.color = "Red"
det.discount = "10%"

calc.add(10, 65)
calc.sub(82, 63)
calc.mul(2, 6)
calc.div(85, 15)
calc.floor(75, 63)
calc.rem(23,3)

calc.details1()
det.details2()

# self represents the current instance (object) of the class.
# It is used to access variables and methods inside the class.
# When you call a method using an object, Python automatically passes that object as the first argument to the method, and by convention we call it self.