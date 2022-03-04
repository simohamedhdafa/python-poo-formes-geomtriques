from Circle import *
from Rectangle import *

def drawShapes(shapes, t):
    for shp in shapes:
        shp.draw(t)
    t.done()

if __name__ == '__main__':
    c = Circle(x=0, y=100, radius=50) 
    r = Rectangle(x=0, y=-100, w=50, h=200) 
    shapes = [c, r, Circle(-100, 50, 40), Circle(200, 50, 40)] 
    drawShapes(shapes, tr) 
    tr.exitonclick()
