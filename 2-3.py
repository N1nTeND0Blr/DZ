#Принадлежит ли точка кругу
x = int(input('x: '))
y = int(input('y: '))
r = int(input('r: '))


import math


g = math.sqrt(x ** 2 + y ** 2)


if g <= r:
    print('Точка в круге')
else:
    print('Точка вне круга')