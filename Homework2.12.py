#№1#
def find_elements_by_index(values, indices):
    result = []
    try:
        for index in indices:
            result.append(values[index])
        return result
    except IndexError as e:
        return f"Ошибка индекса: {e}"
if __name__ == '__main__':
    values1 = [10, 20, 30, 40, 50]
    indices1 = [0, 2, 4]
    result1 = find_elements_by_index(values1, indices1)
    print(f"Результат 1: {result1}") 
    values2 = [10, 20, 30]
    indices2 = [0, 1, 3] 
    result2 = find_elements_by_index(values2, indices2)
    print(f"Результат 2: {result2}")  
    values3 = [1, 2, 3, 4, 5]
    indices3 = []
    result3 = find_elements_by_index(values3, indices3)
    print(f"Результат 3: {result3}") 
    values4 = []
    indices4 = [0, 1]
    result4 = find_elements_by_index(values4, indices4)
    print(f"Результат 4: {result4}") 


#№2#
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2
    def area(self):
        return math.pi * self.radius ** 2
if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f"Радиус: {circle.radius}")
    print(f"Диаметр: {circle.diameter}") 
    area = circle.area()
    print(f"Площадь: {area}")
    circle.radius = 10
    print(f"Новый радиус: {circle.radius}")
    print(f"Новый диаметр: {circle.diameter}")
    try:
        circle.diameter = 20
    except AttributeError as e:
        print(f"Ошибка при попытке изменить диаметр: {e}")


#№3#
class Employee:
    def __init__(self):
        self._employees = []  # Список словарей, где каждый словарь представляет сотрудника
    def add_employee(self, name, salary):
        self._employees.append({"name": name, "salary": salary})
    @property
    def average_salary(self):
        if not self._employees:
            return 0  # Возвращает 0, если список сотрудников пуст
        total_salary = sum(emp["salary"] for emp in self._employees)
        return total_salary / len(self._employees)
    def get_sorted_employees(self):
        return sorted(self._employees, key=lambda emp: emp["salary"])
if __name__ == '__main__':
    employees = Employee()
    employees.add_employee("Alice", 50000)
    employees.add_employee("Bob", 60000)
    employees.add_employee("Charlie", 45000)
    employees.add_employee("David", 55000)
    average_salary = employees.average_salary
    print(f"Средняя зарплата: {average_salary}")
    sorted_employees = employees.get_sorted_employees()
    print("Сотрудники, отсортированные по зарплате:")
    for employee in sorted_employees:
        print(f"{employee['name']}: {employee['salary']}")