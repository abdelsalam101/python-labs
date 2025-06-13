# 1- Define a class attribute”color” with a default value white. I.e., Every Vehicle should be
# white.
class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Car(Vehicle):
    pass
class Bus(Vehicle):
    pass
bmw = Car("BMW", 240, 15000)
print(f"Car Name: {bmw.name}, Max Speed: {bmw.max_speed}, Mileage: {bmw.mileage}, Color: {bmw.color}")
tourBus = Bus("Tour Bus", 120, 50000)
print(f"Bus Name: {tourBus.name}, Max Speed: {tourBus.max_speed}, Mileage: {tourBus.mileage}, Color: {tourBus.color}") 

# 2- Create a Bus child class that inherits from the Vehicle class. The default fare charge of
# any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra
# 10% on full fare as a maintenance charge. So total fare for bus instance will become the
# final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need
# to override the fare() method of a Vehicle class in Bus class.
# Use the following code for your parent Vehicle class. We need to access the parent class
# from inside a method of a child class.
class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge
School_bus = Bus("School Bus", 200, 12, 50)
print("Total Bus fare is:", School_bus.fare())

# 3- Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))  #TRUE

# 4-Define a class named Rectangle which can be constructed by a length and width. The
# Rectangle class has a method which can compute the area.
# Hints:
# Use def methodName(self) to define a method.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rec=Rectangle(5, 10)
print(rec.area())    

# 5- Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
class StrManipulate:
    def __init__(self):
        self.user_string = ""
    def get_string(self):
        self.user_string = input("Enter a string: ")
    def print_string(self):
        print(self.user_string.upper())
s = StrManipulate()
s.get_string()
s.print_string()

# 6-Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class.
class Person:
    def getGender(self):
        return "Not defined"   
class Male(Person):
    def getGender(self):
        return "Male" 
class Female(Person):
    def getGender(self):
        return "Female"
M=Male()
F=Female()
print(M.getGender())
print(F.getGender())

# 7- Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
# but "[)", "({[)]" and "{{{" are invalid
class Validation:
    def is_valid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                continue
        return not stack 
p= Validation()
print(p.is_valid("({[]})"))
