while True:
    try:
        num1 = float(input("Tell the first number: "))
        num2 = float(input("Tell the second number: "))
        operation = input("Choose an operation (+, -, *, / , ^ ,pie): ")
        
        if operation == '+':
            result = num1 + num2
        
        elif operation == '-':
            result = num1 - num2
        
        elif operation == '*':
            result = num1 * num2

        elif operation == 'pie':
            import math
            result = math.pi * num1 * num2
        
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2

        elif operation == '^':
            result = num1 ** num2
        
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        print(f"The result of {num1} {operation} {num2} is:  {result}")
        break
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
print("Thank you for using the calculator!")    