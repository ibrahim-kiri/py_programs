# Python Programs to Find Perfect Number

# 1. How to Find a Perfect Number in Python

def is_perfect_square(num):
    divisors_sum = 0

    # Loop through all numbers from 1 to num - 1
    for i in range(1, num):
        if num % i == 0: # Check if 'i' is a divisor of 'num'
            divisors_sum += i # Add the divisors to the sum

    # Check if the sum of divisors equals the number
    return divisors_sum == num

number = 6
print(is_perfect_square(number))
number = 15
print(is_perfect_square(number))

# 2. Using math.sqrt function

import math

#  Input number to check
num = 28

# Initialize the sum of divisors
divisors_sum = 1 # Start with 1, as it is a divisor of every number

# Check divisors up to the square root of the number
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0: #  Check if 'i' is a divisor of 'num'
        divisors_sum += i
        if i != num // i: # Avoid adding the square root twice
            divisors_sum += num // i

# Check if the sum of divisors equals the number    
is_perfect = divisors_sum == num
print(f"Is {num} a perfect number? -> {is_perfect}")


# 3. Using List Comprehension

# Input number to  check
num = 28

# Calculate the sum of divisors using list comprehension
is_perfect = num == sum([i for i in range(1, num) if num % i == 0])
print(f"Is {num} a perfect number? -> {is_perfect}")

