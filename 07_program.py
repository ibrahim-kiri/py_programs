# Python Find the Numbers Divisible by Another Number

# 1. How to find the Numbers Divisible by Another Number in Python

numbers = [10, 15, 22, 33, 40, 50, 60]
divisor = 10
divisibles = []

for num in numbers:
    if num % divisor == 0:  # Check divisibility
        divisibles.append(num); # Add divisible in list

print(divisibles)

# 2. Using the filter() Function

numbers = [10, 15, 22, 33, 40, 50, 60]
divisor = 10
divisible_numbers = filter(lambda x: x % divisor == 0, numbers)
print(f'Numbers divisible by {divisor}:', *divisible_numbers)


# 3. Using Recursion

def divisible_numbers(numbers, divisor):
    if len(numbers) == 0:   # Base case: stop if list is empty
        return
    if numbers[0] % divisor == 0:
        print(f'Number {numbers[0]} is divisible by {divisor}')
    else:
        print(f'Number {numbers[0]} is NOT divisible by {divisor}')
    divisible_numbers(numbers[1:], divisor) # Recursive call with the rest of the list

numbers = [10, 15, 22, 33, 40, 50, 60]
divisor = 10
divisible_numbers(numbers, divisor)

# 4. Using List Comprehension

numbers = [10, 15, 22, 33, 40, 50, 60]
divisor = 10
divisible_numbers = [num for num in numbers if num % divisor == 0]
print(f'Numbers divisible by {divisor}:', divisible_numbers)


