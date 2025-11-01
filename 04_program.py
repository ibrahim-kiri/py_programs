# Programs for Summing Even Numbers from 1 to n

# 1. Using a Mathematical Formula

n = 100
k = n // 2 # here, k = 50
even_sum = k * (k + 1)
print(f'Sum of even number from 1 to {n} is {even_sum}'
)

# 2. Using a For Loop with Modulus Operator (%)

n = 100
even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
print(f'Sum of even number from 1 to {n} is {even_sum}')

# 3. Using range() with a Step and sum()

n = 100
even_sum = sum(range(2, n + 1, 2))
print(f'Sum of even number from 1 to {n} is {even_sum}')

# 4. Using a List Comprehension with sum()

n = 100
even_sum = sum([i for i in range(2, n + 1, 2)])
print(f'Sum of even number from 1 to {n} is {even_sum}')

# 5. Using Functional Programming with filter() and lambda

n = 100
even_sum = sum(filter(lambda x: x % 2 == 0, range(1, n + 1)))
print(f'Sum of even number from 1 to {n} is {even_sum}')
