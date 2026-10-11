class Dog:
    def __init__(self, name, breed="None"):
        self.name = name
        self.breed = breed


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


jerry = Dog(name="Jerry", breed="Labrador")

print(jerry.name)  # Jerry

dog = Dog(name="Buddy", breed="Golden Retriever")

print(dog.name)  # Buddy


class Fish:
    def __init__(self, name):
        self.name = name


jerry = Dog(name="jerry")
