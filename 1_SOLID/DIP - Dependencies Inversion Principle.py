# Высокоуровневые модули не зависят от низкоуровневых, а зависят от абстракций
from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipsBrowser:
    @abstractmethod
    def find_all_children(self, name): pass

class Relationships(RelationshipsBrowser):
    def __init__(self):
        self.relations = []
    def add_parent_and_child (self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )
    # добавляем поиск в низкоуровневый модуль, чтобы не зависеть от способа хранения
    def find_all_children(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

# класс для пользователей высокого уровня
class Research:
    # def __init__(self, relationships):
    #     # обращаемся к низкоуровнему хранилищу и зависим от способа хранения
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')
    def __init__(self, browser: Relationships):
        for p in browser.find_all_children('John'):
            print(f'John has child called {p}')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)