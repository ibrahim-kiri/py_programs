# Python Convert Decimal Numbers to Octal and vice versa

# 1. Using Built-in oct() Function

decimal = 26
octal = oct(decimal)
print(f"Octal value: {octal[2:]}")


# 2. Using format() Function

decimal = 255
octal = format(decimal, 'o')
print(f"Octal value: {octal}")


# 3. Using F-String Formatting

decimal = 65
print(f"Octal value: {decimal:o}")

# 4. Using a While Loop

def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

decimal = 65
print("Octal value:", decimal_to_octal(decimal))


# Octal to Decimal Conversion in Python

# 1. Using Built-in int() with Base 8

oct = "101"
decimal = int(oct, 8)
print(f"Decimal value of {oct} is {decimal}")

# 2. Manual Conversion Using Loop
# function to convert octal to decimal
def octal_to_decimal(octal_str):
    decimal = 0
    power = 0

    # Start from the rightmost digit
    for digit in reversed(octal_str):
        decimal += int(digit) * (8 ** power)
        power += 1

    return decimal

# Example
octal = "127"
print("Decimal value:", octal_to_decimal(octal))
