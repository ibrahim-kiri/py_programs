# Programs to Check if a Number is Odd or Even

# 1. Using the Modulo Operator (%)
number = int(input("Enter a number: "))

# Check if the number is even or odd using the modulus operator
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# 2. Using Integer Division operator (//)
number = int(input("Enter a number: "))

# Check if the number is even or odd using integer division
if (number // 2) * 2 == number:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
