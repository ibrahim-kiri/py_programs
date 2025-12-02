# Python Programs to Calculate Perimeter of Triangle

# 1. How to Calculate Perimeter of Triangle

# Get all sides of triangle
side1 = 5
side2 = 6
side3 = 7

# Perimeter Formula
perimeter = side1 + side2 + side3
print("Perimeter of the triangle:", perimeter)


# 2. Calculate Perimeter of Triangle Using User Inputs

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

perimeter = a + b + c
print("Perimeter of the triangle:", perimeter)


# 3. Calculate Perimeter of Triangle Using User Inputs

# Function to calculate perimeter
def triangle_perimeter(a, b, c):
    return a + b + c

# Example usage
p1 = triangle_perimeter(5, 6, 7)
print("Perimeter of the triangle:", p1)

p2 = triangle_perimeter(10, 12, 14)
print("Perimeter of the triangle:", p2)

# 4. Calculate Perimeter of Triangle Using Class (OOP)

# Define a class named Triangle
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Method to calculate perimeter
    def calculate_perimeter(self):
        return self.a + self.b + self.c

# Create an object of the Triangle class
triangle1 = Triangle(5, 6, 7)
triangle2 = Triangle(10, 12, 14)

# Call the method to calculate perimeter
p1 = triangle1.calculate_perimeter()
p2 = triangle2.calculate_perimeter()

# Display the perimeter
print("Perimeter of the triangle1:", p1)
print("Perimeter of the triangle2:", p2)


# 5. Calculate Perimeter of Triangle Using Lambda

triangle_perimeter = lambda a, b, c: a + b + c
print("Perimeter of the triangle:", triangle_perimeter(5, 6, 7))
