from replit import clear
# Calculator


def add(num_1,num_2):
    "Addition"
    res = num_1 + num_2
    return res

def subtract(num_1, num_2):
    """
        Subtraction
    """
    res = num_1 - num_2
    return res

def multiply(num_1, num_2):
    """
        Multiplication
    """
    res = num_1 * num_2
    return res

def divide(num_1, num_2):
    """
        Division
    """
    res = num_1 / num_2
    return res

def calc(number_1, number_2, operation):
    """
        Calculator
    """
    if operation == "+":
        final_res = add(number_1, number_2)
        return final_res

    elif operation == "-":
        final_res = subtract(number_1, number_2)
        return final_res

    elif operation == "*":
        final_res = multiply(number_1, number_2)
        return final_res

    elif operation == "/":
        final_res = divide(number_1, number_2)
        return final_res

    else:
        print("Invalid operation")

    ############################## Approach-2 ################################

#     operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

number_1 = float(input("Enter the number: "))
flag = True

while flag:
    print("Select the operator:\n + \n - \n * \n / \n")
    operation = input()
    number_2 = float(input("Enter the next number: "))
    output_ = calc(number_1, number_2, operation)
    print(f"{number_1} {operation} {number_2} = {output_}")

    choose_ = input("Type 'yes' to move further with the current result or 'no' for new calculation \n")

    if choose_ == "yes":
        # number_2 = int(input("Enter the number: "))
        number_1 = output_

    elif choose_ == "no":
        clear()
        number_1 = float(input("Enter the number: "))

    else:
        print("Good Bye")
        flag = False
    
    # print(f"{number_1} {operation} = {output_}")

# num1 = int(input("Enter the first number: "))
# for symbol in operations:
#     print(symbol)
# choose_operation = input("Pick the operation")
# num2 = int(input("Enter the second number: "))

# calc_function = operations[choose_operation]
# ans = calc_function(num1, num2)