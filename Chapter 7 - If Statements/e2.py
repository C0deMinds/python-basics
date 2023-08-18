"""
Exercise 2: Create a program for a store that offers discounts based on different conditions:
 - If a customer is a student and the purchase amount is over $50, apply a 10% discount.
 - If the customer is not a student but the purchase amount is over $100, apply a 5% discount.
 - If neither condition is met, provide no discount.
"""

print("Discount Calculator")

# Play around with these values to see what prints out
price = 160
student = False

if student and price > 50:
    price = price - (price * 0.1)  # Subtracts the current price from the amount discounted
    print("10% discount applied.")
elif not student and price > 100:
    price = price - (price * 0.05)
    print("5% discount applied.")
else:
    print(f"No Discount applied.")

print(f"Your final price is ${price}.")
