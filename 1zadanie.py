#Вычислить сумму цифр случайного трехзначного числа.
import random

a = random.randint(100, 999)
print('Случайное число: ' , a)
c = a % 10
a = a // 10
b = a % 10
n = a // 10
print('Сумма = ', c + b + n)