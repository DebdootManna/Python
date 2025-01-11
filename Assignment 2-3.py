# 1. Count the frequency of each word in a string and store it in a dictionary
def count_word_frequency(input_string):
    words = input_string.split()
    frequency = {}
    for word in words:
        word = word.lower().strip(",.!?")  # Normalize words (lowercase and remove punctuation)
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# 2. Simple phonebook application
class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact '{name}' added with number {number}.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found.")

# 3. Filter students who scored more than a specific mark
def filter_students_by_grade(students, min_marks):
    return {name: grade for name, grade in students.items() if grade > min_marks}

# 4. Convert list of tuples (key-value pairs) into a dictionary and vice versa
def list_to_dict(tuple_list):
    return dict(tuple_list)

def dict_to_list(dictionary):
    return list(dictionary.items())

# Main program to demonstrate functionality
if __name__ == "__main__":
    # 1. Word frequency count
    input_string = "Hello, world! Hello everyone. Welcome to the world of Python."
    print("Input String:", input_string)
    word_freq = count_word_frequency(input_string)
    print("\nWord Frequency:", word_freq)

    # 2. Phonebook application
    print("\nPhonebook Application:")
    phonebook = Phonebook()
    phonebook.add_contact("Alice", "123-456-7890")
    phonebook.add_contact("Bob", "987-654-3210")
    print("Search for 'Alice':", phonebook.search_contact("Alice"))
    phonebook.delete_contact("Bob")
    print("Search for 'Bob':", phonebook.search_contact("Bob"))

    # 3. Filter students by grades
    students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88, "Eva": 95}
    min_marks = 80
    print("\nOriginal Student Grades:", students)
    filtered_students = filter_students_by_grade(students, min_marks)
    print(f"Students scoring more than {min_marks}:", filtered_students)

    # 4. Convert between dictionary and list of tuples
    tuple_list = [("name", "Alice"), ("age", 25), ("city", "New York")]
    print("\nList of Tuples:", tuple_list)
    converted_dict = list_to_dict(tuple_list)
    print("Converted Dictionary:", converted_dict)
    converted_list = dict_to_list(converted_dict)
    print("Converted Back to List of Tuples:", converted_list)