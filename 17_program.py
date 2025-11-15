# Python Programs to Check Prime Number

# 1. How to Check if Number is Prime In Python

def is_prime(n):
    if n <= 1:
        return False # Numbers <= 1 are not prime

    # Loop through numbers from 2 to n-1
    for i in range(2, n):
        if n % i == 0: # Check divisibility
            return False

    # If no divisor found then it's a prime number
    return True

print(is_prime(19))
print(is_prime(49))

# 2. Using math.sqrt function

import math

n = 19
is_prime = True

if n <= 1:
    is_prime = False

# Check divisors up to the square root of n
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False

print(f"Is {n} a prime number? - {is_prime}")


# 3. Optimized Method (Skipping Even Numbers)

import math

n = 19
is_prime = True

# Handle special cases for 1 and 2
if n <= 1:
    is_prime = False
elif n == 2:
    is_prime = True # 2 is the only even prime number
elif n % 2 == 0:
    is_prime = False

# Loop through odd numbers from 3 to sqrt of n
sqrt_number = int(math.sqrt(n)) + 1 # Add 1 to ensure we check the square root itself
for i in range(3, sqrt_number, 2):
    if n % i == 0:
        is_prime = False

print(f"Is {n} a prime number? - {is_prime}")


# 4. Using the all() function with List Comprehension

import math

n = 19
is_prime = True
if n <= 1:
    is_prime = False
is_prime = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
print(f"Is {n} a prime number? - {is_prime}")
