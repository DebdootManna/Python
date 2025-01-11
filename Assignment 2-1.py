from collections import Counter

# Function to remove duplicates from a tuple
def remove_duplicates(input_tuple):
    return tuple(set(input_tuple))

# Function to create a list of tuples representing students and sort by marks
def sort_students_by_marks(student_data):
    return sorted(student_data, key=lambda x: x[1], reverse=True)

# Function to count the frequency of elements in a tuple using Counter
def count_frequency(input_tuple):
    return Counter(input_tuple)

# Function to implement a tuple-based record system and search operations
def search_record(records, search_id=None, search_name=None):
    if search_id:
        result = [record for record in records if record[0] == search_id]
    elif search_name:
        result = [record for record in records if record[1].lower() == search_name.lower()]
    else:
        result = []
    return result

# Main program to demonstrate the functionality
if __name__ == "__main__":
    # 1. Removing duplicates from a tuple
    input_tuple = (1, 2, 3, 2, 1, 4, 5, 3, 6)
    print("Original Tuple:", input_tuple)
    print("Tuple after removing duplicates:", remove_duplicates(input_tuple))
    
    # 2. List of tuples representing student names and marks
    students = [("Alice", 85), ("Bob", 90), ("Charlie", 75), ("David", 90), ("Eva", 95)]
    print("\nOriginal Student Data:", students)
    sorted_students = sort_students_by_marks(students)
    print("Sorted Student Data by Marks (Descending):", sorted_students)
    
    # 3. Counting the frequency of elements in a tuple
    frequency_tuple = (1, 2, 3, 2, 1, 2, 4, 3, 1)
    print("\nTuple for Frequency Count:", frequency_tuple)
    print("Frequency Count:", count_frequency(frequency_tuple))
    
    # 4. Tuple-based record system
    records = [
        (101, "Alice", 85),
        (102, "Bob", 90),
        (103, "Charlie", 75),
        (104, "David", 90),
        (105, "Eva", 95)
    ]
    print("\nRecords:", records)
    # Search by ID
    search_id = 102
    print(f"Search Result for ID {search_id}:", search_record(records, search_id=search_id))
    # Search by Name
    search_name = "Eva"
    print(f"Search Result for Name '{search_name}':", search_record(records, search_name=search_name))