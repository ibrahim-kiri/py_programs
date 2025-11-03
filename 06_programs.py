# Python Swap Two Numbers

# 1. Swap two numbers using tuple unpacking

# Initializing numbers
a = 50
b = 100

# Swapping using tuple unpacking
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 2. Swap two numbers using Temporary Variable

# Initializing numbers
a = 50
b = 100

# Print original values
print("Original values:")
print("a =", a)
print("b =", b)

# Using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


#3. Swap two numbers without using a temporary variable

a = 50
b = 100

print("Before swapping")
print("a =", a, "b =", b)

# Swapping without a temporary variable
a = a + b   # a now holds the sum of a and b
b = a - b   # b now holds the original value of a
a = a - b   # a now holds the original value of b

print("After swapping:")
print("a =", a)
print("b =", b)

# ii) Example 2: Using Multiplication and Division

a = 50
b = 100

print("Before swapping:")
print("a =", a, "b =", b)

# Swapping without a temporary variable
a = a * b
b = a // b
a = a // b

print("After swapping:")
print("a =", a)
print("b =", b)


# 4. Swap two numbers using XOR swap

a = 50
b = 100

print("Before swapping:")
print("a =", a, "b =", b)

# Swapping using XOR
a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)


# 5. Swapping in a Function Using Multiple Assignment

def swap_numbers(a, b):
    print("Before swapping:")
    print("a =", a, "b =", b)
    return b, a

# Initializing numbers
a = 50
b = 100

# Swapping using a function
a, b = swap_numbers(a, b)

print("After swapping:")
print("a =", a)
print("b =", b)


# 6. Swap two numbers Using list indexing

# Initializing numbers in list
numbers = [50, 100]
print("Before swapping:")
print("a =", numbers[0], "b =", numbers[1])

# Swapping using list indexing
numbers[0], numbers[1] = numbers[1], numbers[0]

print("After swapping:")
print("a =", numbers[0])
print("b =", numbers[1])



