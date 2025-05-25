# Calculator

def add(n1: float, n2: float):
    return n1 + n2


def subtract(n1: float, n2: float):
    return n1 - n2


def multiply(n1: float, n2: float):
    return n1 * n2


def divide(n1: float, n2: float):
    return n1 / n2


display = """
    +
    -
    *
    /
    """

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

calculate = True
next_operation_flag = True
num1 = 0
while calculate:
    if next_operation_flag:
        num1 = float(input("What is the first number? : "))
    print(display)
    op_perform = str(input(f"Pick an operation "))
    num2 = float(input("What is the second number? : "))
    result = operations[op_perform](num1, num2)
    print(f"{str(float(num1))} {op_perform} {str(float(num2))} = {result}")
    next_cal = str(input(f"Type 'y' to continue calculation with {result} or press 'n' to start new calculation: "))
    if next_cal == 'y':
        num1 = result
        next_operation_flag = False
    else:
        next_operation_flag = True
        print("\n" * 100)
        continue
