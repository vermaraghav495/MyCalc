while True:
    try:
        additional_numbers = []
        num1 = float(input("Tell the first number: "))
        num2 = float(input("Tell the second number: "))
        operation = input("Choose an operation (+, -, *, / , ^ ,pie,exit): ")
        
        if operation == '+':
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                for n in num_list:
                    Final_result = n + num1 + num2
                print(f"The result of {operation} {num1} {num2} {additional_numbers} and the additional numbers is: {Final_result}")
                break
            else:
                result = num1 + num2
                print(f"The result of {num1} {operation} {num2} is: {result}")
        
        elif operation == '-':
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                result =  num1 - num2 
                for num in num_list:
                    Final_result = result - num
                print(f"The result of {num1} {operation} {num2} {additional_numbers}and the additional numbers is: {Final_result}")
            else:
                result = num1 - num2
                print(f"The result of {num1} {operation} {num2} is: {result}")  
        
        elif operation == '*':
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                result = num1 * num2
                for num in num_list:
                    Final_result = result * num
                print(f"The result of {operation} {num1} and the additional numbers is: {Final_result}")
            else:
                result = num1 * num2
                print(f"The result of {num1} {operation} {num2} is: {result}")


        elif operation == 'pie':
            import math
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                result =  num1 * math.pi
                for num in num_list:
                    Final_result = result * num
                print(f"The result of {operation} {num1} and the additional numbers is: {Final_result}")
            else:
                result = num1 * math.pi
                print(f"The result of {num1} {operation} is: {result}")


        elif operation == '/':
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                result = num1 / num2
                for num in num_list:
                    Final_result = result / num
                print(f"The result of {operation} {num1} and the additional numbers is: {Final_result}")
            else:
                result = num1 / num2
                print(f"The result of {num1} {operation} {num2} is: {result}")
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            


        elif operation == '^':
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                result =  num1 ** num2
                for num in num_list:
                    Final_result = result ** num
                print(f"The result of {num1} {operation} {num2} {additional_numbers} and the additional numbers is: {Final_result}")
            else:
                result = num1 ** num2
                print(f"The result of {num1} {operation} {num2} is: {result}")
            if num2 < 0:
                print("Error: Negative exponentiation is not allowed.")
                continue

        elif operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue


        print(f"The result of {num1} {operation} {num2} {additional_numbers} is:  {Final_result}")
        break
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
print("Thank you for using the calculator!")