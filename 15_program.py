# Python Programs to Check Palindrome Number

# 1. How to check Palindrome Number in Python
number = 12321

# Convert number to string
num_str = str(number)
# Reverse the string
rev_num_str = num_str[::-1]

# Compare original string with its reverse
if num_str == rev_num_str:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


# 2. Mathematical Reversal (Without String Conversion)

number = 12321
original_number = 12321
reversed_number = 0

while number > 0:
    digit = number % 10 # Extract the last digit
    reversed_number = reversed_number * 10 + digit # Append digit to reversed number
    number = number // 10 # Remove the last digit fromthe number

is_palindrome = original_number == reversed_number

print(f"Is {original_number} is a palindrome? : {is_palindrome}")


# 3. Recursive Method

# Recursive function
def is_palindrome_recursive(num, rev=0):
    # base case
    if (num == 0):
        return rev;

    # stores the reverse of a number
    rev = (rev * 10) + (num % 10);

    return is_palindrome_recursive(num // 10, rev);

#Start
number = 12321
rev_num = is_palindrome_recursive(number)
is_palindrome = number == rev_num

print(f"Is {number} a palindrome? : {is_palindrome}")


# 4. Using Stack (Last In, First Out)

def is_palindrome_stack(number):
    num_str = str(number) # Convert number to string
    stack = [] # Initialze stack

    # Push all characters onto the stack
    for char in num_str:
        stack.append(char)

    reversed_str = ''
    # Pop characters from the stack to create reversedstring
    while stack:
        reversed_str += stack.pop()

    return num_str == reversed_str # checking originalnum with reversed

number = 12321
is_palindrome = is_palindrome_stack(number)

print(f"Is {number} is a plaindrome? : {is_palindrome}")

    
