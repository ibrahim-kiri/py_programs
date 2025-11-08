# Python Programs to Find HCF and LCM of two numbers

# 1. Using the math Module

import math

# Input numbers
a = 24
b = 36

# HCF
hcf = math.gcd(a, b)

# LCM
lcm = (a * b) // hcf

print(f"HCF: {hcf}")
print(f"LCM: {lcm}")


# 2. Using an Iterative Approach

def find_hcf(a, b):
    while b:    # The loop runs until b becomes 0
        a, b = b, a % b    # Update a with b, and b with the remainder
    return a

# Input numbers
a = 24
b = 36

hcf = find_hcf(a, b)
lcm = (a * b) // hcf    # Calculate lcm using hcf

print(f"HCF: {hcf}")
print(f"LCM: {lcm}")


# 3. Using Recursion

def find_hcf_recursive(a, b):
    if b == 0:
        return a
    return find_hcf_recursive(b, a % b)

# Input numbers
a = 24
b = 36

hcf = find_hcf_recursive(a, b)
lcm = (a * b) // hcf    # Calculate lcm using hcf

print(f"HCF: {hcf}")
print(f"LCM: {lcm}")
