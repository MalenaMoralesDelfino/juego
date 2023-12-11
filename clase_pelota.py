import pygame

from variables_globales import *
from clase_personaje import*


class Pelota:
    def __init__(self,tamaño:tuple,origen:tuple,path_imagen, velocidad: int, direccion: str):
        self.superficie = pygame.image.load(path_imagen).convert_alpha() #optimiza la imagen
        self.superficie = pygame.transform.scale(self.superficie,tamaño) #lo escala
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = origen
        self.velocidad = velocidad
        self.direccion = direccion
        self.flag_disparada = False

    def update(self):
        if self.direccion == "arriba":
            self.rectangulo.y -= self.velocidad
            if self.rectangulo.bottom < 0:
                self.rectangulo.center = (-10,-10)
                self.flag_disparada = False
        elif self.direccion == "abajo":
             self.rectangulo.y += self.velocidad
             if self.rectangulo.top > 680:
                    self.rectangulo.center = (-10,-10)
                    self.flag_disparada = False
        

    def crear_pelota(direccion, oringen_personaje,path_imagen):
            pelota = Pelota((20,40),oringen_personaje,path_imagen,8,direccion)
            return pelota
    

    def colisionar(self,objeto_personaje:Personaje, lista_personajes:list):
        if self.rectangulo.colliderect(objeto_personaje.rectangulo):
            objeto_personaje.perder_vida() 
            self.rectangulo.center = (-10,-10)
            if objeto_personaje.vidas == 0:
                lista_personajes.remove(objeto_personaje)
 

