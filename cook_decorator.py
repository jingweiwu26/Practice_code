from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        import ipdb;ipdb.set_trace()
        return partial(attach_wrapper, obj)
    import ipdb;ipdb.set_trace()
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Span!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(add(2,3))

    add.set_message('example')
    print(add(2,3))
    import ipdb;ipdb.set_trace()