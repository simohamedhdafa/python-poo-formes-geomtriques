from Shape import *

class Rectangle(Shape):

    def __init__(self, x, y, w, h, t_t=1, c_t="black", c_r="white"):
        super().__init__(x,y, t_t, c_t, c_r)
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

    def draw(self, fk):
        super().draw(fk)
        fk.begin_fill()
        fk.fd(self.__width)
        fk.lt(90)
        fk.fd(self.__height)
        fk.lt(90)
        fk.fd(self.__width)
        fk.lt(90)
        fk.fd(self.__height)
        fk.lt(90)
        fk.end_fill()
        fk.penup()