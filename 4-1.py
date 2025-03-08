print("Class functions")

class marks:
    def __init__(self,value):
        self.value = value

    def display(self):
        print("Marks: ", self.value)

    def update_value(self,new_value):
        self.value = new_value
        print("Updates Marks: ",self.value)

a1 = marks(100)
a1.display()
a1.update_value(90)
a1.display