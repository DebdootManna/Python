class timepass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        # print("The name is: ",self.name," and the age is ",self.age)
        print(f"Name: {self.name}, Age: {self.age}")

def main():
    anothertimepass = timepass("Debdoot Manna", 20)

    print("Initial Attributes was...")
    timepass.display

    print("Modified...!!")
    timepass.name = "Aryan"
    timepass.age = 69
    timepass.display

if __name__ == "__main__":
    main()