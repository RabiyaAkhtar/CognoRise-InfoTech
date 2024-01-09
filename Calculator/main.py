class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"


def main():
    calculator = Calculator()
    continue_calculation = True

    while continue_calculation:
        try:
            print()
            print("LET'S CALCULATE!\n")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            if operation == "+":
                result = Calculator.add(num1, num2)
            elif operation == "-":
                result = calculator.subtract(num1, num2)
            elif operation == "*":
                result = calculator.multiply(num1, num2)
            elif operation == "/":
                result = calculator.divide(num1, num2)
            else:
                result = "Invalid operation"

            print(f"Result: {result}")

        except ValueError:
            print("\nInvalid input. Please enter valid numbers.")

        choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()

        while choice not in ['yes', 'no']:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()

        continue_calculation = choice == 'yes'


if __name__ == "__main__":
    main()
