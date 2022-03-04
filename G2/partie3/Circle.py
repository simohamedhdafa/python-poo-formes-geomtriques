
from Shape import *

class Circle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self,x,y)
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def setRadius(self, r):
        self.__radius = -r if r<0 else r
    
    def __str__(self):
        return "x {} y {} radius {}".format(self._x, self._y, self.__radius)

    def draw(self, tc):
        super().draw(tc) # appeler la vrsion superieure de draw
        tc.circle(self.__radius)
        tc.penup()