class Rectangle:

    def __init__(self, x, y, w, h):
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height

    def setX(self, v):
        self.__x = v
    def setY(self, v):
        self.__y = v
    def setWidth(self, v):
        self.__width = v if v>=0 else -v
    def setHeight(self, v):
        self.__height = v if v>=0 else -v
    
    def __str__(self):
        return "x {2} y {0} width {3} height {1}".format(self.__y, self.__height, self.__x, self.__width)