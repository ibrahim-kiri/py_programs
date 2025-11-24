# Python Programs to Find Prime Numbers within a Range

# 1. Using loop for Checking Divisibility

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = 50
end = 100
primes = []
for num in range(start, end + 1):
    if is_prime(num):
        primes.append(num)
print(primes)

# 2. Optimized Method (Check up to √n)

import math

def is_prime_optimized(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

start = 50
end = 100
primes = []
for num in range(start, end + 1):
    if is_prime_optimized(num):
        primes.append(num)
print(primes)
