import random

from variables_globales import *
from clase_personaje import*
from clase_pelota import*

class Mbappe(Personaje):
    def __init__(self, tamaño, origen, path_imagen, vidas,velocidad):
        super().__init__(tamaño, origen, path_imagen, vidas,velocidad)
        self.direccion_movimiento = "der"
        

    
    def desplazar(self,direccion):
        if direccion == "der":
            if self.rectangulo.x >= 820:
                direccion = "izq"
            elif self.rectangulo.x != 820:
                self.rectangulo.x += self.velocidad
        if direccion == "izq":
            if self.rectangulo.x <= 10:
                self.rectangulo.x = 10
                direccion = "der"
            elif self.rectangulo.x != 0:
                self.rectangulo.x -= self.velocidad
        return direccion

    def aumentar_desplazamiento(self):
        self.velocidad = +15

    def disparar_pelota(self, lista_pelotas:list):
        dispara = random.randint(1,20)
        if dispara == 1:
            cantidad_disparos = 0
            for pelota in lista_pelotas:
                if pelota.flag_disparada == False and cantidad_disparos == 0:
                    pelota.rectangulo.center = self.rectangulo.center
                    pelota.flag_disparada = True
                    cantidad_disparos = cantidad_disparos + 1
            return pelota

    
    def colisionar(self,objeto_pelota:Pelota):
        if self.rectangulo.colliderect(objeto_pelota.rectangulo):
            self.perder_vida() 
            objeto_pelota.rectangulo.center = (-10,-10)
            if self.vidas == 0:
                return True