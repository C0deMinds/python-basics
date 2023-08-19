"""
Exercise 1: Write a program that prints all the numbers from 1 to 10 using a while loop.
Now do it using a for loop. Which one do you think is more efficient for this task?
"""

counter = 1
while counter <= 10:
    print(counter)
    counter += 1

for num in range(1, 11):
    print(num)

# For loop are much more efficient than while loops when looping through a sequence (lists, strings, etc)
