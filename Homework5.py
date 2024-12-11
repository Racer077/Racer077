#№1#
import math
def find_min_angle_point(x1, x2, y1, y2, z1, z2):
    angle_x = math.atan2(x2, x1)
    angle_y = math.atan2(y2, y1)
    angle_z = math.atan2(z2, z1)
    min_angle_point = min([(angle_x, x1, x2), (angle_y, y1, y2), (angle_z, z1, z2)], key=lambda x: x[0])
    return min_angle_point[1:]
x1, x2 = 1, 2
y1, y2 = 3, 4
z1, z2 = 5, 6
print(find_min_angle_point(x1, x2, y1, y2, z1, z2))
#№2#
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def find_palindrome_primes(n):
    palindrome_primes = []
    for i in range(2, n + 1):
       if is_palindrome(i) and is_prime(i):
            palindrome_primes.append(i)
    return palindrome_primes
n = 100
print(find_palindrome_primes(n))