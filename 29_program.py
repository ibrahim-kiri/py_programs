# Python Programs to Calculate Area of Triangle

# 1. How to Calculate Area of a Triangle

# Step 1: Define base and height
base = 10
height = 5

# Step 2: Calculate area using the formula A = (1/2) * base * height
area = 0.5 * base * height

# Step 3: Display the result
print("Area of the triangle:", area, "square units")

# 2. Calculate Area of Triangle Using User Inputs

# Step 1: Get user input for base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Step 2: Calculate area using the formula A = (1/2) * base * height
area = 0.5 * base *  height

# Step 3: Display the result
print("Area of the triangle:", area, "square units")


# 3. Calculate Area of Triangle Using a Function

def triangle_area(base, height):
    return 0.5 * base * height

triangle1 = triangle_area(10, 5)
print("Area of the triangle1:", triangle1, "square units")

triangle2 = triangle_area(20, 7)
print("Area of the triangle2:", triangle2, "square units")


# 4. Calculate Area of Triangle Using Class (OOP)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Creating an object of the Triangle class
triangle1 = Triangle(10, 5)
triangle2 = Triangle(20, 7)

# Printing the area
print("Area of the triangle1:", triangle1.calculate_area(), "square units")
print("Area of the triangle2:", triangle2.calculate_area(), "square units")


# 5. Calculate Area of Triangle Using Lambda

triangle_area = lambda base, height: 0.5 * base * height

# Example usage
print("Area of the triangle:", triangle_area(10, 5), "square units")


