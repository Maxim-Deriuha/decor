def decorator(func):
    return 'sumit'


@decorator
def hello_world():
    return 'hello world'


a = hello_world
print(a)


