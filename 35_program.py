# Python Programs Calculate Value of nCr

# 1. Using Factorial Formula
import math

def calculate_nCr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = 5
r = 3
result = calculate_nCr(n, r)
print(result)

# 2. Using the math.comb Function (Python 3.8+)
import math

# nCr = math.comb(n, r)
n = 5
r = 3
result = math.comb(n, r)
print(result)

# 3. Using Recursive Formula

def calculate_nCr_recursive(n, r):
    if r == 0 or r == n:
        return 1
    return calculate_nCr_recursive(n - 1, r - 1) + calculate_nCr_recursive(n - 1, r)

n = 5
r = 2
result = calculate_nCr_recursive(n, r)
print(result)
