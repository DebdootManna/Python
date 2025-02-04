def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        print("\nFactorial Calculator")
        print("1. Calculate Factorial")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "2":
            print("Exiting the factorial calculator. Goodbye!")
            break

        number = int(input("Enter a number to calculate its factorial: "))
        print("Factorial of", number, "is:", factorial(number))

if __name__ == "__main__":
    main()