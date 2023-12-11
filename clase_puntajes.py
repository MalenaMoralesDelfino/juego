
class Puntajes:

    def ordenar_puntajes(lista_puntajes:list) -> list:
        '''
        Ordena los puntajes de menor a mayor pasandole por parametro la lista
        de los puntajes y el metodo de ordenamiento
        Parametros:
        -lista_puntajes: lista donde estan guardados los puntajes
        Retorna la lista ordenada de los mismos.
        '''
        lista_ordenada = sorted(lista_puntajes, key=lambda x: x[1])

        return lista_ordenada 