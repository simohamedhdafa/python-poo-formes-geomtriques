import turtle as tr

class Shape:
    def __init__(self, x, y, t_t, c_t, c_r):
        self._x = x
        self._y = y
        self._taille_trait = t_t
        self._couleur_trait = c_t
        self._couleur_remplissage = c_r
        
    def getX(self):
        return self._x
    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y
    
    def draw(self, t):
        t.pensize(self._taille_trait)
        t.pencolor(self._couleur_trait)
        t.fillcolor(self._couleur_remplissage)
        t.penup()
        t.setposition(self._x, self._y)
        t.pendown()