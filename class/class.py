# Создание класса
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# Функция init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Используем слова mysillyobject и abc вместо self:
    # Методы объектов
    def my_func(self):
        print("Привет, меня зовут " + self.name + ' мне ' + str(self.age))


p1 = Person("Максим", 21)
print(p1.name)
print(p1.age)
p1.my_func()

p1.age = 40
print(p1.age)

del p1.age

del p1
