#Найти самое длинное слово в строке.

a = str(input('Введите строку: '))
b = (a.split())

print(max(b, key=len))