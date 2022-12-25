class Singleton(type):
    # _instances = {}
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instance
        # if cls not in cls._instances:
        #     cls._instances[cls] = super(5_Singleton, cls).__call__(*args, **kwargs)
        # return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1==d2)