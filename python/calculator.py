def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    """Safely prompt the user for a numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    print("Simple Python Calculator")
    print("Available operations: +, -, *, /")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        op = input("Choose an operation (+, -, *, /) or 'q' to quit: ").strip()

        if op.lower() == 'q':
            print("Goodbye!")
            break

        if op not in operations:
            print("Invalid operation. Please select +, -, *, or /.\n")
            continue

        num1_input = input("Enter first number (or 'q' to quit): ").strip()
        if num1_input.lower() == 'q':
            break
        try:
            num1 = float(num1_input)
        except ValueError:
            print("Invalid number. Returning to start.\n")
            continue

        num2_input = input("Enter second number (or 'q' to quit): ").strip()
        if num2_input.lower() == 'q':
            break
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Invalid number. Returning to start.\n")
            continue

        try:
            result = operations[op](num1, num2)
            # Display whole numbers as integers (e.g., 5 instead of 5.0)
            if result.is_integer():
                result = int(result)
            print(f"Result: {num1} {op} {num2} = {result}\n")
        except ZeroDivisionError as err:
            print(f"Error: {err}\n")

if __name__ == "__main__":
    calculator()