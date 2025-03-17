import datetime
import math

# Basic arithmetic functions
def add(a, b):
    return a + b

def is_even(num):
    return num % 2 == 0

# Functions for shape operations and prime check
def calculate_area(shape, *dimensions):
    """
    Calculate area for:
      - circle: dimensions = (radius,)
      - rectangle: dimensions = (length, width)
      - triangle: dimensions = (base, height)
    """
    if shape.lower() == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle area requires 1 dimension (radius)")
        radius = dimensions[0]
        return math.pi * radius ** 2
    elif shape.lower() == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle area requires 2 dimensions (length, width)")
        length, width = dimensions
        return length * width
    elif shape.lower() == 'triangle':
        if len(dimensions) != 2:
            raise ValueError("Triangle area requires 2 dimensions (base, height)")
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # Print current date and time in a readable format.
    now = datetime.datetime.now()
    formatted_date = now.strftime("%A, %d %B %Y %I:%M:%S %p")
    print(f"Current Date and Time: {formatted_date}\n")

    # Use basic arithmetic functions
    a, b = 5, 3
    result = add(a, b)
    even_status = "even" if is_even(result) else "odd"
    print(f"Addition of {a} and {b} is {result}, which is {even_status}.\n")

    # Shape area calculations
    try:
        circle_area = calculate_area("circle", 4)
        rectangle_area = calculate_area("rectangle", 5, 6)
        triangle_area = calculate_area("triangle", 7, 8)

        print(f"Area of circle with radius 4: {circle_area:.2f}")
        print(f"Area of rectangle 5x6: {rectangle_area:.2f}")
        print(f"Area of triangle with base 7 and height 8: {triangle_area:.2f}")
    except ValueError as e:
        print(e)

    # Prime check
    number = 29
    prime_status = "prime" if is_prime(number) else "not prime"
    print(f"\nNumber {number} is {prime_status}.")

if __name__ == "__main__":
    main()