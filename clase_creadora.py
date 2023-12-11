

from variables_globales import *
from clase_messi import*
from clase_mbappe import*
from clase_enemigo import*
from clase_sonido import*

class Creadora:
    def crear_personajes():
        messi = Messi((70,90),(150,630),"CUATRI2\juego\prueba_4\codigo\\recursos\messi_1.png",3,10)
        mbappe = Mbappe((70,80),(150,60),"CUATRI2\juego\prueba_4\codigo\\recursos\mbappe_2.png",3,10) 
        lista_personajes_principales = [messi, mbappe]

        return lista_personajes_principales
    
    def crear_lista_pelotas(direccion, path_imagen):
        lista_pelotas = []
        for i in range(20):
            pelota = Pelota.crear_pelota(direccion,(-10,-10),path_imagen)
            lista_pelotas.append(pelota)
        return lista_pelotas
    

    def crear_lista_personajes_secundarios():
        lista_general = []

        lista_aliados = [Personaje((80,70),(150,540),"CUATRI2\juego\prueba_4\codigo\\recursos\depaul.jpg",6,0),
                        Personaje((80,70),(350,540),"CUATRI2\juego\prueba_4\codigo\\recursos\paredes.jpg",6,0),
                        Personaje((80,70),(550,540),"CUATRI2\juego\prueba_4\codigo\\recursos\dimaria.jpg",6,0),
                        Personaje((80,70),(750,540),"CUATRI2\juego\prueba_4\codigo\\recursos\ota.jpg",6,0)
                        ]
        
        configuracion_enemigos = [((40, 20), (100, 130), "CUATRI2\juego\prueba_4\codigo\\recursos\\francia.png", 4, 5, 60, 13),
                                ((50, 30), (120, 180), "CUATRI2\juego\prueba_4\codigo\\recursos\croacia.png", 3, 3, 68, 11),
                                ((55, 35), (140, 230), "CUATRI2\juego\prueba_4\codigo\\recursos\paises_bajos.png", 2, 4, 80, 9),
                                ((70, 40), (160, 280), "CUATRI2\juego\prueba_4\codigo\\recursos\\australia.png", 2, 1, 100, 7)
                                ]
        
        lista_enemigos = []

        for configuracion in configuracion_enemigos:
            enemigo = Enemigo(*configuracion)
            lista_enemigos.extend(enemigo.generar_enemigos(configuracion[2]))



        lista_general.append(lista_aliados)
        lista_general.append(lista_enemigos)
        return lista_general

    def crear_sonido():
        musica = Sonido("CUATRI2\juego\prueba_4\codigo\\recursos\sonido_on.png",GREEN,(600,375))
        return musica
        


    