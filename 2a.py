# 1. Create tuples with different data types
int_tuple = (1, 2, 3, 4, 5)
float_tuple = (1.1, 2.2, 3.3)
string_tuple = ("apple", "banana", "cherry")
mixed_tuple = (1, "apple", 3.14, True)

print("Integer Tuple:", int_tuple)
print("Float Tuple:", float_tuple)
print("String Tuple:", string_tuple)
print("Mixed Tuple:", mixed_tuple)

# 2. Access tuple elements using positive and negative indices
print("\nAccessing elements:")
print("Positive Index (int_tuple[1]):", int_tuple[1])  # 2
print("Negative Index (string_tuple[-1]):", string_tuple[-1])  # "cherry"

# 3. Perform tuple slicing to extract specific portions
print("\nSlicing tuples:")
print("int_tuple[1:4]:", int_tuple[1:4])  # (2, 3, 4)
print("mixed_tuple[:3]:", mixed_tuple[:3])  # (1, "apple", 3.14)

# 4. Count occurrences and find the index of an element in a tuple
example_tuple = (1, 2, 3, 1, 1, 4)
print("\nCount and index:")
print("Count of 1 in example_tuple:", example_tuple.count(1))  # 3
print("Index of 3 in example_tuple:", example_tuple.index(3))  # 2

# 5. Use built-in functions with tuples
num_tuple = (10, 20, 30, 40)
print("\nBuilt-in functions:")
print("Length of num_tuple:", len(num_tuple))  # 4
print("Maximum in num_tuple:", max(num_tuple))  # 40
print("Minimum in num_tuple:", min(num_tuple))  # 10
print("Sum of num_tuple:", sum(num_tuple))  # 100

# 6. Count and print distinct elements from a tuple
example_tuple = (1, 2, 3, 1, 4, 4, 5)
distinct_elements = set(example_tuple)
print("\nDistinct elements:")
print("Distinct elements in example_tuple:", distinct_elements)

# 7. Convert a list to a tuple and vice versa
example_list = [10, 20, 30]
converted_tuple = tuple(example_list)
converted_list = list(converted_tuple)
print("\nConversions:")
print("List to Tuple:", converted_tuple)  # (10, 20, 30)
print("Tuple to List:", converted_list)  # [10, 20, 30]

# 8. Demonstrate unpacking of tuples into individual variables
person_tuple = ("Alice", 25, "Engineer")
name, age, profession = person_tuple
print("\nTuple unpacking:")
print(f"Name: {name}, Age: {age}, Profession: {profession}")