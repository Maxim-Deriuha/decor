# Используйте ключевое слово As для отлова определенных типов исключений.
try:
    f = open("no-file")
except IOError as err:
    print("Error:", err)
    print("Code:", err.errno)

# Здесь мы приводим конкретный тип исключения, а не общий тип.
# И мы также используем опцию args для вывода неверных аргументов, если они есть.
# Давайте посмотрим на приведенный ниже пример.
try:
    raise ValueError('Testing exceptions: The input is in incorrect order', 'one', 'two', 'four')
except ValueError as err:
    print(err.args)

# Как пропустить ошибки и продолжить выполнение
try:
    assert False
except AssertionError:
    pass
print('Welcome to Prometheus!!!')

# IOError - происходит при ошибках файловой системы, например, если файл не открывается.
# ImportError - Если модуль Python не может быть загружен или не найден.
# ValueError - происходит, если функция получает аргумент правильного типа, но не подходящего значения.
# KeyboardInterrupt - когда пользователь вводит ключ прерывания (т.е. Control-C или Del в консоли)
# EOFError - Возникает, если входные функции (input() / raw_input()) попадают в условие конца файла (EOF),
# но без чтения каких-либо данных.


