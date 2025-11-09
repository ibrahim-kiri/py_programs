# Python Programs to Find Factorial of a Number

# 1. Find Factorial of a Number in Python using for Loop

n = 5
if n < 0:
    print("Factorial not defined for negative numbers")

factorial = 1
for i in range(1, n + 1):
    factorial *= i  # Multiply factorial by loop counter

print(f"Factorial of {n} is : {factorial}")

# 2. Using Recursion

def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))

# 3. Using Python’s Built-in math.factorial Function

import math

n = 5
if n < 0:
    print("Factorial not defined for negative numbers")
factorial = math.factorial(n)
print(f"Factorial of {n} is {factorial}")


# 4. Using reduce from functools

from functools import reduce

n = 5
if n < 0:
    print("Factorial not defined for negative numbers")

factorial = reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(f"Factorial of {n} is {factorial}")


