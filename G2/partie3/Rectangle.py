
from Shape import *

class Rectangle(Shape):

    def __init__(self, x, y, w, h):
        super().__init__(x,y)
        self.__width = w
        self.__height = h

    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height

    def setWidth(self, v):
        self.__width = v if v>=0 else -v
    def setHeight(self, v):
        self.__height = v if v>=0 else -v
    
    def __str__(self):
        return "x {2} y {0} width {3} height {1}".format(self._y, self.__height, self._x, self.__width)

    def draw(self, tr):
        super().draw(tr)
        tr.fd(self.__width)
        tr.lt(90)
        tr.fd(self.__height)
        tr.lt(90)
        tr.fd(self.__width)
        tr.lt(90)
        tr.fd(self.__height)
        tr.penup()

