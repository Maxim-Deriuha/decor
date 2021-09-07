num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)
itr = iter(num_list)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print('*******************************')


# Создание собственных итераторов

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration


s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)

print("***************")


def simple_generator(val):
    while val > 0:
        val -= 1
        yield 1


gen_iter = simple_generator(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))

