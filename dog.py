class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
        
my_dog = Dog("Willi", 6)
your_dog = Dog("Jack", 8)

print(my_dog.name + " is my dog and " + your_dog.name + " is your dog.")
print("They are " + str(my_dog.age) + " and " + str(your_dog.age) + " years old respectivly.")
my_dog.sit()
your_dog.roll_over()
