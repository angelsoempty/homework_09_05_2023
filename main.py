class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18
person1 = Person("Саша", 25)
print(person1.is_adult())

person2 = Person('Олександр', 16)
print(person2.is_adult())