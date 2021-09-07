# Используйте предложение else сразу после блока try-except.
# Предложение else будет получено, только если не сгенерировано исключение.
# Оператор else всегда должен предшествовать блокам except.
while True:
    x = int(input())

    try:
        result = 1 / x
    except:
        print("Error case")
        exit(0)
    else:
        print("Pass case")
        exit(1)
