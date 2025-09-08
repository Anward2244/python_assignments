# Method Overloading (Compile-time Polymorphism Simulation)
class MathOps:
    def add(self, *num):
        return sum(num)

# Method Overriding (Runtime Polymorphism)
class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):   # overriding parent method
        print("This is Child class method")

# Operator Overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value



# Method Overloading:
# Python doesn’t support true overloading like Java/C++,
# but we achieve it using default arguments or *args.
math_obj = MathOps()
print("Add 2 numbers:", math_obj.add(5, 10))
print("Add 3 numbers:", math_obj.add(5, 10, 20))

# Method Overriding
p = Parent()
c = Child()
p.show()  # calls parent method
c.show()  # calls child overridden method

# Operator Overloading
n1 = Number(50)
n2 = Number(30)
print("Addition using + :", n1 + n2)



