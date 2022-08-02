#Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.


try:
    a = int(input('Введите 1 число: '))
    b = int(input('Введите 2 число: '))
    c = a / b
except ValueError:
    print('Ошибка ввода чисел!')
except ZeroDivisionError:
    print('Делить на 0 нельзя!')
else:
    if a != 0 and b != 0:
        print(c)
    else:
        a = int(input('Введите 1 число еще раз: '))
        b = int(input('Введите 2 число еще раз: '))
        print(a / b)