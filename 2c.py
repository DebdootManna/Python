# 1. Create a dictionary to store key-value pairs
my_dict = {"name": "Alice", "age": 25, "profession": "Engineer"}
print("Dictionary:", my_dict)

# 2. Access, update, and delete dictionary elements using keys
print("\nAccessing elements:")
print("Name:", my_dict["name"])  # Access element by key

# Updating a value
my_dict["age"] = 26
print("Updated Dictionary:", my_dict)

# Deleting an element
del my_dict["profession"]
print("After deletion:", my_dict)

# 3. Use dictionary methods like keys(), values(), and items()
print("\nDictionary methods:")
print("Keys:", my_dict.keys())  # Returns all keys
print("Values:", my_dict.values())  # Returns all values
print("Items:", my_dict.items())  # Returns all key-value pairs as tuples

# 4. Add a new key-value pair and remove an existing key-value pair
my_dict["city"] = "New York"  # Add a new key-value pair
print("\nAfter adding a new key-value pair:", my_dict)

removed_value = my_dict.pop("city")  # Remove a key-value pair
print("After removing 'city':", my_dict)
print("Removed Value:", removed_value)

# 5. Create a nested dictionary to store student details
students = {
    "student1": {"name": "John", "age": 20, "marks": {"math": 85, "science": 90}},
    "student2": {"name": "Emily", "age": 22, "marks": {"math": 78, "science": 88}},
}
print("\nNested Dictionary (Students):", students)

# 6. Access and update elements in a nested dictionary
print("\nAccessing nested dictionary elements:")
print("Student1's Math Marks:", students["student1"]["marks"]["math"])  # Access nested element

# Updating a nested value
students["student2"]["marks"]["math"] = 80
print("Updated Nested Dictionary:", students)

# 7. Merge two dictionaries using update()
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # Merge dict2 into dict1, overwriting common keys
print("\nMerged Dictionary:", dict1)

# 8. Write a program to sort a dictionary based on its values
unsorted_dict = {"apple": 3, "banana": 1, "cherry": 2}
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print("\nSorted Dictionary (by values):", sorted_dict)