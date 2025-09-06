# types of variables => instance variables, class/static variables
# types of methods => instance, class, static

class Car:
    company_name = "BMW"

    def __init__(self, id, color, cost):
        self.id = id
        self.color = color
        self.cost = cost
    
    #instance method
    def details(self):
        print(self.id, self.color, self.cost)

    # class method
    @classmethod
    def other_company(cls, company_name2):
        cls.company_name2 = company_name2
        print(cls.company_name2)

    #static method
    @staticmethod
    def other_details():
        print('75 years')
        print('high class cars')

class Super_car(Car):
    def __init__(self, id, color,cost, classes):
        super().__init__(id, color, cost)
        self.classes = classes
        print(self.classes)
        
    # Method Overriding
    def details(self):
        print("Super Car Details:", self.id, self.color, self.cost, self.classes)


# Extra classes for MRO demo
class Electric:
    def show(self):
        print("This is Electric class")

class Hybrid(Super_car, Electric):
    pass
    

car1 = Car(1002, 'Black', 20000000)
car2 = Car(1004, 'Red', 35000000)


# Accessing instance variables with Object name
print('ID of',car1.color,'color car is',car1.id)
print('Cost of',car2.color,'color car is',car2.cost)

# Accessing class/static variables with Object name 
print(car1.company_name)

# Accessing class/static variables with Class name 
print(Car.company_name,'is the comapany name of all cars')


car1.details() # instance method with object
car2.other_company("Maruthi") # class method with object
car1.other_details() # Static method with object

Car.other_company('Audi')
Car.other_details()

#creating an object for child class
s_car1 = Super_car(2004, "lamborghini", 12650000, "S")
s_car1.details()  # overridden method

# MRO Example
h1 = Hybrid(3001, "Blue", 4500000, "Hybrid-S")
h1.details()   # comes from Super_car (first in MRO)
h1.show()      # comes from Electric
print("MRO for Hybrid:", Hybrid.mro()) # MRO for Hybrid: [<class '__main__.Hybrid'>, <class '__main__.Super_car'>, <class '__main__.Car'>, <class '__main__.Electric'>, <class 'object'>]