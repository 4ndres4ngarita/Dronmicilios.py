try:
    from arista import *
except:
    from model.arista import *

class IAlgoritmoDeOrdenamiento:
    def ordenarAristas(self, aristas:list):
        pass

class selectionSort( IAlgoritmoDeOrdenamiento):
    
    def ordenarAristas(self, aristas:list):
        aristaMenor:arista
        for i in range(len(aristas)):
            posicionAristaMenor = i
            for j in range(i+1, len(aristas)):
                if aristas[posicionAristaMenor].costo > aristas[j].costo: 
                    posicionAristaMenor = j
            aristas[i], aristas[posicionAristaMenor] = aristas[posicionAristaMenor], aristas[i]

    def __ordenar(self, arrayA:list = [64, 25, 12, 22, 11] ):
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
        
