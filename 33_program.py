# Python Convert Decimal Number to Binary and Vice Versa

# 1. Using Python’s Built-in bin() Function

decimal = 20
binary = bin(decimal)
print(f"Binary of {decimal} is {binary[2:]}")

# 2. Using format() Function

decimal = 20
binary = format(decimal, 'b')
print(f"Binary of {decimal} is {binary}")

# 3. Using F-String Formatting

decimal = 20
print(f"Binary of {decimal} is {decimal:b}")

# 4. Using While Loop

decimal = 20
binary = ""

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2 # Get the remainder which is the last binary digit (0 or 1)
        binary = str(remainder) + binary # Add it to the front of the result
        decimal = decimal // 2 # Divide number by 2 (Integer division)

print(binary)


# 5. Using Recursion

def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end= '')

decimal = 20
print("Binary is: ", end='')
decimal_to_binary(decimal)


# Convert Binary to Decimal

# 1. Using Built-in int() with Base 2

binary = "1010"
decimal = int(binary, 2)
print(f"Decimal value of {binary} is {decimal}")

# 2. Manual Conversion Using Loop

binary = "1010"
decimal = 0
power = 0

for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print(f"Decimal value is {decimal}")
