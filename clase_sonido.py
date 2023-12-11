import pygame
from variables_globales import *




class Sonido:
    def __init__(self,path,color,center) -> None:
        self.cambiar_imagen(path)
        self.color = color
        self.rect_sonido = self.boton_sonido.get_rect()
        self.rect_sonido.center = center
        pygame.mixer.music.load("CUATRI2\juego\prueba_4\codigo\\recursos\seleccion.mp3")#carga el sonido
        pygame.mixer.music.play()#se reproduce en bucle
        pygame.mixer.music.set_volume(0.2)#sube baja volumen


    def cambiar_imagen(self,path):
        self.boton_sonido = pygame.image.load(path).convert_alpha() #optimiza la imagen
        self.boton_sonido = pygame.transform.scale(self.boton_sonido,(30,30)) #lo escala




    def apagar_musica (self):
        self.color = RED
        self.cambiar_imagen("CUATRI2\juego\prueba_4\codigo\\recursos\sonido_off.png")
        pygame.mixer.music.pause()

    def prender_musica(self):
        self.color = GREEN
        self.cambiar_imagen("CUATRI2\juego\prueba_4\codigo\\recursos\sonido_on.png")
        pygame.mixer.music.play()#se reproduce en bucle
        pygame.mixer.music.set_volume(0.2)#sube baja volumen
