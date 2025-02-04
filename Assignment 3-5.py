def add_key_value(dictionary, key, value):
    dictionary[key] = value

def update_key_value(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value
    else:
        print("Key not found")

def delete_key_value(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        print("Key not found")

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

def display_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def main():
    my_dict = {}
    while True:
        print("\nDictionary Operations")
        print("1. Add Key-Value")
        print("2. Update Key-Value")
        print("3. Delete Key-Value")
        print("4. Merge Dictionaries")
        print("5. Display Dictionary")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "6":
            print("Exiting the dictionary operations program. Goodbye!")
            break

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            add_key_value(my_dict, key, value)
        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter new value: ")
            update_key_value(my_dict, key, value)
        elif choice == "3":
            key = input("Enter key to delete: ")
            delete_key_value(my_dict, key)
        elif choice == "4":
            new_dict = {}
            while True:
                key = input("Enter key for new dictionary (or 'done' to finish): ")
                if key == "done":
                    break
                value = input(f"Enter value for {key}: ")
                new_dict[key] = value
            my_dict = merge_dictionaries(my_dict, new_dict)
        elif choice == "5":
            display_dictionary(my_dict)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()