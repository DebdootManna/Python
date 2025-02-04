def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    largest = smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

def main():
    while True:
        print("\nLargest and Smallest Number Finder")
        print("1. Find Largest and Smallest")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "2":
            print("Exiting the program. Goodbye!")
            break

        numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
        largest, smallest = find_largest_smallest(numbers)
        print("Largest:", largest)
        print("Smallest:", smallest)

if __name__ == "__main__":
    main()