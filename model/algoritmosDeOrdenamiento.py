from model.arista import *

class IAlgoritmoDeOrdenamiento:
    @staticmethod
    def ordenarAristas( aristas:list):
        pass
    @staticmethod
    def ordenarLista( arrayA:list):
        pass
    @staticmethod
    def ordenarDireccionesDijkstra( direcciones:dict):
        pass

class selectionSort( IAlgoritmoDeOrdenamiento):
    @staticmethod
    def ordenarAristas( aristas:list):
        for i in range(len(aristas)):
            posicionAristaMenor = i
            for j in range(i+1, len(aristas)):
                if aristas[posicionAristaMenor].costo > aristas[j].costo: 
                    posicionAristaMenor = j
            aristas[i], aristas[posicionAristaMenor] = aristas[posicionAristaMenor], aristas[i]
    @staticmethod
    def ordenarLista( arrayA):
        for i in range(len(arrayA)): 
      
            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, len(arrayA)): 
                if arrayA[min_idx] > arrayA[j]: 
                    min_idx = j 
                    
            # Swap the found minimum element with  
            # the first element         
            arrayA[i], arrayA[min_idx] = arrayA[min_idx], arrayA[i]
    @staticmethod
    def ordenarDireccionesDijkstra( direcciones:dict):
        for i in range(len(direcciones)):
            posicionLessCostAdress = i# posicion de la direccion con el menor costo
            for j in range(i+1, len(direcciones)):
                if direcciones[posicionLessCostAdress]['costo'] > direcciones[j]['costo'] : 
                    posicionLessCostAdress = j
            direcciones[i], direcciones[posicionLessCostAdress] = direcciones[posicionLessCostAdress], direcciones[i]
