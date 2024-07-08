# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  colors = ['red', 'blue', 'green']
  for element in colors:
      print(element)

# Call the function and print each element
example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students = ['Alice', 'Bill', 'Chuck']
    first_student = students[0]
    last_student = students[2]
    return(f"first student is {first_student} and last student is {last_student}")

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # your code here
    foods = ("apple", "banana", "chocolate")
    meal = []
    for item in foods:
        meal.append(item)
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only tuple the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    foods = ("apple", "banana", "chocolate")
    last_two_foods = foods[-2:]
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # your code here
    home_town = {
        "city" : "Moscow",
        "state" : "Idaho",
        "population" : 20000
    }
    return (f"I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}")

# Call the function and print the result
print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # your code here
        home_town = {
        "city" : "Moscow",
        "state" : "Idaho",
        "population" : 20000
        }
        home_town_items = []
        for item in home_town:
            # home_town_items.append(f"{item} = {home_town_items["item"]}")
            home_town_items.append(f"{item} = {home_town[item]}")
        return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())

# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.
def calculate_area_triangle(base, height): 
    area = base * height / 2
    return area


print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.
def apply_discount(price, discount):
    new_price = price - (price*discount/100)
    return new_price

print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(temp, unit):
    if unit == "C":
        new_temp = (temp * 9/5) + 32
    elif unit == "F":
        new_temp = (temp - 32) * 5/9
    return new_temp

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(100, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.
def sum_to(n):
    running_sum = 0
    for counter in range(1,n):
        running_sum = counter + running_sum
    return running_sum + n

print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print('Exercise 6:', largest(3, 3, 2))

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.
def calculate_tip(bill, tip):
    return bill * tip / 100

print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.

def product(*num):
    running_prod = 1
    for counter in num:
        running_prod = counter * running_prod
    return running_prod

print('Exercise 8:', product(4))

def basicCalculator(a,b,operation):
    match operation:
        case "a":
            return a+b
        case "s":
            return a-b
        case "m":
            return a * b
        case "d":
            return a / b

print(basicCalculator(10,5,'a'))
print(basicCalculator(10,5,'s'))
print(basicCalculator(10,5,'m'))
print(basicCalculator(10,5,'d'))

print('Exercise 9 Result:', basicCalculator(10, 5, 's'))

