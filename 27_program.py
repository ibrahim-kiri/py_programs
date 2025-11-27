# Python Programs to Calculate Area and Perimeter of Circle

# 1. How to Calculate Area and Circumference of a Circle

import math # Step 1: Import the math module

# Step 2: Define radius
radius = 5

# Step 3.1: Calculate area
area = math.pi * radius ** 2

# Step 3.2: Calculate the perimeter
perimeter = 2 * math.pi * radius

# Step 4: Display the result
print(f"Area is {area} square units")
print(f"Perimeter is {perimeter} units")

# 2. Calculate Using User Inputs

import math # Step 1: Import the math module

# Step 2: Get user input for radius
radius = float(input("Enter the radius of the circle: "))

# Step 3.1: Calculate area
area = math.pi * radius ** 2

# Step 3.2: Calculate the perimeter
perimeter = 2 * math.pi * radius

# Step 4: Display the result
print(f"Area is {area} square units and perimeter is {perimeter} units")

# 3. Calculate Using a Function

import math # import math module

# Function to calculate area of a circle
def circle_area(radius):
    return math.pi * radius ** 2 # Formula: A = pir2

# Function to calculate perimeter of a circle
def circle_perimeter(radius):
    return 2 * math.pi * radius

# Function call
radius = 5
area = circle_area(radius)
perimeter = circle_perimeter(radius)

# Display the result
print(f"Area is {area} square units and perimeter is {perimeter} units")


# 4. Calculate Area of Circle Using Class (OOP)

import math # import math module

# Define a class named Circle
class Circle:
    # Constructor to initialize radius
    def __init__(self, radius):
        self.radius = radius # Store radius

    # Method to calculate area
    def calculate_area(self):
        return math.pi * self.radius ** 2

    # Method to calculate perimeter
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Create an object of Circle class
radius = 5
circle = Circle(radius)

# Call the methods
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

# Display the result
print(f"Area is {area} square units and perimeter is {perimeter} units")

# 5. Calculate Area of Circle Using Lambda

import math # import math module

radius = 5
circle_area = lambda radius: math.pi * radius ** 2
circle_perimeter = lambda r: 2 * math.pi * radius

area = circle_area(radius)
perimeter = circle_perimeter(radius)

# Display the result
print(f"Area is {area} square unitsand perimeter is {perimeter} units")
