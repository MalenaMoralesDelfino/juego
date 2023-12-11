import pygame

from variables_globales import *


class Personaje:
    def __init__(self,tamaño:tuple,origen:tuple,path_imagen, vidas:int,velocidad) -> None:
        self.superficie = pygame.image.load(path_imagen).convert_alpha() #optimiza la imagen
        self.superficie = pygame.transform.scale(self.superficie,tamaño) #lo escala

        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = origen
        self.vidas = vidas
        self.velocidad = velocidad


    def perder_vida(self):
        self.vidas -= 1




