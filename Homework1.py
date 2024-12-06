#№1#
import math
R = int(input())
a = 2*math.pi*R
b = math.pi*R**2
print(round(a, 2))
print(round(b, 2))
#№2#
x, y = 10, 55
print("x=", x, "y=", y)
print("x=", y, "y=", x)
#№3#
import math
L = tuple(input())
g = 9.81
T = 2 * math.pi * math.sqrt(L / g)
print(round(T, 2))

