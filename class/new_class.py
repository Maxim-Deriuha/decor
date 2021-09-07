class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age

    def __del__(self):
        print(self.name, self.age, 'лет', "удален из памяти")

    def display_info(self):
        print("Привет, меня зовут", self.name, 'мне ', self.age, 'лет')
        if self.age > 18:
            print(self.name, "is student")
        else:
            print(self.name, 'is school')


class Auto:
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "едет со скоростью", speed, "км/ч")
        if speed > 50:
            print(self.name, 'превышает скорость по городу ')
        else:
            print(self.name, 'едет по правилам')

    def __del__(self):
        print(self.name, "удалена из памяти")
