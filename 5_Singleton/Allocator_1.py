import random


class Database:
    _instance = None

    def __init__(self):
        id_ = random.randint(1, 101)
        print(f'{id_ = }')
        print('Loading database from file')

    def __del__(self):
        Database._instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)