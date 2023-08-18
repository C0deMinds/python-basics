"""
Exercise 3: Write a program that gives advice based on the weather temperature:
 - If the temperature is above 30 degrees Celsius, advise wearing light   clothing.
 - If the temperature is between 20 and 30 degrees Celsius, suggest wearing a light jacket.
 - If the temperature is below 20 degrees Celsius, recommend wearing a warm coat.
 - If it's raining (use a variable is_raining), remind the user to carry an umbrella.
"""

print("Weather Advice")

is_raining = False
temp = float(input("How many degrees Celsius is it: "))  # Converted it to float since it's a temperature

if temp > 30.0:
    print("Wear some light clothing outside.")
elif temp > 20.0:
    print("Wear a light jacket outside.")
else:
    print("Wear a warm coat outside.")

if is_raining:  # We used a seperate if statement because is_raining and temp are unrelated
    print("Remember to carry an umbrella.")
