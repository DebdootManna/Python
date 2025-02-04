def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def find_min(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

def find_average(lst):
    return find_sum(lst) / len(lst)

def main():
    while True:
        print("\nList Operations")
        print("1. Perform Operations")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "2":
            print("Exiting the list operations program. Goodbye!")
            break

        numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
        print("Max:", find_max(numbers))
        print("Min:", find_min(numbers))
        print("Sum:", find_sum(numbers))
        print("Average:", find_average(numbers))

if __name__ == "__main__":
    main()