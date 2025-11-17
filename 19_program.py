# Python Programs to Print Alternate Prime Numbers till N

# 1. Using a List to Store All Prime Numbers

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Set N
n = 20
primes = [] # List to store all prime numbers
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)

# Printing all prime numbers
print(f'All prime numbers from 1 to {n}: {primes}')
# Printing alternate prime numbers from the list
print(f'Alternate prime numbers from 1 to {n}:')

for i in range(0, len(primes), 2): # Step by 2 to get alternate primes
    print(primes[i])

# 2. Using a Counter for Alternate Primes

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 20
counter = 0 # Counter to track alternate primes
for num in range(2, n + 1):
    if is_prime(num):
        if counter % 2 == 0: # Print only alternate primes
            print(num, end=' ')
        counter += 1 # Increment counter for every prime number found

# 3. Using Generators for Efficient Prime Generation

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Using a generator to yield prime numbers
def prime_generator(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num # Yield prime number

n = 20
counter = 0
for prime in prime_generator(n):
    if counter % 2 == 0: # Print alternate primes
        print(prime, end=' ')
    counter += 1

