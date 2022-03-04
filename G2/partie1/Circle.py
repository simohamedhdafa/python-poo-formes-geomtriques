class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getRadius(self):
        return self.__radius
    
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setRadius(self, r):
        self.__radius = -r if r<0 else r
    
    def __str__(self):
        return "x {} y {} radius {}".format(self.__x, self.__y, self.__radius)