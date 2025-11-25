# Python Programs to Calculate Area, Perimeter, Diagonal of Rectangle

# 1. How to Calculate Area, Perimeter and Diagonal of a Rectangle

import math

# length and width measurement
length = 10
width = 5

# Calculate Area
area = length * width

# Calculate Perimeter
perimeter = 2 * (length + width)

# Calculate Diagonal
diagonal = math.sqrt(length**2 + width**2)

# Display the result
print(f"Area is {area} square units. Perimeter is {perimeter} units. Diagonal is {diagonal} units.")

# 2. Calculate Using User Inputs

import math
# Step 1: Take input and convert it to float
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Step 2: Use the formula
area = length * width
perimeter = 2 * (length + width)
diagonal = math.sqrt(length**2 + width**2)

# Step 3: Display the result
print(f"Area is {area} square units. Perimeter is {perimeter} units. Diagonal is {diagonal} units.")


# 3. Calculate Using a Function

import math

# Function to calculate area
def rectangle_area(length, width):
    return length * width

# Function to calculate perimeter
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate the diagonal
def rectangle_diagonal(length, width):
    return math.sqrt(length**2 + width**2)

# Example usage
length = 10
width = 5

area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)
diagonal = rectangle_diagonal(length, width)

# Display the result
print(f"Area is {area} square units. Perimeter is {perimeter} units. Diagonal is {diagonal} units")


# 4. Calculate Using Class (OOP)

import math

# Define a class named Rectangle
class Rectangle:
    # Constructor to initialize length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def calculate_area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    # Method to calculate diagonal
    def calculate_diagonal(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)

# Create an object of the Rectangle class
rect = Rectangle(10, 5)

# Call the methods
area = rect.calculate_area()
perimeter = rect.calculate_perimeter()
diagonal = rect.calculate_diagonal()

# Display the result
print(f"Area is {area} square units. Perimeter is {perimeter} units. Diagonal is {diagonal} units.")


# 5. Calculate Using Lambda

import math

length = 10
width = 5

rectangle_area = lambda length, width: length * width

rectangle_perimeter = lambda length, width: 2 * (length + width)

rectangle_diagonal = lambda length, width: math.sqrt(length**2 + width**2)

# Call the methods
area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)
diagonal = rectangle_diagonal(length, width)

# Display the results
print(f"Area is {area} square units. Perimeter is {perimeter} units. Diagonal is {diagonal} units.")
