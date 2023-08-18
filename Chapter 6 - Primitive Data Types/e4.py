"""
Exercise 4: Ask the user for the temperature in Celsius and convert 
it to Fahrenheit using floats for accuracy.
"""

print("Temperature Converter")

cels_temp = float(input("What is the temperature in Celcius: "))  # float() automatically converts the string to a float
fahr_temp = (cels_temp * (9 / 5)) + 32.0  # You can use brackets/parentheses to make it more clear / for bedmas
print(f"The temperature in fahrenheit is {fahr_temp}°F") # You don't need to convert fahr_temp back to a string with f-strings
