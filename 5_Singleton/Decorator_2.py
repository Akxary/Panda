def singleton(class_):
    # instances = {}
    instance = None

    def get_instance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = class_(*args, **kwargs)
        return instance
        # if class_ not in instances:
        #     instances[class_] = class_(*args,**kwargs)
        # return instances[class_]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)