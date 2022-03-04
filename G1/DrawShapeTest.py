from Circle import *
from Rectangle import *

def drawShapes(shapes, t):
    for shp in shapes:
        shp.draw(t)
    t.done()

if __name__ == '__main__':
    """
    c = Circle(x=0, y=100, radius=50) 
    r = Rectangle(x=0, y=-100, w=50, h=200) 
    shapes = [c, r] 
    drawShapes(shapes, tr) 
    tr.exitonclick()
    """
    c = Circle(x=0, y=100, radius=50, t_t=3, c_t="red", c_r="orange") 
    r = Rectangle(x=0, y=-100, w=50, h=200, t_t=5, c_t="blue", c_r="cyan") 
    shapes = [c, r, Circle(x=-150, y=300, radius=70, t_t=6, c_t="purple", c_r="pink") , Rectangle(x=100, y=100, w=50, h=85, t_t=2, c_t="green",  c_r="yellow")] 
    drawShapes(shapes, tr) 
    tr.exitonclick()