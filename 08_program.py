# Find all Divisors of Number in Python

# 1. Find all the Divisors of a Number in Python using loop

num = 36
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print(f"Divisors of {num}: {divisors}")

# 2. Using math.sqrt function

import math

num = 36
divisors = []

# Iterate from 1 to sqrt(num)
for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0: # If 'i' is a divisor of 'num'
        divisors.append(i)  # Add 'i' to the list of divisors
        if i != num // i:
            divisors.append(num // i)   # Add the corresponding divisor
print(f"Divisors of {num}: {divisors}")

# 3. Using List Comprehension

num = 36
divisors = [i for i in range(1, num + 1) if num % i == 0]
print(f"Divisors of {num}: {divisors}")


# 4. Using a Generator

def find_divisors_generator(n):
    for i in range(1, int(n**0.5) + 1): #   loop up to the sqrt of n
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i    # Yield the paired divisor

num = 36
divisors = list(find_divisors_generator(num))
print(f"Divisors of {num}: {divisors}")






