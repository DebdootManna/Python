def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    while True:
        print("\nFibonacci Sequence Generator")
        print("1. Generate Sequence")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "2":
            print("Exiting the Fibonacci generator. Goodbye!")
            break

        terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        print("Fibonacci sequence:", fibonacci(terms))

if __name__ == "__main__":
    main()