"""
Exercise 2: Using a for loop, loop through numbers 1 through 100, and print the numbers. 
However, if the number is even don't print the number.
"""

for num in range(1, 101):
    if num % 2 != 0:  # Checks if the number divided by 2 gives a remainder that isn't 0 (If it isn't 0, it's odd ex: 5 / 2 --> Remainder 1)
        print(num)
