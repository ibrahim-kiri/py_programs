# Python Convert a Decimal Number to Hexadecimal and Vice Versa

# 1. Using Built-in hex() Function

decimal = 20
hex_value = hex(decimal)
print(f"Hexadecimal value: {hex_value[2:]}")

# 2. Using Built-in hex() Function

decimal = 13
hex_value = format(decimal, 'X') # 'x' for lowercase, 'X' for uppercase
print(f"Hexadecimal value: {hex_value}")


# 3. Using F-String Formatting

decimal = 255
print(f"Hexadecimal value: {decimal:X}")


# 4. Using While Loop

# function to convert decimal to hexadecimal
def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    hex_results = ""

    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % 16
        hex_result = hex_digits[remainder] + hex_results
        decimal = decimal // 16

    return hex_result

# Example
decimal = 2545
print(f"Hexadecimal value: {decimal_to_hex(decimal)}")


# 5. Using Recursion

# recursion function to convert hexadecimal to decimal
def decimal_to_hex_recursive(n):
    hex_digits = "0123456789ABCDEF"
    if n < 16:
        return hex_digits[n]
    return decimal_to_hex_recursive(n // 16) + hex_digits[n % 16]

decimal = 2545
print(f"Hexadecimal value: {decimal_to_hex_recursive(decimal)}")


# Convert Hexadecimal to Decimal

# 1. Using Built-in int() with Base 16

hex = "1A"
decimal = int(hex, 16)
print(f"Decimal value of {hex} is {decimal}")

# 2. Manual Conversion Using Loop

# function to convert hexadecimal to decimal
def hex_to_decimal(hex_str):
    hex_str = hex_str.upper()
    hex_digits = "0123456789ABCDEF"
    decimal = 0
    power = 0

    for digit in reversed(hex_str):
        value = hex_digits.index(digit)
        decimal += value * (16 ** power)
        power += 1

    return decimal

# Example
print(hex_to_decimal("1A"))
