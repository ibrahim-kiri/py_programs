# Python Programs to Reverse an Integer Number

# 1. How to reverse an integer number in Python
num = 123456
# Convert the integer to string and reverse it using slicing
reversed_str = str(num)[::-1]

# Handle negative numbers
if num < 0:
    reversed_int = int('-' + reversed_str[:-1]) # Exclude the last character which is '-'
else:
    reversed_int = int(reversed_str)

print('Reversed Integer:', reversed_int)


# 2. Using a Mathematical Approach

num = 123456
reversed_int = 0
negative = num < 0
num = abs(num)

while num != 0:
    reversed_int = reversed_int * 10 + num % 10 # Extract the last digit and append it to the reversed number
    num //= 10 # Remove the last digit

if negative:
    reversed_int = -reversed_int # Restore sign if negative

print('Reversed Integer:', reversed_int)


# 3. Using Recursion

def reverse_int(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_int(n // 10, rev * 10 + n % 10)

print('Reversed Integer:', reverse_int(123456))


# 4. Using List Reversal

num = 123456
sign = -1 if num < 0 else 1
n = abs(num)

digits = list(str(num)) # Convert string to list
digits.reverse() # Reverse the list

reverse_int = sign * int(''.join(digits)) # Convert list to string and then convert string to integer

print('Reversed Integer:', reverse_int)
