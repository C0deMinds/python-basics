"""
Exercise 5: Ask the user for three float numbers and calculate their average.
"""

print("Average Calculator")

n1 = float(input("Give me the first float number: "))  # float() is used to automatically convert from string to float
n2 = float(input("Give me the second float number: "))
n3 = float(input("Give me the third float number: "))
average = (n1 + n2 + n3) / 3

print(f"The average of these three numbers is {average}.")
