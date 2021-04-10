import math
import re


class Point:
    __colour = "red"

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def Coord(self):
        print("Координати точки:", self.__x, self.__y)

    def Distance(self):
        return math.sqrt(self.__x * self.__x + self.__y * self.__y)

    def Vector(self, a, b):
        self.__x += a
        self.__y += b

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, value_x):
        self.__x = value_x

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, value_y):
        self.__y = value_y

    @property
    def GetColour(self):
        return self.__colour

    def __getitem__(self, item):
        if item == 0:
            return self.__x
        elif item == 1:
            return self.__y
        elif item == 2:
            return self.__colour
        return "Такого значення не існує"

    def __setitem__(self, item, value):
        if item == 0:
            self.__x = value
        elif item == 1:
            self.__y = value
        elif item == 2:
            self.__colour = value
        else:
            print("Такого значення не існує")

    def __iadd__(self, other):
        self.__x += 1
        self.__y += 1
        return self

    def __isub__(self, other):
        self.__x -= 1
        self.__y -= 1
        return self

    def __bool__(self):
        return self.__x == self.__y

    def __add__(self, other):
        self.__x += other
        self.__y += other

        return self

    def __str__(self):
        strPoint = "x: " + str(self.__x) + " y: " + str(self.__y)
        return strPoint

    @staticmethod
    def with_str(strP):
        result = re.findall(r'\d+', str(strP))
        return Point(int(result[0]), int(result[1]))


pt = Point(3, 4)

pt.Coord()
print(pt.GetColour)

pt[2] = "blue"
print(pt[0], pt[1], pt[2])
pt += 1
pt.Coord()
pt -= 1
pt.Coord()
if pt:
    print("Координати рівні")
else:
    print("Координати не рівні")
pt + 5
pt.Coord()
print(pt)
Point.with_str(pt)
