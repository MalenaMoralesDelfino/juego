
import pygame,sys
from clase_conexionBD import*
from clase_puntajes import*
from clase_sonido import*
from variables_globales import *
from clase_creadora import*

def pegar_fondo(screen,path):
        fondo = pygame.image.load(path).convert()
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

        # Crear superficie translúcida
        translucent_surface = pygame.Surface((700, 460), pygame.SRCALPHA)
        translucent_surface.fill((255, 255, 255))  # Color blanco translúcido (RGBA)
        pygame.draw.rect(translucent_surface, (255, 255, 255, 128), translucent_surface.get_rect())
        screen.blit(fondo, (0, 0))
        screen.blit(translucent_surface, (100, 100))  # Renderizar el rectángulo translúcido

        return translucent_surface

def mostrar_pantalla_nombre(screen):
    fondo = pygame.image.load("CUATRI2\juego\prueba_4\codigo\\recursos\estadio.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # Crear superficie translúcida
    translucent_surface = pygame.Surface((700, 460), pygame.SRCALPHA)
    translucent_surface.fill((255, 255, 255))  # Color blanco translúcido (RGBA)
    pygame.draw.rect(translucent_surface, (255, 255, 255, 128), translucent_surface.get_rect())

    font1 = pygame.font.SysFont("MV Boli", 50, True, False)
    font2 = pygame.font.SysFont("MV Boli", 30, True, False)
    font3 = pygame.font.SysFont("MV Boli", 20, False, False)
    text_inicio = font1.render("LA SCALONETA", True, BLACKBLUE)
    text_ingresar_nombre = font2.render("Ingresa tu nombre: ", True, BLACKBLUE)
    text_continuar = font3.render("Presiona 'enter' para continuar", True, BLACK)
    
    sonido = Creadora.crear_sonido()

    # Variable
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Nombre ingresado:", input_text)
                    mostrar_pantalla_inicio(screen,input_text,sonido)
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Renderizar texto
        text_surface = font2.render(input_text, True, BLACK)
        text_rect = text_surface.get_rect(center=(600, 312))
        screen.blit(fondo, (0, 0))
        screen.blit(translucent_surface, (100, 100))  # Renderizar el rectángulo translúcido
        screen.blit(text_inicio,  (250, 156))
        screen.blit(text_ingresar_nombre, (250, 286))
        screen.blit(text_surface, text_rect)
        screen.blit(text_continuar, (100, 506))
    
        # Actualizar la pantalla
        pygame.display.flip()




def mostrar_pantalla_inicio(screen,input_text:str,sonido:Sonido):

    pegar_fondo(screen,"CUATRI2\juego\prueba_4\codigo\\recursos\estadio.png")

    font1 = pygame.font.SysFont("MV Boli", 50, True, False)
    font2 = pygame.font.SysFont("MV Boli", 30, True, False)
    text_inicio = font1.render("LA SCALONETA", True, BLACKBLUE)
    text_nombre = font2.render("HOLA "+input_text.upper(), True, BLACKBLUE)
    text_jugar = font2.render("Jugar", True, WHITE)
    text_salir = font2.render("Salir", True, WHITE)
    text_opciones = font2.render("Opciones", True, WHITE)


    # Crear superficies rectangulares para las opciones
    boton_jugar = pygame.Surface((100, 50))
    boton_jugar.fill(BLACKBLUE)
    boton_salir = pygame.Surface((100, 50))
    boton_salir.fill(BLACKRED)
    boton_opciones = pygame.Surface((130,50))
    boton_opciones.fill(ORANGE)

    rect_jugar = boton_jugar.get_rect()
    rect_jugar.center=(320, 406)
    rect_salir = boton_salir.get_rect()
    rect_salir.center=(550, 406)
    rect_opciones = boton_opciones.get_rect()
    rect_opciones.center=(430, 500)

    # Renderizar texto en las superficies rectangulares
    boton_jugar.blit(text_jugar, (5, 2))
    boton_salir.blit(text_salir, (15, 2))
    boton_opciones.blit(text_opciones, (2, 2))

    
    bandera = True
    while bandera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rect_jugar.collidepoint(mouse_pos):
                    bandera = False
                elif rect_opciones.collidepoint(mouse_pos):
                    flag = True
                    if flag:
                        mostrar_pantalla_opciones(screen, sonido)
                    pegar_fondo(screen,"CUATRI2\juego\prueba_4\codigo\\recursos\estadio.png")
                elif rect_salir.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(text_inicio,  (250, 156))
        screen.blit(text_nombre, (350, 286))
        screen.blit(boton_jugar, rect_jugar)#(300, 406)
        screen.blit(boton_salir, rect_salir)#(500, 406)
        screen.blit(boton_opciones, rect_opciones)
        pygame.display.update()



def mostrar_pantalla_opciones(screen, sonido:Sonido):
    translucent_surface = pegar_fondo(screen,"CUATRI2\juego\prueba_4\codigo\\recursos\estadio.png")
    font1 = pygame.font.SysFont("MV Boli", 50, True, False)
    font2 = pygame.font.SysFont("MV Boli", 30, False, False)
    text_inicio = font1.render("LA SCALONETA", True, BLACKBLUE)
    text_opciones = font2.render("Opciones", True, BLACKBLUE)
    text_musica = font2.render("Activar/Desactivar música", True, BLACKBLUE)
    text_volver = font2.render("Volver", True, WHITE)

    # Crear superficies rectangulares para las opciones
    boton_volver = pygame.Surface((100, 50))
    boton_volver.fill(BLACKRED)
    
    #Rectangulos
    rect_volver= boton_volver.get_rect()
    rect_volver.center=(740, 130)
    # blitear texto en las superficies rectangulares
    boton_volver.blit(text_volver, (5, 2))
    
    bandera = True
    while bandera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rect_volver.collidepoint(mouse_pos):
                    bandera= False
                    
                    #mostrar_pantalla_inicio(screen,input_text)
                elif sonido.rect_sonido.collidepoint(mouse_pos):
                    if  sonido.color == GREEN:
                        sonido.apagar_musica()
                    elif sonido.color == RED:
                        sonido.prender_musica()

        screen.blit(text_inicio,  (250, 156))
        screen.blit(text_opciones, (350, 220))
        screen.blit(text_musica, (150,350))
        screen.blit(boton_volver, rect_volver)
        screen.blit( sonido.boton_sonido,  sonido.rect_sonido)

        pygame.display.update()





def mostrar_game_over(screen, score, nombre_jugador):
        pegar_fondo(screen,"CUATRI2\juego\prueba_4\codigo\\recursos\mbappe_ganador.jpg")
        font = pygame.font.SysFont("MV Boli", 50, True, False)
        font2 = pygame.font.SysFont("MV Boli", 20, False, False)
        text_game_over = font.render("GAME OVER", True, BLACK)
        text_score = font.render(f"Score: {round(score,1)}", True, BLACK)
        text_continuar = font2.render("Presiona 'enter' para ver los puntajes", True, BLACK)
        # Calcular las coordenadas x e y para centrar el texto
        x = (ANCHO - text_game_over.get_width()) / 2
        y = (ALTO - text_game_over.get_height()) / 2
        screen.blit(text_game_over,(x,y))
        screen.blit(text_score,(x,(y+50)))
        screen.blit(text_continuar, (100, 506))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        mostrar_puntajes(screen)




def mostrar_juego_ganado(screen, score, nombre_jugador):
    pegar_fondo(screen,"CUATRI2\juego\prueba_4\codigo\\recursos\messi_ganador.jpg")
    font = pygame.font.SysFont("Courier new", 50, True, False)
    text_game_over = font.render("¡GANASTE!", True, BLACK)
    font2 = pygame.font.SysFont("MV Boli", 20, False, False)
    text_score = font.render(f"Score: {round(score,1)}", True, BLACK)
    text_continuar = font2.render("Presiona 'enter' para ver los puntajes", True, BLACK)

    # Calcular las coordenadas x e y para centrar el texto
    x = (ANCHO - text_game_over.get_width()) / 2
    y = (ALTO - text_game_over.get_height()) / 2
    screen.blit(text_game_over,(x,y))
    screen.blit(text_score,(x,(y+50)))
    screen.blit(text_continuar, (100, 506))
    pygame.display.update()

    ConexionBD.guardar_puntaje_en_BD("db_puntajes.db", nombre_jugador, score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mostrar_puntajes(screen)
            
     

def mostrar_puntajes(screen):
    pegar_fondo(screen,"CUATRI2\juego\prueba_4\codigo\\recursos\campeones.jpg")
    font = pygame.font.SysFont("MV Boli", 40, True, False)
    text_inicio = font.render("LA SCALONETA", True, BLACKBLUE)
    text_puntaje = font.render("Puntajes", True, BLACKBLUE)
    text_salir = font.render("Salir", True, WHITE)
    
    # Crear superficies rectangulares para las opciones
    boton_salir = pygame.Surface((100, 50))
    boton_salir.fill(BLACKRED)

    #Rectangulos
    rect_salir= boton_salir.get_rect()
    rect_salir.center=(740, 130)

    # blitear texto en las superficies rectangulares
    boton_salir.blit(text_salir, (5, 2))

    screen.blit(text_inicio,  (110, 110))
    screen.blit(text_puntaje, (200, 186))
    screen.blit(boton_salir, rect_salir)#(500, 406)

    lista_desordenada = ConexionBD.guardar_puntajes_en_lista('db_puntajes.db')
    lista_ordenada = Puntajes.ordenar_puntajes(lista_desordenada)
    texto_top_five = crear_texto_top_five(lista_ordenada)

    saltos_de_linea = texto_top_five.split("\n")
    y = 250
    for linea in saltos_de_linea:
        text_lista_puntajes = font.render(linea, True, BLACKBLUE)
        screen.blit(text_lista_puntajes,  (350, y-10))
        y+=text_lista_puntajes.get_height()

    bandera = True
    while bandera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if  rect_salir.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def crear_texto_top_five(lista_ordenada:list) ->str:

    top_five = ""
    flag_maximo = 0
    for cantidad in range(0,len(lista_ordenada)):
        if flag_maximo < 5:
            nombre = lista_ordenada[cantidad][0]
            puntos = lista_ordenada[cantidad][1]
            top_five += nombre + " " + str("%.2f" % puntos) + "\n"
            flag_maximo += 1

    return top_five