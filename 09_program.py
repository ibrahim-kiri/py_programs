# Create Multiplication Table in Python

# 1. Print the multiplication table for a specific number using for loop
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 2. Print Full Multiplication Table Using Nested Loops
for i in range(1, 11):
    print('multiplication table of:', i)
    for j in range(1, 11):
        print(f" {i * j}", end="")
    print() # Move to the next line after each row


# 3. Create multiplication table using while loop

# Initialize the outer loop counter
i = 1

# Outer loop for each multiplication table
while i <= 10:
    print(f"Multiplication table of: {i}")  # Print header for the table

    # Initialize the inner loop counter
    j = 1

    # Inner loop for each multiplier
    while j <= 10:
        print(f" {i * j}", end="")  # Print the product on the same line
        j += 1  # Increment the inner loop counter

    print() # Move to the next line after each row
    i += 1  # Increment the outer loop counter


# 4. Create multiplication table using List Comprehension

multiplication_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]

for row in multiplication_table:
    print(' '.join(map(str, row)))


# 5. Using Functions

def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Call the function
num = int(input("Enter a number: "))
print('Multiplication table of', num)
print_multiplication_table(num)


# 6. Using Libraries (e.g., Pandas)
import pandas as pd

# Create a DataFrame for the multiplication table
def create_multiplication_table():
    data = {i: [i * j for j in range(1, 11)] for i in range(1, 11)}
    df = pd.DataFrame(data, index=range(1, 11))
    return df

# Generate and display the table
multiplication_table_df = create_multiplication_table()
print(multiplication_table_df)


# 7. Using String Formatting for Better Alignment

print('Full multiplication table with alignment')
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

#8. Interactive Multiplication Table Generator

def interactive_table():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of column: "))

    for i in range(1, rows + 1):
        print('Multiplication table of:', i)
        for j in range(1, cols + 1):
            print(f"{i * j}", end=" ")
        print()

interactive_table()





