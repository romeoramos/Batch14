from Figure import Figure
from Triangle import Triangle
from Cuadrado import Cuadrado
from Circle import Circle
import math

if __name__ == '__main__':
    fig=Figure("Cuadro")
    fig.setName("Cuadros")
    print(fig.getName())

    triangulo=Triangle("triangulo",25)
    print(triangulo.getSide())
    triangulo.perimeter()
    triangulo.area()

    cuadro=Cuadrado("cuadro",30)
    cuadro.setSide(25)
    cuadro.perimeter()
    cuadro.area()

    circulo=Circle("circulo",25)
    circulo.perimeter()
    circulo.area()
