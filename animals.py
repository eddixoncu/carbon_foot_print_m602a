class Animal:
    def __init__(self):
        pass

    def speak(self):
        print('I am an animal')


class Dog(Animal):
    def __init__(self):
        pass

    def speak(self):
        print('I am a dog')


anx = Animal()
anx.speak()
dog = Dog()
dog.speak()