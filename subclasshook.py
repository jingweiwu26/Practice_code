import abc


class MockCache(object):
    pass


class Mockhaha(object):
    pass


def __mocksubclasshook__(kls, other_kls):
    if other_kls.__name__ == 'MockCache':
        return True
    return NotImplemented


def deco(kls):
    kls.__subclasshook__ = classmethod(__mocksubclasshook__)
    return kls


@deco
class Cache(object, metaclass=abc.ABCMeta):
    pass


if __name__ == '__main__':
    mc = MockCache()
    c = Cache()
    d = Mockhaha()

    print(isinstance(mc, Cache))
    print(isinstance(c, Cache))
    print(isinstance(d, Cache))
    print(Cache.__subclasscheck__(MockCache))