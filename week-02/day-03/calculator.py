# Create a simple calculator application which does read the parameters from the prompt  # nopep8
# and prints the result to the prompt.

# It should support the following operations:
# +, -, *, /, % and it should support two operands.

# The format of the expressions must be: {operation} {operand} {operand}.
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
op = str(input("Choose an operator( + - / % *): "))

if op == "+":
    print(number1 + number2)
elif op == "-":
    print(number1 - number2)
elif op == "/":
    print(number1 / number2)
elif op == "%":
    print(number1 % number2)
elif op == "*":
    print(number1 * number2)
