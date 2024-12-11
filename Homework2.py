#№1#
a = float(input())
b = float(input())
if b == 0:
    print("На ноль делить нельзя")
else:
    c = a/b
    print(c)
#№2#
a = float(input())
b = 0
if a > 20:
    b = round(a*0.35, 2)
c = a-b
print("Итоговая стоимость:", round(c, 2),
      "Cкидка:", b)
#№3#
a = int(input())
b = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
if 1 <= a <= 12:
    if 9 <= a <= 11:
        print(f'{b[a]}, осень')
    elif 3 <= a <= 5:
        print(f'{b[a]}, весна')
    elif 6 <= a <= 8:
        print(f'{b[a]}, лето')
    else:
        print(f'{b[a]}, зима')
else:
    print("Ошибка")

