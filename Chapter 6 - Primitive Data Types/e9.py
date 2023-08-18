"""
Exercise 9: Ask the user to input a sentence. 
Print the sentence in reverse order using string slicing and negative indexes

Line 12 Explanation:
There is a third parameter you can use when string slicing which dictates how much you increment by, and -1 means backwords. 
For example, string[1:1:2] means that every 2nd character will print. If it's 1, you can leave it empty and just do string[::2]
Try it out yourself!
"""

string = input("Give me a sentence: ")
print(string[::-1])
