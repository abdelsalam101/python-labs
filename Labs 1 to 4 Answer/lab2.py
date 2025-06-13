# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.
l=[1,2,3,4,5]
r=[]
for i in l:
    r.append(i-1)
print(r)


# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# # (a-front + b-front) + (a-back +b-back)
def combine(a: str, b: str)-> str:
    len_a = len(a)
    len_b = len(b)
    if len_a %2 ==0:
        a_mid = len_a // 2
    else:
        a_mid = (len_a+1) // 2

    if len_b %2 ==0:
        b_mid = len_b // 2
    else:
        b_mid = (len_b+1) // 2
    a_front = a[:a_mid]
    b_front = b[:b_mid]
    a_back = a[a_mid:]
    b_back = b[b_mid:]
    return a_front + b_front + a_back + b_back
print(combine("abced", "xyz"))

# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False
def different(numbers)-> bool:
    return len(set(numbers)) == len(numbers)
print(different([1, 5, 7, 9]))
print(different([2, 4, 5, 5, 7, 9]))


# 4- Given unordered list, sort it using algorithm bubble sort
# # ( read about bubble sort and try to implement it)
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        swapped = False 
        for j in range(0, n - i - 1): 
            if numbers[j] > numbers[j + 1]:  
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# 5- Gusses game
# ● Your game generates a random number and gives only 10 tries for the user to
# guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of
# the random number
# ● If the user type number is out of range(100), display a message that is not allowed
# and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and
# don’t count this as try
# ● In case the user entered a correct number within the 10 tries, display a
# congratulations message and let your application guess another random number
# with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play
# again or not.
import random
def guess_game():
    max_tries = 10
    play_again = True
    while play_again:
        target = random.randint(1, 100)
        tries = 0
        guesses = set()
        print(f"Guess a number between 1 and 100. You have {tries} left.")
        while tries < max_tries:
            try:
                guess = int(input(f"Enter your guess: #{tries + 1}: "))
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if guess < 1 or guess > 100:
                print("Number out of range. Please enter a number between 1 and 100.")
                continue
            if guess in guesses:
                print(f"You already guessed {guess}. Try different number.")
                continue
            guesses.add(guess)
            tries += 1
            if guess == target:
                print(f"Congratulations! You guessed the number {target} in {tries} tries.")
                max_tries -= tries
                if max_tries > 0:
                    print(f"let's play again! You have {max_tries} tries left.")
                    target = random.randint(1, 100)
                    tries = 0
                    guesses = set()
                    continue
                else:
                    print("You have no tries left. Game over!")
                    break
            elif guess < target:
                print(f"Too low! {max_tries - tries} tries left.")
            else:
                print(f"Too high! {max_tries - tries} tries left.")
        
        if tries >= max_tries and guess != target:
            print(f"Game Over!. The number was {target}.")
        
        res = input("Do you want to play again? (yes/no): ").lower()
        play_again = res == 'yes'
        if play_again:
            print("Starting a new game...")
            max_tries = 10
guess_game()
                
# 6- Make account on Hacker-rank for problem solving
# (bonus)
# And try to solve this problem and send me your submission
# https://www.hackerrank.com/challenges/diagonal-difference/problem

# Submittion Link:
#     https://www.hackerrank.com/challenges/diagonal-difference/submissions/code/434143949