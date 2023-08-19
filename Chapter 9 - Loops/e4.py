"""
Exercise 4: Build a program that calculates the factorial of a given number using a for loop.
"""

num = 535
factorial = 1

for n in range(1, num + 1):  # Don't name the for loop variable the same as any of your variables as it will mess things up
    factorial *= n  # This is the same thing as: factorial = factorial * num / this line is basically multipying factorial by num and updating factorial with the answer

print(f"The factorial of {num} is {factorial}.")
