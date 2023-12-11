import random

from variables_globales import *
from clase_personaje import*

class Enemigo(Personaje):
    def __init__(self, tamaño, origen, path_imagen, vidas,velocidad, incremento_x, cantidad):
        super().__init__(tamaño, origen, path_imagen, vidas,velocidad)
        self.cantidad = cantidad
        self.incremento_x = incremento_x
        self.direccion_movimiento = None

    def elegir_direccion_movimiento(self):
        numero_random = random.randint(0,1)
        if numero_random == 0:
            direccion = "der"
        else:
            direccion = "izq"

        self.direccion_movimiento = direccion
        

    def generar_enemigos(self, path_imagen):
        enemigos = []
        x = self.rectangulo.center[0]
        y = self.rectangulo.center[1]
        for _ in range(self.cantidad):
            enemigo = self.__class__(self.rectangulo.size, (x, y), path_imagen, self.vidas,self.velocidad, self.incremento_x, self.cantidad)
            enemigo.elegir_direccion_movimiento()
            enemigos.append(enemigo)
            x += self.incremento_x
        return enemigos
    
    def desplazar(self):

        if self.direccion_movimiento == "der":
            if self.rectangulo.x >= 820:
                self.direccion_movimiento = "izq"
            elif self.rectangulo.x != 820:
                self.rectangulo.x += self.velocidad
        if self.direccion_movimiento ==  "izq":
            if self.rectangulo.x <= 10:
                self.rectangulo.x = 10
                self.direccion_movimiento = "der"
            elif self.rectangulo.x != 0:
                self.rectangulo.x -= self.velocidad


    def aumentar_desplazamiento(self):
        self.velocidad = +10