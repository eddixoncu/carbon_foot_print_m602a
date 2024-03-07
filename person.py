class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello my name is {self.name} and I am {self.age} years old.'

    def is_under_age(self):
        return self.age < 18


p = Person("Edde", 36)
greet = p.greet()
print(greet)

