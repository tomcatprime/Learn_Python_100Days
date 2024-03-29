from art import logo

def add(n1, n2):
    """add numbers"""
    return n1 + n2


def substract(n1, n2):
    """substract numbers"""
    return n1 - n2


def multiply(n1, n2):
    """multiply numbers"""
    return n1 * n2


def divide(n1, n2):
    """divide numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
    }

def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))

    for sumbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the live above: ")
        num2 = float(input("What's the second number: "))
        calculaction_function = operations[operation_symbol]
        answer = calculaction_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2}- = {answer}")
        if input(f"Type 'y'  to continue calculation with {answer}, or type 'n' to start a new calculation") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()


