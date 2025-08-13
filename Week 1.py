# Basic Calculator Program


# Ask the user for two numbers
num1 = float(input("Enter the first number: "))


num2 = float(input("Enter the second number: "))


# Ask for the mathematical operation
operation = input("Enter the operation (+, -, *, /): ")


# Perform the calculation based on the operation
if operation == "+":

    result = num1 + num2

elif operation == "-":

    result = num1 - num2

elif operation == "*":

    result = num1 * num2

elif operation == "/":

    if num2 != 0:

        result = num1 / num2

    else:

        result = "Error! Division by zero."

else:

    result = "Invalid operation."


# Display the result
print(f"{num1} {operation} {num2} = {result}")
