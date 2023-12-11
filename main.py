import pygame, sys, tkinter.messagebox
import pygame.display
from variables_globales import *
from clase_creadora import*
from clase_conexionBD import*
from clase_puntajes import*
from pantallas import*


#VARIABLES GLOBALES

screen_size = (ANCHO,ALTO)


pygame.init()

screen = pygame.display.set_mode(screen_size) #pixeles tupla
clock = pygame.time.Clock() #tiempo
pygame.display.set_caption("LA SCALONETA")

# Carga la imagen de fondo
fondo = pygame.image.load("CUATRI2\juego\prueba_4\codigo\\recursos\estadio.png").convert() #convierte la imagen a un formato más eficiente y optimo
fondo = pygame.transform.scale(fondo, screen_size) #lo escala


#Icono del juego
icono = pygame.image.load("CUATRI2\juego\prueba_4\codigo\\recursos\icono.png")
pygame.display.set_icon(icono)

#Instancias
lista_pelotas_messi = Creadora.crear_lista_pelotas("arriba","CUATRI2\juego\prueba_4\codigo\\recursos\\futbol_arg.png")
lista_pelotas_mbappe = Creadora.crear_lista_pelotas("abajo","CUATRI2\juego\prueba_4\codigo\\recursos\pelota_enemigo.png")
lista_personajes_principales = Creadora.crear_personajes()
messi = lista_personajes_principales[0]
mbappe = lista_personajes_principales[1]

lista_personajes_secundarios = Creadora.crear_lista_personajes_secundarios()
lista_aliados = lista_personajes_secundarios[0]
lista_enemigos = lista_personajes_secundarios[1]

ConexionBD.crear_bd_puntajes()
nombre_jugador = mostrar_pantalla_nombre(screen)


while True: #Todo sucede dentro de un bucle
    
    score = (pygame.time.get_ticks()  * 0.001)
    clock.tick(FPS) #no ejecuta mas rapido
    
    font = pygame.font.SysFont("Courier new", 22, True, False)
    text = font.render(f"Score: {round(score,1)}", True, WHITE)
    texto_vidas_messi = font.render(f"Vidas: {messi.vidas}", True, WHITE)
    fuente_vidas_mbappe = pygame.font.SysFont("Courier new", 20, True, False)
    texto_vidas_mbappe = fuente_vidas_mbappe.render(f"{mbappe.vidas}",True,WHITE)
    nivel= 1
    
    for event in pygame.event.get(): #por cada evento en una cola de evento
        if event.type == pygame.QUIT: #si ese evento coincide con "cerrar ventana se finaliza y cierra"
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                messi.disparar_pelota(lista_pelotas_messi)
            if event.key == pygame.K_ESCAPE:
                respuesta = tkinter.messagebox.askquestion("Salir", "¿Seguro que quiere salir?")
                if respuesta == "yes":
                    pygame.quit()
 
                
    teclas = pygame.key.get_pressed() #lista de todas las teclas presionadas en una iteracion del while
        #MESSI SE MUEVE DE IZQ a DER
    if teclas[pygame.K_RIGHT]:
        messi.desplazar("der")
    if teclas[pygame.K_LEFT]:
        messi.desplazar("izq")

    mbappe.disparar_pelota(lista_pelotas_mbappe)
    mbappe.direccion_movimiento = mbappe.desplazar(mbappe.direccion_movimiento)


    # Dibuja la imagen de fondo
    screen.blit(fondo, (0, 0))
    screen.blit(text,(0,0))
    screen.blit(texto_vidas_messi, (200,0))       
    screen.blit(messi.superficie, messi.rectangulo)
    screen.blit(mbappe.superficie, mbappe.rectangulo)
    screen.blit(texto_vidas_mbappe, mbappe.rectangulo)
    

    for pelota in lista_pelotas_messi:
        screen.blit(pelota.superficie, pelota.rectangulo)
        Pelota.update(pelota)
        if mbappe.colisionar(pelota):
            mostrar_juego_ganado(screen,score, nombre_jugador)
        for enemigo in lista_enemigos:
            pelota.colisionar(enemigo,lista_enemigos)
        
            

    for pelota in lista_pelotas_mbappe:
        screen.blit(pelota.superficie, pelota.rectangulo)
        Pelota.update(pelota)
        if messi.colisionar(pelota):
            mostrar_game_over(screen, score, nombre_jugador)
        for aliado in lista_aliados:
            pelota.colisionar(aliado,lista_aliados)




    for aliado in lista_aliados:
        screen.blit(aliado.superficie, aliado.rectangulo)
    for enemigo in lista_enemigos:
        screen.blit(enemigo.superficie, enemigo.rectangulo)
        if len(lista_enemigos)<37:
            enemigo.desplazar()
        if len(lista_enemigos)<30:
            nivel = 2
            enemigo.aumentar_desplazamiento()
        if len(lista_enemigos)<15:
            nivel = 3
            mbappe.aumentar_desplazamiento()
            
    
    texto_banderas = font.render(f"Banderas: {len(lista_enemigos)}", True, WHITE)
    texto_niveles = font.render(f"Nivel: {nivel}", True, WHITE)
    screen.blit(texto_niveles, (450,0))
    screen.blit(texto_banderas, (650,0))

    
    

    pygame.display.update()
