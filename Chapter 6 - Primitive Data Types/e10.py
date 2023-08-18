"""
Exercise 10: Write a program that takes the user's age as input and converts it to an integer. 
Then, calculate and print the year the user will turn 100 years old.
"""

print("Age Calculator")

age = int(input("What is your age: "))  # int() automatically converts age from a string to integer
year = (100 - age) + 2023

print(f"You will turn 100 in {year}.")  # f-string
