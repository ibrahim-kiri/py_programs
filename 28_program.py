# Python Programs to Calculate Area, Perimeter and Diagonal of Square

# 1. How to Calculate Area, Perimeter and Diagonal of a Square
import math

side = 5 # Length of one side
area = side * side # Area formula
perimeter = 4 * side # Perimeter formula
diagonal = math.sqrt(2) * side # Diagonal formula

print(f"Area is {area} square units, Perimeter is {perimeter} units, Diagonal is {diagonal} units")

# 2. Calculate Using User Inputs
import math

side = float(input("Enter the side length of the square: "))
area = side * side # Area formula
perimeter = 4 * side # Perimeter formula
diagonal = math.sqrt(2) * side # Diagonal formula

print(f"Area is {area} square units, Perimeter is {perimeter} units, Diagonal is {diagonal} units")


# 3. Calculate Using a Function

import math

# Function to calculate the area
def square_area(side):
    return side * side

# Function to calculate the perimeter
def square_perimeter(side):
    return 4 * side

# Function to calculate the Diagonal
def square_diagonal(side):
    return math.sqrt(2) * side

# Function calls
side = 5
area = square_area(side)
perimeter = square_perimeter(side)
diagonal = square_diagonal(side)

# Display the result
print(f"Area is {area} square units, Perimeter is {perimeter} units, Diagonal is {diagonal} units")


# 5. Calculate Area of Square Using Class (OOP)

import math

class Square:
    def __init__(self, side):
        self.side = side # Initialize side length

    # Method to calculate the area
    def calculate_area(self):
        return self.side * self.side

    # Method to calculate the perimeter
    def calculate_perimeter(self):
        return 4 * self.side

    # Method to calculate the perimeter
    def calculate_diagonal(self):
        return math.sqrt(2) * self.side

side = 5 # length of side
sq = Square(side) # object of square class

# method calls
area = sq.calculate_area()
perimeter = sq.calculate_perimeter()
diagonal = sq.calculate_diagonal()

# Display the result
print(f"Area is {area} square units, Perimeter is {perimeter} units, Diagonal is {diagonal} units")


# 5. Calculate Using Lambda
import math

square_area = lambda side: side * side
square_perimeter = lambda side: 4 * side
square_diagonal = lambda side: math.sqrt(2) * side

side = 5 # length of side
area = square_area(side)
perimeter = square_perimeter(side)
diagonal = square_diagonal(side)

# Display the result
print(f"Area is {area} square units, Perimeter is {perimeter} units, Diagonal is {diagonal} units")
