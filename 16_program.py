# Python Programs to check if a number is a Perfect Square

# 1. How to check if Number is Perfect Square in Python

import math

def is_perfect_sq(num):
    if num < 0:
        return False    # Negative numbers cannot be perfect squares
    sqrt_num = math.sqrt(num)
    return sqrt_num.is_integer() # Check if the square root is an integer

# Check if it's a perfect square
print(is_perfect_sq(15))
print(is_perfect_sq(36))

# 2. Using math.isqrt function

import math

# Function to check if a number is a perfect square
def is_perfect_square(num):
    if num < 0:
        return False # Negative numbers cannot be perfect squares
    sqrt_num = math.isqrt(num) # Get the integer square root
    is_perfect_sq = sqrt_num * sqrt_num == num # Verify if the square matches the number
    return is_perfect_sq

# Test cases
print(is_perfect_square(16))
print(is_perfect_square(20))

