# Function to generate a list of prime numbers within a given range
def generate_primes(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in range(start, end + 1) if is_prime(num)]

# Function to flatten a nested list using recursion
def flatten_nested_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_nested_list(element))
        else:
            flat_list.append(element)
    return flat_list

# Function to find the second largest element from a list without using built-in functions
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for second largest
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest, largest = largest, num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None

# Task queue management using a list
class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)
        print(f"Task '{task}' added to the queue.")

    def remove_task(self):
        if self.queue:
            task = self.queue.pop(0)
            print(f"Task '{task}' removed from the queue.")
            return task
        else:
            print("No tasks in the queue to remove.")
            return None

    def process_tasks(self):
        print("\nProcessing tasks:")
        while self.queue:
            task = self.remove_task()
            print(f"Processing task: {task}")

# Main program to demonstrate the functionality
if __name__ == "__main__":
    # 1. Generate a list of prime numbers within a range
    start, end = 10, 50
    print("Prime numbers between", start, "and", end, ":", generate_primes(start, end))
    
    # 2. Flatten a nested list using recursion
    nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
    print("\nOriginal Nested List:", nested_list)
    print("Flattened List:", flatten_nested_list(nested_list))
    
    # 3. Find the second largest element in a list
    numbers = [10, 20, 4, 45, 99, 45, 50]
    print("\nList of Numbers:", numbers)
    print("Second Largest Element:", find_second_largest(numbers))
    
    # 4. Task queue management using a list
    print("\nTask Queue Management:")
    task_queue = TaskQueue()
    task_queue.add_task("Task 1")
    task_queue.add_task("Task 2")
    task_queue.add_task("Task 3")
    task_queue.process_tasks()