import copy
# а как же добавление метода клонирования объекта в сам класс объекта?
# Вы считаете, что это нецелесообразно или почему здесь об этом ни слова?

class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address
    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} lives at {self.address}'

john = Person('John', Address('123 London Road', 'London', 'UK'))
# jane = john bad way
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '124 London Road'
print(john, jane, sep='\n')