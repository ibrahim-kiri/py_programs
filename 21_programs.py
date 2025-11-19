# Python Find Square Root of a Number

# 1. Using the Exponentiation Operator (**)

num = float(input("Enter a number: "))
sqrt = num ** 0.5
print(f"The square root of {num} is {sqrt}")


# 2. Using math.sqrt() Function

import math

print('square root of 0: ', math.sqrt(0))
print('square root of integer number 64: ', math.sqrt(64))
print('square root of float number 5.6: ', math.sqrt(5.6))


# 3. Using cmath.sqrt() Function for complex numbers

import cmath

print('square root of integer number 64: ', cmath.sqrt(64))
print('square root of float number 5.6: ', cmath.sqrt(5.6))
print('square root of negative number -64: ', cmath.sqrt(-64))
