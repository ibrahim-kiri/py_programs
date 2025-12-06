# Python Convert Celsius To Fahrenheit and Vice Versa

# 1. How to Convert Celsius To Fahrenheit in Python

c = float(input("Enter temperature in Celsius: "))
# formula to convert Celsius to Fahrenheit
f = (c * 9/5) + 32
print(f"{c}°C is equal to {f:.2f}°F")

# 2. How to Convert Fahrenheit To Celsius in Python
f = float(input("Enter temperature in Fahrenheit: "))
# formula to convert Fahrenheit to Celsius
c = (f - 32) * 5/9
print(f"{f}°F is equal to {c:.2f}°C")
