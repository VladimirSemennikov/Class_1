"""
Задача 1: Класс "Круг"
Создайте класс Circle, который будет иметь атрибут радиуса и методы для
вычисления площади и периметра круга.
"""
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius                        # создаем атрибут радиуса

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(11)
print(f"Площадь круга: {circle.area()}")
print(f"Периметр круга: {circle.perimeter()}")

"""
Задача 2: Класс "Прямоугольник"
Создайте класс Rectangle, который будет иметь атрибуты ширины и высоты, а 
также методы для вычисления площади и периметра.
"""
class Rectangle:
    def __init__(self,width, height):           # создаем атрибуты ширины и высоты
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(3,11)
print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Периметр прямоугольника: {rectangle.perimeter()}")

"""
Задача 3: Класс "Счетчик"
Создайте класс Counter, который будет иметь метод для увеличения счетчика 
на 1 и метод для получения текущего значения счетчика.
"""
class Counter:
    def __init__(self, count = 0):
        self.count = count
    def increment(self):
        self.count += 1
    def value(self):
        return self.count

counter = Counter()
print(f"Текущее значение счетчика: {counter.value()}")
counter.increment()
print(f"Текущее значение счетчика: {counter.value()}")
counter.increment()
print(f"Текущее значение счетчика: {counter.value()}")
counter.increment()
print(f"Текущее значение счетчика: {counter.value()}")
counter.increment()
print(f"Текущее значение счетчика: {counter.value()}")


"""
Задача 4: Класс "Автомобиль"
Создайте класс Car, который будет иметь атрибуты для марки, модели и года выпуска. 
Добавьте метод для отображения информации об автомобиле.
"""



"""
Задача 5: Класс "Студент"
Создайте класс Student, который будет иметь атрибуты имени, фамилии и списка оценок. 
Реализуйте методы для добавления оценки и вычисления среднего балла.
"""