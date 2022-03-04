#import turtle as tt
from Rectangle import *

if __name__ == '__main__':
    #tt = turtle.turtle()
    rct = Rectangle(10,50,50,40)
    rct.draw(tr)
    # x 10 y 50 width 50 hight 40
    #print(rct)
    rct.setX(20)
    rct.setY(30)
    rct.setHeight(100)
    # x 20 y 30 width 50 hight 100
    #print(rct)
    rct.draw(tr)
    tr.done()
