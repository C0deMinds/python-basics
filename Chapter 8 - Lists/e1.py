"""
Exercise 1: Create an empty list. Allow users to add items into that list. 
Once they are done, print the list out.
"""

my_list = []  # Don't name your list "list" because it will cause problems

element1 = input("Enter what do you want to add to the list: ")
element2 = input("What else do you want to add to the list: ")
element3 = input("What else do you want to add to the list: ")

my_list.append(element1)
my_list.append(element2)
my_list.append(element3)

print(my_list)
