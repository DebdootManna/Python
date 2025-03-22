import os

def file_operations_demo():
    # 1. Opening files in different modes
    print("1. Opening files in different modes:")
    
    # Write mode ('w') - creates new file or overwrites existing
    with open('example.txt', 'w') as file:
        file.write("This is line 1.\n")
        file.write("This is line 2.\n")
    print("   File created in write mode.")
    
    # Read mode ('r') - default mode
    with open('example.txt', 'r') as file:
        # Read entire file content
        content = file.read()
        print(f"   Read entire file:\n{content}")
    
    # Reading line by line
    with open('example.txt', 'r') as file:
        # Read first line
        first_line = file.readline()
        print(f"   First line: {first_line.strip()}")
        
        # Read next line
        second_line = file.readline()
        print(f"   Second line: {second_line.strip()}")
    
    # Reading all lines into a list
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        print(f"   All lines as list: {lines}")
    
    # Append mode ('a') - adds to end of file
    with open('example.txt', 'a') as file:
        file.write("This is line 3 (appended).\n")
    print("   Content appended to file.")
    
    # Writing multiple lines at once
    with open('example.txt', 'a') as file:
        lines_to_add = ["Line 4 from list.\n", "Line 5 from list.\n"]
        file.writelines(lines_to_add)
    print("   Multiple lines appended using writelines().")
    
    # 2. File positioning operations
    print("\n2. File positioning operations:")
    with open('example.txt', 'r') as file:
        # Get current position
        position = file.tell()
        print(f"   Initial position: {position}")
        
        # Read some content
        file.read(10)
        position = file.tell()
        print(f"   Position after reading 10 chars: {position}")
        
        # Seek to specific position
        file.seek(0)  # Go back to beginning
        print(f"   After seek(0), position: {file.tell()}")
        
        # Seek from current position
        file.seek(5, 1)  # Move 5 chars forward from current position
        print(f"   After seek(5, 1), position: {file.tell()}")
    
    # 3. File management operations
    print("\n3. File management operations:")
    
    # Check if file exists
    file_exists = os.path.exists('example.txt')
    print(f"   Does example.txt exist? {file_exists}")
    
    # Get file information
    file_size = os.path.getsize('example.txt')
    print(f"   Size of example.txt: {file_size} bytes")
    
    # Rename a file
    os.rename('example.txt', 'renamed_example.txt')
    print("   File renamed to 'renamed_example.txt'")
    
    # Create a copy to demonstrate removal
    with open('to_be_deleted.txt', 'w') as file:
        file.write("This file will be deleted.")
    
    # Remove a file
    os.remove('to_be_deleted.txt')
    print("   File 'to_be_deleted.txt' removed")
    
    # Show current directory path
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(f"   Current directory: {current_dir}")
    
    print("\nFile operations demo completed!")

def file_operations_demo():
    # ...existing code...
    print("\nFile operations demo completed!")

# Conclusion section
def conclusion():
    print("\n----- CONCLUSION -----")
    print("This practical demonstrated Python's comprehensive file handling capabilities:")
    print("1. File access modes: write ('w'), read ('r'), and append ('a')")
    print("2. Reading techniques: read(), readline(), readlines()")
    print("3. Writing operations: write() and writelines()")
    print("4. File positioning with tell() and seek()")
    print("5. File management using os module (exists, getsize, rename, remove)")
    print("\nKey takeaways:")
    print("- The 'with' statement ensures proper file closing regardless of exceptions")
    print("- Different file modes serve specific purposes (creating, reading, appending)")
    print("- Python provides versatile positioning methods for navigating file content")
    print("- The os module extends file handling beyond basic I/O operations")
    print("\nThese file operations are fundamental for data persistence, configuration")
    print("management, logging, and other practical programming applications.")
    print("-----------------------")

if __name__ == "__main__":
    file_operations_demo()
    conclusion()