# Python program to demonstrate
# use of class method and static method.

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18


if __name__ == '__main__':
    person1 = Person('mayank', 21)
    person2 = Person.from_birth_year('mayank', 1996)

    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.is_adult(22))
