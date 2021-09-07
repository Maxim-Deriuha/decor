# На вход программе подается строка, состоящая из трех слов.
# Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

a = input().split()
for i in range(len(a)):
    if set(a[i]) != set(a[i-1]):
        print('NO')
        break
    else:
        print('YES')
        break
