# 1-The program takes a command line argument, this argument is the name of a text file.
# the program reads all the text and split them and calulate the 20 most used workds in the
# file
# and then write them to a file called popular_words.t xt
import sys
from collections import Counter
import re
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py mockingjay.txt")
        return
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)  # extract words only
            counter = Counter(words)
            most_common = counter.most_common(20)

        with open("popular_words.txt", 'w', encoding='utf-8') as out_file:
            for word, count in most_common:
                out_file.write(f"{word}: {count}\n")
        print("Top 20 words written to popular_words.txt")
    except FileNotFoundError:
        print(f"File {filename} not found.")
if __name__ == "__main__":
    main()

# 2-Given two points represented as x1, y1, x2, y2, r the (float)return (float) distance
# between
# them considering the following distance equation.
import math
def equation(x1, y1, x2, y2):
    x_side = (math.pow(x2- x1 ,2))
    y_side = (math.pow(y2- y1 ,2))
    d = math.sqrt(x_side + y_side)
    print (d)
equation(1, 2, 4, 6)

# 3-Create a Vehicle class without any variables and methods
class Vehicle:
    pass

# 4-Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
# 5-Write a Python program to reverse a string word by word.
def reverse_string(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_words = ' '.join(reversed_words)
    return reversed_words
print(reverse_string("Hello, it's me Mario!"))

# 6-Write a Python class which has two methods get_String and print_String. get_String
# accept a string from the user and print_String print the string in upper case
class StringManipulator:
    def __init__(self):
        self.user_string = ""
    def get_string(self):
        self.user_string = input("Enter a string: ")
    def print_string(self):
        print(self.user_string.upper())
s= StringManipulator()
s.get_string()
s.print_string()

# 7-Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(5)
print("Area:", circle.area())