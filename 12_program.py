# Python Programs to Find Power of a Number (a^n)

# 1. Using a Loop – Manual approach

base = 2
exponent = 3
result = 1

for _ in range(exponent):
    result *= base
print(result)

# 2. Using the ** Operator

base = 2
exponent = 3
result = base ** exponent   # 2^3 = 8
print(result)

# 3. Using the pow() Function

result = pow(2, 3)
print(result)

# Code Example with modulus
result = pow(2, 3, 5)
print(result)

# 4. Using the math.pow() Function

import math
result = math.pow(2, 3)
print(result)

# 5. Using Recursion

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

result = power(2, 3)
print(result)
