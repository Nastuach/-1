# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Rectangle:
    def __init__(self, width: float, height: float):
        """
                Создание и подготовка к работе объекта "Прямоугольник"

                :param width: Ширина прямоугольника
                :param height: Высота прямоугольника

                Примеры:
                >>> rectangle = Rectangle(20, 30)  # инициализация экземпляра класса

                """
        if not isinstance(width,(int,float)):
            raise TypeError("Ширина прямоугольника должна быть типа int или float")
        if not isinstance(height,(int,float)):
            raise TypeError("Высота прямоугольника должна быть типа int или float")
        if width<=0:
            raise  ValueError("Ширина должна быть положительным числом")
        if height<=0:
            raise ValueError("Высота должна быть положительным числом")
        self.width = width
        self.height = height
    def Square(self)->float:
        """
                Функция которая считает площадь прямоугольника

                :return: Площадь прямоугольника

                Примеры:
                >>> rectangle = Rectangle(20, 30)
                >>> rectangle.Square()
                """
        ...
    def Perimetr(self):
        """
                        Функция которая считает периметр прямоугольника

                        :return: Периметр прямоугольника

                        Примеры:
                        >>> rectangle = Rectangle(20, 30)
                        >>> rectangle.Perimetr()
                        """
        ...

class Ball:
    def __init__(self, radius: float):
        """
                        Создание и подготовка к работе объекта "Шар"

                        :param radius: Радиус шара

                        Примеры:
                        >>> ball = Ball(10)  # инициализация экземпляра класса

                        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус шара должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус шара должен быть положительным числом")
        self.radius = radius

    def Volume(self) -> float:
        """
                Функция которая считает объём шара

                :return: Объём шара

                Примеры:
                >>> ball = Ball(10)
                >>> ball.Volume()
                """
        ...

    def Surface_Area(self):
        """
                        Функция которая считает площадь поверхности шара

                        :return: Площадь поверхности шара

                        Примеры:
                        >>> ball = Ball(10)
                        >>> ball.Surface_Area()
                        """
        ...

class Car:
    def __init__(self, speed: float):
        """
                        Создание и подготовка к работе объекта "Машина"

                        :param speed: Скорость машины

                        Примеры:
                        >>> car = Car(120)  # инициализация экземпляра класса
                        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость машины должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость машины должна быть положительным числом")
        self.speed = speed
    def Distance(self, time: float) -> float:
        """
                Функция которая считает расстояние пройденное за время time

                :return: Расстояние

                Примеры:
                >>> car = Car(120)
                >>> car.Distance(5)
                """
        ...
    def Time(self, distance: float) -> float:
        """
                Функция которая считает время, за которое было пройденно расстояние distance

                :return: Время

                Примеры:
                >>> car = Car(120)
                >>> car.Time(10)
                """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
