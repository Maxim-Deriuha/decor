# Множества — неупорядоченная и не индексируемая последовательность. В Python множества пишутся в фигурных скобках.
# Создание множества:
this_set = {"set", "list", "tuple"}
print(this_set)

# Множество хранит только уникальные элементы:
this_set = {"set", "list", "tuple", "list"}
print(this_set)

# for
for x in this_set:
    print(x)

# Чтобы добавить один элемент в set используйте метод add().
# Чтобы добавить больше одного — метод update().
this_set.add("dict")
print(this_set)

this_set.update(["dict",  "class",  "int"])
print(this_set)

# Чтобы определить сколько элементов есть в наборе, воспользуйтесь методом len().
print(len(this_set))

# Удаление элементов
this_set = {"set", "list", "tuple"}
this_set.remove("list")
print(this_set)

this_set.discard("set")
print(this_set)

this_set.pop()
print(this_set)

this_set.clear()
print(this_set)

this_set = {"set", "list", "tuple"}
del this_set











