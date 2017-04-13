from Figure import Figure

class Cuadrado(Figure):

    def __init__(self,name,side):
        super().__init__(name)
        self.__side = side

    def getSide(self):
        return self.__side

    def setSide(self,side):
        self.__side = side

    def perimeter(self):
        p = self.__side * 4
        print("El Perimetro de %s es" % self.getName(), str(p))

    def area(self):
        a = self.__side ** 2
        print("El Area de %s es" % self.getName(), str(a))
