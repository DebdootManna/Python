# 1. Define a simple function that takes inputs and returns an output.
def add(a, b):
    return a + b

result = add(3, 5)
print("1. Simple function output:", result)  # Output: 8

# 2. Define a function with positional, keyword, default, and variable-length arguments.
def example_function(a, b, c=10, *args, **kwargs):
    print("\n2. Function with various arguments:")
    print(f"Positional: a={a}, b={b}")
    print(f"Default: c={c}")
    print(f"Variable-length positional (args): {args}")
    print(f"Variable-length keyword (kwargs): {kwargs}")

example_function(1, 2, 3, 4, 5, name="Alice", age=25)

# 3. Define a function that returns multiple values using a tuple.
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

min_val, max_val, avg_val = get_stats([10, 20, 30, 40])
print("\n3. Function returning multiple values:", min_val, max_val, avg_val)  # Output: 10 40 25.0

# 4. Define an anonymous function using the `lambda` keyword.
square = lambda x: x ** 2
print("\n4. Lambda function output:", square(5))  # Output: 25

# 5. Define a function inside another function.
def outer_function():
    def inner_function():
        return "Hello from inner function"
    return inner_function()

print("\n5. Nested function output:", outer_function())  # Output: Hello from inner function

# 6. Create and use decorators to modify the behavior of functions.
def my_decorator(func):
    def wrapper():
        print("\n6. Decorator output:")
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 7. Define a function that calls itself to solve a problem recursively.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\n7. Recursive function output:", factorial(5))  # Output: 120

# 8. Define functions that take other functions as arguments or return functions as results.
def apply_function(func, value):
    return func(value)

def multiply_by_two(x):
    return x * 2

print("\n8. Function as argument output:", apply_function(multiply_by_two, 5))  # Output: 10

# 9. Add docstrings to functions to document their purpose and usage.
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

print("\n9. Docstring output:", add.__doc__)

# 10. Use type annotations to specify the expected types of function arguments and return values.
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

print("\n10. Type annotation output:", greet("Alice", 25))