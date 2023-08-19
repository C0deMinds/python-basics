"""
Exercise 2: Take user input (only integers) to add to the list. 
Once you have enough elements, calculate and display the average of the numbers.
"""

numbers = []
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

print(f"The average is {sum(numbers) / len(numbers)}.")  # sum is a list method that adds up all the numbers in a list
