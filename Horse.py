import random
class Horse:

    def __init__(self,name,step,position):
        self.name = name
        self.step = step
        self.position = position

    def goStep(self):
        self.step = random.randrange(0,5)
        self.position += self.step

if __name__ == '__main__':

    pancho = Horse("Pancho",0,0)
    otelo = Horse("Otelo",0,0)

    while pancho.position < 20 and otelo.position < 20 :
        pancho.goStep()
        otelo.goStep()
        print("Un paso en la carrera")

    if pancho.position == otelo.position:
        print("Tus caballos %s y %s han empatado con %s y %s pasos" % (pancho.name, otelo.name,str(pancho.position),str(otelo.position)))
    elif pancho.position > otelo.position:
        print("El caballo %s gano la carrera con %s" % (pancho.name,pancho.position))
    elif pancho.position < otelo.position:
        print("El caballo %s gano la carrera con %s" % (otelo.name,otelo.position))
