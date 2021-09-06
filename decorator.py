def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')

    return wrapper


@decorator_function
def hello_world():
    print('Hello world!')


hello_world()


##########
# Здесь мы создаём декоратор, замеряющий время выполнения функции.
# Далее мы используем его на функции, которая делает GET-запрос к главной странице Google.
# Чтобы измерить скорость, мы сначала сохраняем время перед выполнением обёрнутой функции,
# выполняем её, снова сохраняем текущее время и вычитаем из него начальное.
def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)



