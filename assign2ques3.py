class Animal:
    """Represents an animal.
        Attributes:
            name (str): The name of the animal.
            type (str): The type of the animal."""
    def __init__(self, name, type):
        """Initializes an Animal object with a name and a type."""
        self.type = type
        self.name = name

    def speak(self):
        """method for making the animal speak."""
        pass

class Dog(Animal):
    """Represents a dog, inheriting from Animal.
        Attributes:
            breed (str): The breed of the dog."""
    def __init__(self, name, type, breed):
        """Initializes a Dog object with a name, type, and breed."""
        super().__init__(name, type)
        self.breed = breed

    def speak(self):
        """Makes the dog bark."""
        print("Woof!")

class Cat(Animal):
    """Represents a cat, inheriting from Animal.
        Attributes:
            color (str): The color of the cat."""
    def __init__(self, name, type, color):
        """Initializes a Cat object with a name, type, and color."""
        super().__init__(name, type)
        self.color = color

    def speak(self):
        """Makes the cat meow."""
        print("Meow!")

def main():
    """Entry point of the program."""
    dog1 = Dog("Misha", "Dog", "Husky")
    cat1 = Cat("Sizz", "Cat", "Black")

    print("Dog:")
    print("Name:", dog1.name)
    print("Species:", dog1.type)
    print("Breed:", dog1.breed)
    print("Sound:", end=" ")
    dog1.speak()

    print("\n")

    print("Cat:")
    print("Name:", cat1.name)
    print("Species:", cat1.type)
    print("Color:", cat1.color)
    print("Sound:", end=" ")
    cat1.speak()

if __name__ == "__main__":
    main()
