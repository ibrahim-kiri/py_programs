# Python Programs to Find Sum of First n Prime Numbers

# 1. Using loop

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): # Optimized by checking till the sqrt of n
        if num % i == 0:
            return False
    return True

n = 4 # first 5 prime numbers
prime_sum = 0 # sum of prime numbers
prime_counter = 0 # counter of prime numbers
num = 2 # Start from the first prime number
while prime_counter < n:
    if is_prime(num):
        print(num)
        prime_sum += num
        prime_counter += 1
    num += 1
print(f"The sum of the first {n} prime numbers is: {prime_sum}")


# 2. Using Python’s Built-in filter() and itertools
import math
import itertools

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): # optimized by checking till sqrt of n
        if num % i == 0:
            return False
    return True

n = 4
primes = filter(is_prime, itertools.count(2)) # infinite generator of prime numbers
prime_sum = sum(itertools.islice(primes, n))
print(f"The sum of the first {n} prime numbers is: {prime_sum}")


