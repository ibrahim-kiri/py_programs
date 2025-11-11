# Python Programs to Find Quotient and Remainder

# 1. Using Quotient Divison (//) and Modulo (%) operators

numerator = 13
denominator = 5

# Calculate quotient
quotient = numerator // denominator

# Calculate remainder
remainder = numerator % denominator

print("Quotient:", quotient)
print("Remainder:", remainder)

# 2. Using divmod() function

# Define two numbers
numerator = 13
denominator = 5

quotient, remainder = divmod(numerator, denominator)

# Output results
print("Quotient:", quotient)
print("Remainder:", remainder)

# 3. Using mathematical formula

import math

# Define two numbers
numerator = 13
denominator = 5

# Quotient using floor
quotient = math.floor(numerator / denominator)

# Remainder using formula
remainder = numerator - (quotient * denominator)

print("Quotient:", quotient)
print("Remainder:", remainder)
