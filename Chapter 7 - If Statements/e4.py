"""
Exercise 4: You're building a program that gives discounts for movie tickets based on age and whether it's a weekend or not. The rules are:
 - If the person is under 12 years old or over 65 years old they get a 10% discount.
 - If it's a weekend (Saturday or Sunday), there's a 5% discount for everyone.
 - If none of the above conditions are met, there is no discount.
"""

print("Discount Giver")

weekend = False

age = int(input("How old are you: "))  # int() because it's age

if age < 12 or age > 65:
    print("You get a 10% discount!")
elif weekend:
    print("Everyone gets a 5% discount!")
else:
    print("There is no disount today.")
