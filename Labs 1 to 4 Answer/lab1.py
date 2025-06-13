# Lab 1 - Python Programming
import math

# Question 1
# Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.
fname = input("Enter first name:")
lname = input("Enter last name:")
print(lname + " " + fname)

# Question 2
# Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
number = input("Enter a number: ")
print(int(number) + int(number + number) + int(number + number + number))

# Question 3
#3- Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
print("a string that you \"don't\" have to escape \nThis\nis a....multi-line\nheredoc ----> exapmle")

# Question 4
#Write a Python program to get the volume of a sphere with radius 6.
#v=(4/3) * PI * r^3
r = input("Enter the radius of the sphere: ")
print(int((4/3) * math.pi * (int(r)**3)))

# Question 5
# Write a Python program that will accept the base and height of a triangle and compute
# the area.
#area of triangle = (base * height) / 2
b = input("Enter the base of the triangle: ")
h = input("Enter the height of the triangle: ")
print(int((int(b) / 2) * int(h)))

# Question 6
# Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1, 10):
    for j in range(1, 6):
        if j <= i and i <= 5:
            print("*", end=" ")
        elif i > 5 and j <= 10 - i:
            print("*", end=" ")
    print()

# Question 7
#Write a Python program that accepts a word from the user and reverse it.
word = input("Enter a word: ")
for i in range(1, len(word)+1):
        print(word[-i], end="")
#-------------OR----------------       
print(word[::-1])

# Question 8
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")

# Question 9
# Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Question 10
# Write a Python program that accepts a string and calculate the number of digits and
# letters.
sentence = input("Enter a sentence: ")
s=0
n=0
for i in sentence:
    if i.isalpha():
        s+=1
    elif i.isdigit():
        n+=1
print("The number of letters in the sentence is:", s)       
print("The number of digits in the sentence is:", n)      
