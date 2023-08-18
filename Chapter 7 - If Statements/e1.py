"""
Exercise 1: Write a program that takes a user's age as input and categorizes them into different groups:
 - If the age is less than 13, print "Child."
 - If the age is between 13 and 19 (inclusive), print "Teenager."
 - If the age is 20 or older, print "Adult."
"""

print("Age Categorizer")

age = int(input("What is your age: "))

if age < 13:
    print("Child")
elif age <= 19:  # Since it is inclusive, we used <= instead of <
    print("Teenager")
else:
    print("Adult")
