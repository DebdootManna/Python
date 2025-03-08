import math

# Shape superclass to demonstrate polymorphism
class Shape:
    def __init__(self, name="Shape"):
        self.name = name
    
    def calculate_area(self):
        """Base method to calculate area of a shape"""
        return 0
    
    def __str__(self):
        return f"{self.name} with area: {self.calculate_area()}"

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def calculate_area(self):
        """Override area calculation for circle"""
        return math.pi * self.radius ** 2

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def calculate_area(self):
        """Override area calculation for rectangle"""
        return self.length * self.width

# Book class to demonstrate encapsulation
class Book:
    def __init__(self, title, author, isbn):
        # Private attributes using double underscore
        self.__title = title
        self.__author = author
        self.__isbn = isbn
    
    # Getter methods
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    # Setter methods
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def set_isbn(self, isbn):
        if len(isbn) == 13 or len(isbn) == 10:  # Basic validation for ISBN
            self.__isbn = isbn
        else:
            print("Invalid ISBN format")
    
    def __str__(self):
        return f"Book: {self.__title} by {self.__author}, ISBN: {self.__isbn}"


# Test code to demonstrate the classes
if __name__ == "__main__":
    # Polymorphism demonstration
    print("POLYMORPHISM DEMONSTRATION")
    shapes = [Circle(5), Rectangle(4, 6), Shape()]
    
    for shape in shapes:
        print(shape)
    
    # Encapsulation demonstration
    print("\nENCAPSULATION DEMONSTRATION")
    book = Book("Python Programming", "John Smith", "9781234567890")
    print(book)
    
    # Accessing private attributes through getter methods
    print(f"Title: {book.get_title()}")
    print(f"Author: {book.get_author()}")
    print(f"ISBN: {book.get_isbn()}")
    
    # Modifying private attributes through setter methods
    book.set_title("Advanced Python Programming")
    book.set_author("Jane Doe")
    book.set_isbn("1234567891012") 
    print("\nAfter modification:")
    print(book)