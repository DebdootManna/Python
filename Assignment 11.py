def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        try:
            choice = int(input("Enter operation number (1/2/3/4): "))
            
            if choice not in [1, 2, 3, 4]:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
                
            another_calculation = input("Perform another calculation? (y/n): ")
            if another_calculation.lower() != 'y':
                break
                
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    calculator()