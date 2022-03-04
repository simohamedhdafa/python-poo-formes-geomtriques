import turtle as tr
class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    
    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y

    def draw(self, t):
        t.penup()
        t.setx(self._x)
        t.sety(self._y)
        t.pendown()
