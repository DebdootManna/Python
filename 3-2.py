# 1. Iterate over a sequence (list, tuple, string, or range) using a `for` loop.
print("1. Iterating over a list:")
for item in [1, 2, 3, 4]:
    print(item)

print("\nIterating over a string:")
for char in "Python":
    print(char)

# 2. Repeat a block of code as long as a condition is true using a `while` loop.
print("\n2. While loop output:")
count = 0
while count < 5:
    print(count)
    count += 1

# 3. Use loops inside other loops to handle multi-dimensional data structures.
print("\n3. Nested loops output:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)

# 4. Use `break`, `continue`, and `pass` to control the flow of loops.
print("\n4. Break, continue, and pass output:")
for i in range(10):
    if i == 5:
        break  # Exit the loop
    if i % 2 == 0:
        continue  # Skip the rest of the loop body
    print(i)

# 5. Use the `enumerate` function to get both the index and value while iterating over a sequence.
print("\n5. Enumerate output:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 6. Use the `range` function to generate a sequence of numbers for iteration.
print("\n6. Range output:")
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# 7. Iterate over the key-value pairs of a dictionary using a `for` loop.
print("\n7. Dictionary iteration output:")
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 8. Use list comprehensions to create new lists by applying an expression to each item in an existing list.
print("\n8. List comprehension output:")
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]