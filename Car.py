from Vehicle import Vehicle,Transport

class Car(Vehicle,Transport):

    def __init__(self, color, precio, motor, combustible, placas, caballos, num_puertas):
        super().__init__(color, precio, motor, combustible)
        #super().__init__(Transport, tipo)
        self.placas = placas
        self.caballos = caballos
        self.num_puertas = num_puertas

if __name__=='__main__':
    car = Car("Rojo","1212121212","V8","Dissel","345ert",2)
    print(car.moverse())
    print(car.precio)
    print(muestraTipo("Deportivo"))
