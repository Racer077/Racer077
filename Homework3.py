#№1#
a = int(input("Введите верхний предел: "))
if a > 100:
    print("Верхний предел не должен превышать 100")
else:
    sum = 0
    for i in range(1, a + 1):
        sum += i**3
        print("Сумма кубов натуральных чисел от 1 до", a, "включительно:", sum)
#№2#
print("1  2  3  4  5  6  7  8  9")
for i in range(1, 10):
    print(f"{i:2}", end="")
    for j in range(1, 10):
        b = i * j
        print(f"{b:3}", end=" ")
    print()