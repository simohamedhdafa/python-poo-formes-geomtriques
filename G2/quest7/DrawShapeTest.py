from Circle import *
from Rectangle import *

def drawShapes(shapes, t):
    for shp in shapes:
        shp.draw(t)
    t.done()

if __name__ == '__main__':
    c = Circle(x=0, y=100, radius=50) 
    r = Rectangle(x=0, y=-100, w=50, h=200) 
    shapes = [Rectangle(x=0, y=-100, w=50, h=200, t_t=2, c_t="blue", c_r="orange"), c, r, Circle(-100, 50, 40), Circle(200, 50, 40, t_t=3, c_t="purple", c_r="yellow")] 
    drawShapes(shapes, tr) 
    tr.exitonclick()
