import math
print("Welcome to the CLI Calculator!")
Current_result = None
num1=0
while True:
    try:
        add_again = input("Do you want to add / do operations of the numbers you did last? (yes/no): ").strip().lower()
        if add_again in ('yes', 'no'):
            if add_again == 'yes' and Current_result is not None:
                num1 = Current_result
                print(f"Using the last result: {num1}")
            elif add_again == 'no':
                num1 = float(input("Tell the first number: "))
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")
                continue
        additional_numbers = []
        num2 = float(input("Tell the second number: "))

        operation = input("Choose an operation (+, -, *, / , ^ ,pie,exit): ")


        if operation == '+':
            Final_result = num1 + num2
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                for n in num_list:
                    Final_result += n
                    continue
            else:
                Final_result = num1 + num2
        
        elif operation == '-':
            Final_result =  num1 - num2 
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                Final_result -= n
             
            else:
                Final_result = num1 - num2
        
        elif operation == '*':
            Final_result = num1 * num2
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                Final_result = num1 * num2
                for n in num_list:
                    Final_result *= n
            else:
                Final_result = num1 * num2


        elif operation == 'pie':
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                Final_result =  num1 * math.pi
                for n in num_list:
                    Final_result *= n
            else:
                Final_result = num1 * math.pi
                

        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            Final_result = num1 / num2
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                Final_result = num1 / num2
                for n in num_list:
                    Final_result /= n
            else:
                Final_result = num1 / num2

        elif operation == '^':
            Final_result = num1 ** num2
            numbers = input("Do you want to add more numbers? (yes/no): ")
            if numbers.lower() == 'yes':
                additional_numbers = input("Enter the additional numbers separated by spaces: ")
                num_list = [float(n) for n in additional_numbers.split()]
                Final_result =  num1 ** num2
                for n in num_list:
                    Final_result **= n
            else:
                Final_result = num1 ** num2
            if num2 < 0:
                continue

        elif operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue
       
        print(f"The result of {num1} {operation} {num2} {additional_numbers} is:  {Final_result}")
        Final_result= 0
        num2=0
        continue
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("Thank you for using the calculator!")