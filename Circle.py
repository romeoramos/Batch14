from Figure import Figure
import math

class Circle(Figure):

    def __init__(self,name, radius):
        super().__init__(name)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self,side):
        self.__radius = radius

    def perimeter(self):
        p = math.pi * self.__radius ** 2
        print("El Perimetro de %s es" % self.getName(), str(p))

    def area(self):
        a = math.pi * self.__radius * 2
        print("El Area de %s es" % self.getName(), str(a))
