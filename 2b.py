# 1. Create a list of integers, strings, and mixed data types
int_list = [1, 2, 3, 4, 5]
string_list = ["apple", "banana", "cherry"]
mixed_list = [1, "apple", 3.14, True]

print("Integer List:", int_list)
print("String List:", string_list)
print("Mixed List:", mixed_list)

# 2. Access elements using indices, perform slicing, and update list elements
print("\nAccessing and updating:")
print("int_list[1]:", int_list[1])  # Access element at index 1
print("string_list[-1]:", string_list[-1])  # Access last element

# Slicing
print("int_list[1:4]:", int_list[1:4])  # Slice elements

# Updating elements
mixed_list[1] = "orange"
print("Updated mixed_list:", mixed_list)

# 3. Add and remove elements using append(), insert(), remove(), and pop()
print("\nAdding and removing elements:")
int_list.append(6)
print("After append:", int_list)

int_list.insert(2, 10)
print("After insert at index 2:", int_list)

int_list.remove(10)  # Removes the first occurrence of 10
print("After remove(10):", int_list)

popped_element = int_list.pop()  # Pops the last element
print("After pop(), popped element:", popped_element)
print("After pop:", int_list)

# 4. Concatenate and repeat lists using operators
concat_list = int_list + string_list
print("\nConcatenated List:", concat_list)

repeated_list = string_list * 2
print("Repeated List:", repeated_list)

# 5. Create a list of squares of the first 10 natural numbers using list comprehension
squares = [x**2 for x in range(1, 11)]
print("\nSquares of the first 10 natural numbers:", squares)

# 6. Filter even numbers from a list using list comprehension
numbers = list(range(1, 21))
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# 7. Demonstrate sorting, reversing, and copying lists
print("\nSorting, reversing, and copying:")
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(unsorted_list)  # Sorting without modifying original
print("Sorted List:", sorted_list)

unsorted_list.sort()  # Sorting and modifying the original
print("After sort():", unsorted_list)

unsorted_list.reverse()  # Reverse the list
print("After reverse():", unsorted_list)

copied_list = unsorted_list.copy()  # Copy the list
print("Copied List:", copied_list)

# 8. Write a program to remove duplicates from a list
duplicate_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_list = list(set(duplicate_list))  # Remove duplicates using set
print("\nList with duplicates removed:", unique_list)

# Optional: Maintain order while removing duplicates
unique_list_ordered = []
for item in duplicate_list:
    if item not in unique_list_ordered:
        unique_list_ordered.append(item)
print("List with duplicates removed (order maintained):", unique_list_ordered)