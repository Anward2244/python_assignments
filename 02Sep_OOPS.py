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


car1 = Car(1002, 'Black', 20000000)
car2 = Car(1004, 'Red', 35000000)

# Accessing instance variables with Object name
print('ID of',car1.color,'color car is',car1.id)
print('Cost of',car2.color,'color car is',car2.cost)

# Accessing class/static variables with Object name 
print(car1.company_name)

# Accessing class/static variables with Class name 
print(Car.company_name,'is the comapany name of all cars')

# Accessing instance variables with class name
# print(Car.id) # error: type object 'Car' has no attribute 'id'


car1.details() # instance method with object
car2.other_company("Maruthi") # class method with object
car1.other_details() # Static method with object


# Car.details() # instance method with class gives error
Car.other_company('Audi')
Car.other_details()
