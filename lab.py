# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()

def check_letter():
    # Your control flow logic goes here
    letter = input()
    if letter in ['a','e','i','o','u'] or letter in ['A','E','I','O','U']:
        print(f'the letter {letter} is a vowel')
    else:
        print(f'the letter {letter} is a consonant')
# Call the function
# check_letter()

def check_voting_eligibility():
    print("enter age")
    age = int(input())
    if age >= 18:
        print(f"{age} is old enough to vote!")
    elif age > -1:
        print(f"{age} is not old enough to vote! You must wait {18-age} years to vote")
    else:
        print("that is not a valid number")

# check_voting_eligibility()


def calculate_dog_years():
    print("enter dog age")
    age = int(input())
    if age > 2:
        print(f"Age in dog years is {(age - 2) * 7 + 20}")
    elif age >= 0:
        print(f"Age in dog years is {age * 10}")
    else:
        print("not a valid age")

# calculate_dog_years()

def weather_advice():
    # Your control flow logic goes here
    print("is it cold?")
    cold = input()
    print("is it raining?")
    raining = input()
    if cold=="yes" and raining=="yes":
        print("wear waterproof coat")
    if cold=="yes" and raining=="no":
        print("Wear a warm coat")
    if  cold =="no" and raining=="yes":
        print("Carry an umbrella")
    if  cold =="no" and  raining=="no":
        print("Wear light clothing")

# weather_advice()

def determine_season():
    print("enter month as three letters")
    month = input()
    print("enter day")
    day = int(input())
    if (month == "jan" or month == "feb") or (month == "dec" and day >= 21) or (month == "mar" and day < 21):
        print(f"{month} {day} is in Winter")
    if (month == "apr" or month == "may") or (month == "mar" and day >= 21) or (month == "jun" and day < 21):
        print(f"{month} {day} is in Spring")
    if (month == "jul" or month == "aug") or (month == "jun" and day >= 21) or (month == "sep" and day < 21):
        print(f"{month} {day} is in Summer")
    if (month == "oct" or month == "nov") or (month == "sep" and day >= 21) or (month == "dec" and day < 21):
        print(f"{month} {day} is in Autumn")

# Call the function
# determine_season()

def guess_number():
    answer = 42
    for item in range(0,5):
        print(f"you have {5-item} guesses")
        response = int(input())
        if response > answer:
            print("too high")
        elif response < answer:
            print("too low")
        elif response == answer:
            print("correct!")
            break
        if item == 4:
            print("you did not get it five attemts sorry.")
guess_number()