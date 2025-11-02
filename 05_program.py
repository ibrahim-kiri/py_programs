# Python Program to Find Smallest and Largest Number

# 1. Using min() and max() Functions
num1 = 30.5
num2 = 10
num3 = -20

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

print(f"Smallest: {smallest}, Largest: {largest}")

# from list of numbers

numbers = [5, 10, 75, 2, 225]

smallest = min(numbers)
largest = max(numbers)

print(f"Smallest: {smallest}, Largest: {largest}")

# 2. Using Conditional Statements (if-else)
num1 = 30.5
num2 = 10
num3 = -20

def find_smallest(num1, num2, num3):
    # finding the smallest
    if num1 < num2 and num1 < num3:
        smallest = num1
    elif num2 < num3:
        smallest = num2
    else:
        smallest = num3
    return smallest

def find_largest(num1, num2, num3):
    # Finding the largest
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num3:
        largest = num2
    else:
        largest = num3
    return largest

smallest = find_smallest(num1, num2, num3)
largest = find_largest(num1, num2, num3)

print(f"Smallest: {smallest}, Largest: {largest}")


# 3. Using sorting
num1 = 30.5
num2 = 10
num3 = -20

numbers = [num1, num2, num3]    # Add numbers into list
numbers.sort()  # Sorting the list in ascending order
smallest = numbers[0]
largest = numbers[-1]

print(f"Smallest: {smallest}, Largest: {largest}")

