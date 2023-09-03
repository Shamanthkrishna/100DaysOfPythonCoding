logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Add
def add(n1,n2):
    return n1+n2


# Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1*n2

# Divide
def divide(n1,n2):
    return n1/n2

operations={"+":add,
         "-":subtract,
         "*":multiply,
         "/":divide}

def calculator():
    print(logo)
    num1=float(input("What is the 1st number?  "))

    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        op_symbol=input("Select an operation: ")
        num2=float(input("What's the next number?  "))
        calculation_function= operations[op_symbol]
        result = calculation_function(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {result}")

        if input(f"Type y to continue with {result}, or type n to start new calculation: ") == "y":
            num1 = result
        else:
            calculator()

calculator() 