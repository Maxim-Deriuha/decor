import collections
import types


def squares(start, stop):
    for i in range(start, stop):
        yield i * i


a, b = 1, 3
generator = squares(a, b)

generator1 = (i * i for i in range(a, b))
print(type(generator))
print(type(generator1))


class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self): return self

    def next(self):  # __next__ in Python 3
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


iterator = Squares(a, b)
print(type(iterator))


def a_function():
    """when called, returns generator object"""
    yield


print(type(a_function()))


# print(issubclass(types.GeneratorType, collections.Iterator))


def b_function():
    """just a function definition with yield in it"""
    yield


print(type(b_function))
b_generator = a_function()
print(type(b_generator))

print(all(isinstance(iter(element), collections.Iterator) for element in (
    (), [], {}, set(), frozenset(), '', b'', bytearray(), range(0), memoryview(b''))))


class Yes(collections.Iterator):

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration

    __next__ = next  # Python 3 compatibility


print(type(Yes))


def yes(stop):
    for _ in range(stop):
        yield 'yes'


print(type(yes(5)))
