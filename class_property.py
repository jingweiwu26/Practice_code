import functools


class MetaTrace(type):
    @property
    def service_type_dict(cls):
        if cls._service_type_dict is None:
            cls._service_type_dict = {'a': 1}
            cls.count+=1
        return cls._service_type_dict


class Trace(object, metaclass=MetaTrace):
    _service_type_dict = None
    count=0

    @classmethod
    def trace_a(cls, f):
        @functools.wraps(f)
        def wrapper(*args):
            res = f(*args)
            print(cls.service_type_dict)
            print(cls.count)
            return res
        return wrapper

@Trace.trace_a
def func():
    print('haha')


if __name__ == '__main__':
    for i in range(10):
        func()



