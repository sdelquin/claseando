import os


class Coche:
    def __init__(self, nombre, cc, caballos, color, deposito_gasolina=40):
        self.nombre = nombre
        self.cc = cc
        self.caballos = caballos
        self.color = color
        self.velocidad = 0
        self.extras = []
        self.deposito_gasolina = deposito_gasolina
        self.gasolina = self.deposito_gasolina

    def porcentaje_gasolina(self):
        return self.gasolina / self.deposito_gasolina * 100

    def __str__(self):
        buffer = []
        buffer.append(f'''{self.nombre} {self.cc}cc ({self.caballos} caballos)
Velocidad {self.velocidad} km/h
Gasolina: {self.porcentaje_gasolina()}%''')
        if self.extras:
            extras = ','.join(self.extras)
            buffer.append(f'Extras: {extras}')
        buffer.append('----------------')
        return os.linesep.join(buffer)

    def acelerar(self, aceleracion):
        self.gasolina -= 0.05 * aceleracion
        self.velocidad += aceleracion

    def frenar(self, deceleracion):
        self.velocidad -= deceleracion

    def añade_extra(self, extra):
        self.extras.append(extra)


if __name__ == '__main__':
    coche1 = Coche('BMW', 1000, 200, 'azul')
    coche2 = Coche('Mercedes', 2000, 50, 'amarillo')
    coche3 = Coche('Jaguar', 600, 50, 'blanco')
    print(coche1)
    coche1.acelerar(20)
    print(coche1)
    coche2.acelerar(100)
    print(coche2)
    coche2.añade_extra('aire acondicionado')
    coche2.añade_extra('llantas 20"')
    print(coche2)
    print(coche3)
    coche3.acelerar(50)
    print(coche3)
    coche3.frenar(20)
    print(coche3)
