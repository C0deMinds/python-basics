"""
Exercise 3: (Challenge) Write a program that generates the multiplication table (up to 10) using a for loop.

If this is making you confused, don't hesitate to message us for a further explanation.
"""

print("Multiplication Table")

for x in range(1, 11):
    for y in range(1, 11):
        print(x * y, end=" ")  # end=" " tells print that instead of going to a new line, end the print statement with a space
    print("")  # This line is so once the line is finished, a new line can start
