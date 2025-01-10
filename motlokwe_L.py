width = float(10)
height = float(5)
area = width * height

print(f"the area of rectangle:{area}")

# Simple Calculator Program

print("Welcome to the Simple Calculator!")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice
choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

# Get the numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the user's choice
if choice == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice! Please restart the program and choose a valid option.")
