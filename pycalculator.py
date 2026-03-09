def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


def get_operation() -> str:
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input("Choose operation (+, -, *, / ): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operation, please choose one of +, -, *, /")


def main() -> None:
    print("Simple Calculator")
    print("-----------------")

    while True:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        op = get_operation()

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Unexpected operation.")
                continue

            print(f"Result: {a} {op} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Do another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

