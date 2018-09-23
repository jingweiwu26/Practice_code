class Singleton(type):
    def __init__(cls, name, base, dic):
        import ipdb;ipdb.set_trace()
        cls.__instance = None
        super().__init__(name, base, dic)

    def __call__(cls, *args, **kwargs):
        import ipdb;ipdb.set_trace()
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        import ipdb;ipdb.set_trace()
        print('Creating Spam')


###########
'''
class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print('-------------')
        print('Allocating memory for class', name)
        print(meta)
        print(bases)
        print(dct)
        return super().__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('-------------')
        print('Initialzing class', name)
        print(cls)
        print(dct)
        return super().__init__(name, bases, dct)

class MyKlass(metaclass=MyMeta):
    def foo(self, param):
        pass
    barattr = 2
'''
if __name__ == '__main__':
    a = Spam()