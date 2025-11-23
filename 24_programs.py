# Generate Fibonacci Series in Python

# 1. How to Generate Fibonacci Series in Python

def fibonacci_iterative(n):
    if n <= 0:
        return "Please enter s positive number" # Handle invalid input
    elif n == 1:
        return [0] # If only one number is needed, return [0]
    elif n == 2:
        return [0, 1] # If two numbers are needed, return [0, 1]

    fib_series = [0, 1] #  Start with the first two Fibonacci numbers

    for i in range(2, n): # Start loop from 3rd number (index 2)
        next_number = fib_series[i - 1] + fib_series[i - 2] # Add last two numbers
        fib_series.append(next_number) # Store the result in the list

    return fib_series # Return the full Fibonacci series

# Example usage
print(fibonacci_iterative(10))


# 2. Iterative Approach using a while loop

def fibonacci_iterative_while(n):
    """Generative the Fibonacci series up to n terms using a while loop"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        a, b = 0, 1
        count = 2
        while count < n:
            next_fib = a + b
            list_fib.append(next_fib)
            a, b = b, next_fib
            count += 1
        return list_fib

# Example
num_terms = 8
fib_series = fibonacci_iterative_while(num_terms)
print(f"Fibonacci series up to {num_terms} terms (iterative while): {fib_series}")

# 3. Using Recursion

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = 10
fib_sequence = [fibonacci_recursive(i) for i in range(n)]
print("Fibonnaci Series:", fib_sequence)


# 3. Generator Method

def fibonnaci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = 10
fib_gen = fibonnaci_generator()
fib_sequence = [next(fib_gen) for _ in range(n)]
print("Fibonacci Series:", fib_sequence)
