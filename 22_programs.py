# Check Armstrong Number in Python

# 1. How to check Armstrong number in Python

def is_armstrong(number):
    # Convert the number to string to easily iterate over it's digits
    digits = str(number)

    # Calculate the length (number of digits) of the number
    num_digits = len(digits)

    # Initialize a variable to store the sum of digits
    sum_of_powers = 0

    # Iterate over each digit and calculate it's power
    for digit in digits:
        sum_of_powers += int(digit) ** num_digits

    # Check if the sum of powers is equal to the original number
    if sum_of_powers == number:
        return True
    else:
        return False

# function call
print(is_armstrong(153))
print(is_armstrong(154))

# 2. Using Mathematical Operation

number = 153

# Store the original number
temp = number
# Calculate the number of digits
num_digits = len(str(number))
# Initialize sum to store the results of raising digits to power
sum_of_powers = 0

# Iterate over the digits using mathematical operatios
while temp > 0:
    digit = temp % 10 # Extract the last digit
    sum_of_powers += digit ** num_digits # Raise it to the power of num_digits and add it to the sum
    temp //= 10 # Remove the last digit from temp

# Compare with the original number
is_armstrong = sum_of_powers == number
print(f"Is {number} an Armstrong number? : {is_armstrong}")


# 3. Using Recursion

def sum_of_powers_recursive(number, num_digits):
    if number == 0:
        return 0
    else:
        # Extract the last digit and recursively sum powers
        return (number % 10) ** num_digits + sum_of_powers_recursive(number // 10, num_digits)

number = 153
num_digits = len(str(number))
is_armstrong = number == sum_of_powers_recursive(number, num_digits)
print(f"Is {number} an Armstrong numbers? : {is_armstrong}")

# 4. Using Python’s map and lambda functions

number = 153

num_digits = len(str(number))
is_armstrong = number == sum(map(lambda x: int(x) ** num_digits, str(number)))

print(f"Is {number} an Armstrong number? : {is_armstrong}")


# 5. Using List Comprehension

number = 153

num_digits = len(str(number))
# List comprehension to calculate the sum of digits raised to the power of num_digits
is_armstrong = number == sum([int(digit) ** num_digits for digit in str(number)])

print(f"Is {number} an Armstrong number? : {is_armstrong}")
