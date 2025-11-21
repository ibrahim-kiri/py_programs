# Count Digits of a Number in Python

# 1. Using a Loop

num = 123456
count = 0
while num != 0:
    num //= 10 # Integer division by 10 removes the last digit
    count += 1 # Increment the count for each digit removed
print("Number of digits:", count)

# 2. Using String Conversion

num = 123456
count = len(str(abs(num))) # Convert number to string and count its length
print("Number of digits:", count)

# 3. Using Regular Expressions (regex)

import re

num = 123456
count = 0
count = len(re.findall(r'\d', str(abs(num)))) # Find all digit characters using regex
print("Number of digits:", count)

# 4. Using Logarithms

import math

num = 123456
count = 0
if num == 0:
    count = 1 # Special case for zero, which has one digit
else:
    count = math.floor(math.log10(abs(num))) + 1

print("Number of digits:", count)

# 5. Using Recursion

def count(num):
    num = abs(num)
    if num == 0:
        return 0 # Base case: no more digits to count
    return 1 + count(num // 10)

num = 123456
print("Number of digits:", count(num))


# 6. Using List Comprehension and sum()

num = 123456
count = 0
count = sum(1 for _ in str(abs(num))) # Sum up 1 for each character in a string
print("Number of digits:", count)

# 7. Using len() on an Iterator

num = 123456
count = 0
count = len([_ for _ in str(abs(num))]) # Use len() to count the length of a list
print("Number of digits:", count)


# 8. Using the reduce() Function

from functools import reduce

num = 123456
count = 0
count = reduce(lambda x, y: x + 1, str(abs(num)), 0)
print("Number of digits:", count)

# 9. Using the map() Function

num = 123456
count = 0
count = sum(map(lambda x: 1, str(abs(num)))) # Map each character to 1 and sum them
print("Number of digits:", count)
