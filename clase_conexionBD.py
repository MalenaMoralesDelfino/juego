import sqlite3

class ConexionBD:
    '''
    chequea que verdaderamente la conexion se realice.
    si está todo bien, retorna el objeto connection.
    sino retorna error.
    '''
    def conexion_bd(nombre_bd) -> sqlite3.Connection:
        conexion = sqlite3.connect(nombre_bd)

        if isinstance(conexion,sqlite3.Connection):
            return conexion
        else:
            return ConnectionError
        
    def crear_bd_puntajes():
        '''
        Se crea la tabla. primero se crea la conexion, se intenta ejecutar la sentencia dada.
        Si no se puede imprime error. Si o si cierra la conexion.
        '''
        conexion =  sqlite3.connect("db_puntajes.db")

        try:
            sentencia = "create table puntajes (nombre text, puntaje real)"

            conexion.execute(sentencia)
            print("Tabla de puntajes creada")
        except sqlite3.OperationalError:
            print("La tabla de personajes ya existe")
        finally:
            conexion.close()

    def guardar_puntaje_en_BD(nombre_BD:str, nombre:str, score:float):
        '''
        Guarda la informacion en la base de datos.
        inenta insertar la sentencia con los nombres y puntajes del jugador.
        con el 'commit' guarda la sentencia en la base de datos.
        Si hay algun error imprime 'ERROR EN LA ESCRITURA DE LA BD'
        Si o si cierra la conexion.
        Parametros:
        -nombre_BD: nombre de la base de datos
        -nombre: nombre del jugador
        -score: puntaje del mismo
        '''

        conexion = ConexionBD.conexion_bd(nombre_BD)

        try:
            sentencia = "insert into puntajes(nombre, puntaje) values (?,?)"
            conexion.execute(sentencia, (nombre, score))
            conexion.commit()
            print("Guardado con exito")
        except:
            print("ERROR EN LA ESCRITURA DE LA BD")
        finally:
            conexion.close()


    def guardar_puntajes_en_lista(nombre_BD:str) ->list:
        '''
        Guarda todos los puntajes de los jugadores en una lista de tuplas.
        Parametros:
        -nombre_BD: nombre de la base de datos
        Retorna la lista.
        '''
        conexion = sqlite3.connect(nombre_BD)

        sentencia = "SELECT * FROM puntajes"
        cursor = conexion.execute(sentencia)
        
        lista_puntajes = []

        for fila in cursor:
            lista_puntajes.append((fila[0], fila[1]))
        conexion.close()
        
        return lista_puntajes
