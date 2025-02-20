def calculator():
    print("Select options")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")

    choice = input("Enter your number: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if choice == '1':
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            result = num1 * num2
            print("Result:", result)
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
                print("Result:", result)
    else:
        print("Invalid choice")

if __name__ == '__main__':
    calculator()