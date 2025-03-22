def divide_numbers(a, b):
    try:
        # This code might raise exceptions
        result = a / b
        print(f"Result of {a} / {b} = {result}")
        
        # This demonstrates accessing a non-existent list element
        my_list = [1, 2, 3]
        print(f"List element at index 10: {my_list[10]}")
        
    except ZeroDivisionError as e:
        # Handle division by zero specifically
        print(f"Error: Division by zero is not allowed! ({e})")
        
    except IndexError as e:
        # Handle index out of range errors
        print(f"Error: Invalid list index! ({e})")
        
    except Exception as e:
        # Catch any other exceptions that weren't specifically handled
        print(f"Unexpected error occurred: {e}")
        
    else:
        # This block runs only if no exceptions were raised in the try block
        print("No exceptions were raised! Everything worked perfectly.")
        
    finally:
        # This block always runs, regardless of whether exceptions occurred
        print("This is the finally block - it always executes")


# Example 1: No exceptions (won't reach the else block due to IndexError)
print("\nExample 1:")
divide_numbers(10, 2)

# Example 2: Handling ZeroDivisionError
print("\nExample 2:")
divide_numbers(10, 0)

# Example 3: Manually raising an exception
print("\nExample 3:")
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is {age}")
except ValueError as e:
    print(f"Caught an error: {e}")