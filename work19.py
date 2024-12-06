def calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error! Division by zero")
    else:
        print("Invalid operation")

calculator(10, 5, '+')
calculator(10, 5, '-')
calculator(10, 5, '*')
calculator(10, 5, '/')