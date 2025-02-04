def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    while True:
        print("\nEven Number Filter")
        print("1. Filter Even Numbers")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "2":
            print("Exiting the even number filter. Goodbye!")
            break

        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        print("Even numbers:", filter_even_numbers(numbers))

if __name__ == "__main__":
    main()