class BasicStudent:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # list of numeric grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")


class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


if __name__ == "__main__":
    print("---- Testing BasicStudent ----")
    student1 = BasicStudent("Alice", 20, [88, 92, 79])
    student1.display_info()
    print("\n---- Testing BankAccount ----")
    account1 = BankAccount("123456789", 500.0, "Checking")
    account1.display_info()
    account1.deposit(100)
    account1.withdraw(50)
    print("\n---- Testing Student (inherits from Person) ----")
    student2 = Student("Bob", 21, "S12345")
    student2.display_info()