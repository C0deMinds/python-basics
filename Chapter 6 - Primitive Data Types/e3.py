"""
Exercise 3: Create a program that calculates the area of a 
rectangle with user-provided length and width as integers.
"""

print("Rectangle Area Calculator")

length = int(input("What is the length of the rectangle: ")) #using int() automatically converts it from string to integer
width = int(input("What is the width of the rectangle: "))

print(f"The area of the rectangle is {length * width}.") # f-string
