#1#
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point3D(Point2D):
    __slots__ = ('_z',)
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z
    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, value):
        raise AttributeError("Нельзя изменить значение z")
if __name__ == '__main__':
    pt3 = Point3D(10, 20, 30)
    print(f"x: {pt3.x}, y: {pt3.y}, z: {pt3.z}")
    try:
        pt3.z = 40
    except AttributeError as e:
        print(f"Ошибка при попытке изменить z: {e}")
    try:
        pt3.extra = 100
    except AttributeError as e:
        print(f"Ошибка при попытке добавить атрибут 'extra': {e}")
    try:
        print(pt3.__dict__)
    except AttributeError as e:
        print(f"Ошибка доступа к __dict__: {e}")
#2#
import timeit
import sys
class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
class SlotPoint:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
def benchmark_move(obj):
    obj.move(1, 1)
if __name__ == '__main__':
    num_iterations = 100000
    num_objects = 1000
    normal_points = [NormalPoint(i, i) for i in range(num_objects)]
    slot_points = [SlotPoint(i, i) for i in range(num_objects)]
    normal_timer = timeit.Timer(lambda: [benchmark_move(p) for p in normal_points])
    normal_time = normal_timer.timeit(number=num_iterations) / num_iterations
    print(f"NormalPoint move time: {normal_time:.6f} seconds per {num_objects} objects")
    slot_timer = timeit.Timer(lambda: [benchmark_move(p) for p in slot_points])
    slot_time = slot_timer.timeit(number=num_iterations) / num_iterations
    print(f"SlotPoint move time: {slot_time:.6f} seconds per {num_objects} objects")
    normal_size = sys.getsizeof(NormalPoint(0, 0))
    slot_size = sys.getsizeof(SlotPoint(0, 0))
    print(f"NormalPoint size: {normal_size} bytes")
    print(f"SlotPoint size: {slot_size} bytes")
    normal_point = NormalPoint(1, 2)
    normal_point.z = 3
    try:
        slot_point = SlotPoint(1, 2)
        slot_point.z = 3 
    except AttributeError as e:
        print(f"Ошибка при попытке добавить новый атрибут в SlotPoint: {e}")
#3#
class Student:
    __slots__ = ('name', 'age', 'grade')

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
def calculate_average_grade(students):
    """Вычисляет среднюю оценку студентов в коллекции.

    Args:
        students: Список объектов Student.

    Returns:
        Средняя оценка студентов, или 0, если список пуст.
    """
    if not students:
        return 0

    total_grade = sum(student.grade for student in students)
    return total_grade / len(students)
if __name__ == '__main__':
    students = [
        Student("Alice", 20, 90),
        Student("Bob", 21, 85),
        Student("Charlie", 19, 78),
        Student("David", 22, 92),
    ]
    average_grade = calculate_average_grade(students)
    print(f"Средняя оценка студентов: {average_grade}")
#4#
class Product:
    __slots__ = ('name', 'price', 'quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
def find_products_above_threshold(products_dict, price_threshold):
    """Находит названия товаров, цена которых превышает заданный порог.
    Args:
        products_dict: Словарь, где ключи - названия товаров, а значения - объекты Product.
        price_threshold: Пороговая цена.
    Returns:
        Список названий товаров, цена которых выше price_threshold.
    """
    product_names = [
        name for name, product in products_dict.items() if product.price > price_threshold
    ]
    return product_names
if __name__ == '__main__':
    products = {
        "Laptop": Product("Laptop", 1200, 10),
        "Mouse": Product("Mouse", 25, 100),
        "Keyboard": Product("Keyboard", 75, 50),
        "Monitor": Product("Monitor", 300, 20),
        "Headphones": Product("Headphones", 150, 75),
    }
    threshold = 200
    expensive_products = find_products_above_threshold(products, threshold)
    print(f"Товары с ценой выше {threshold}: {expensive_products}")
