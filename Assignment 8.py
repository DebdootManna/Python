# Part 1: Custom Exception
print("\n--- Part 1: Custom Exception ---")

class InvalidAgeError(Exception):
    """Custom exception for invalid age inputs"""
    pass

def verify_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120")
    return True

# Using the custom exception
try:
    age = int(input("Enter your age: "))
    verify_age(age)
    print(f"Age {age} is valid")
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a numeric value for age")

# Part 2: Handling IndexError
print("\n--- Part 2: Handling IndexError ---")

my_list = [10, 20, 30, 40, 50]
print(f"List: {my_list}")
print(f"Valid indices: 0 to {len(my_list) - 1}")

while True:
    try:
        index = int(input("Enter an index to access an element: "))
        element = my_list[index]
        print(f"Value at index {index} is: {element}")
        break
    except IndexError:
        print(f"Error: Index out of range. Please enter a valid index (0-{len(my_list) - 1})")
    except ValueError:
        print("Error: Please enter a numeric value for the index")

# Part 3: Handling ValueError during string to int conversion
print("\n--- Part 3: Handling ValueError in Conversion ---")

while True:
    try:
        user_input = input("Enter a number to convert to integer: ")
        number = int(user_input)
        print(f"Successfully converted '{user_input}' to integer: {number}")
        break
    except ValueError:
        print(f"Error: '{user_input}' is not a valid number. Please enter a valid integer.")