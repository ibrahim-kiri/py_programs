# Program to find Even Numbers in Range

# 1. find even numbers in a range using a for loop
start = 10
end = 30

# List to store even numbers
even_numbers = []

for num in range(start, end + 1):
    # Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num) # Add even number to the list

print(f"Even numbers between {start} and {end} are: {even_numbers}")

# 2. Using List Comprehension
# Using list comprehension to find even numbers between 10 to 30
even_numbers = [num for num in range(10, 31) if num % 2 == 0]
print(f"Even numbers between {start} and {end} are: {even_numbers}")


# 3. Using Python’s filter() Function with Lambda
start = 10
end = 30

# Using filter and lambda to find even numbers
even_numbers = list(filter(lambda num: num % 2 == 0, range(start, end + 1)))
print(f"Even numbers between {start} and {end} are: {even_numbers}")

# 4. Using a Generator
# Define a generator function to find even numbers
def find_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num # Yield even numbers one at a time

# Define the range
start = 10
end = 30
# Generate even numbers and convert to a list
even_numbers = list(find_even_numbers(start, end))
print(f"Even numbers between {start} and {end} are: {even_numbers}")


# 5. Using NumPy
import numpy as np

# Using NumPy to find even numbers in a range
def find_even_numbers(start, end):
    return np.arange(start + start % 2, end + 1, 2)

# Define the range
start = 10
end = 30

# Generate even numbers and convert to a list
even_numbers = list(find_even_numbers(start, end))
# Print the result
print(f"Even numbers between {start} and {end} are: {even_numbers}")

