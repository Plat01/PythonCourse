from abc import ABC, abstractmethod


class Pnt(ABC):
    x_coordinate = 0
    y_coordinate = 0

    def distance(self, other):
        return ((self.x_coordinate - other.x_coordinate) ** 2 +
                (self.y_coordinate - other.y_coordinate) ** 2) ** (1 / 2)


class DefaultPoint(Pnt):
    x_coordinate = 0
    y_coordinate = 0

    def set_coordinate(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def __str__(self):
        return f"x = {self.x_coordinate}, y = {self.y_coordinate}"


p1 = DefaultPoint()
print(p1)
p1.set_coordinate(3, 6)
print(p1)


class StandartPoint(Pnt):
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    def __str__(self):
        return f"x = {self.x_coordinate}, y = {self.y_coordinate}"


p2 = StandartPoint(4, 7)
print(p2)

print(p1.distance(p2))
