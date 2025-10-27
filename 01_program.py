# Python Program to Check if a Number is Positive, Negative, or 0

# 1.Using if-elif-else Statements
num = 10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2.Using Ternary (Conditional) Operator
num = -10
sign = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(sign)

# 3.Using Lambda function
num = 0
check_sign = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(check_sign(num))


# 4.Using NumPy’s sign Function

import numpy as np

num = 2
sign = np.sign(num)

if sign == 1:
    print("Positive")
elif sign == -1:
    print("Negative")
else:
    print("Zero")



