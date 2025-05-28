#№3#
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        return "Attribute is not available"
    
c = Car("BMW", "M4")
print(c.make)     
print(c.color)     

#№4#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name not in ('width', 'height'):
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(name, value)

# Example usage
r = Rectangle(10, 20)
print(r.width)
print(r.height)
try:
    r.color = 'red'  # Попытка создания локального атрибута
except AttributeError as e:
    print(e)  # Вывод: Local attributes are not allowed