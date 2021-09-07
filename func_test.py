# В переменной kwargs у нас хранится словарь, с которым мы, опять-таки, можем делать все, что нам заблагорассудится.
def func(**kwargs):
    return kwargs


print(func(a=1, b=2, c=3))


# Как видно из примера, args - это кортеж из всех переданных аргументов функции,
# и с переменной можно работать также, как и с кортежем.
def func1(*args):
    return args


print(func1(1, 2, 3, 'abc'))

func2 = lambda x, y: x + y
print(func2(1, 2))