#Задание на высокосный год
year = int(input("Введите год: "))
if year % 4 != 0:
    print("Год обычный!")
elif  year % 100 == 0:
    if year % 400 == 0:
        print("Год высокосный!")
    else:
        print("Год обычный!")
else:
    print("Год высокосный!")