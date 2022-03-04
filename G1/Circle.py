from Shape import *

class Circle(Shape):
    def __init__(self, x, y, radius, t_t=1, c_t="black", c_r="white"):
        Shape.__init__(self, x, y, t_t, c_t, c_r) 
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def setRadius(self, r):
        self.__radius = -r if r<0 else r
    
    def __str__(self):
        return "x {} y {} radius {}".format(self._x, self._y, self.__radius)

    def draw(self, t):
        super().draw(t)
        t.begin_fill()
        t.circle(self.__radius)
        t.end_fill()
        t.penup()
