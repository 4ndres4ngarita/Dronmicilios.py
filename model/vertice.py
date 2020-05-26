SI_ES_VECINO = True
NO_ES_VECINO = False
class vertice:
    def __init__(self, codigo:str=""):
        self.codigo = codigo
        self.vecinos = []#este atributo deberá ser modificado directamente por un grafo
    
    def añadirVecino(self, nuevoVecino:str):
        noEsVecino = not self.esVecino(nuevoVecino)
        if noEsVecino:
            self.vecinos.append( nuevoVecino)
    
    def quitarVecino(self, vecino:str):
        for vecinoIesimo in self.vecinos:
            if vecinoIesimo == vecino:
                del vecinoIesimo
                break
    
    def esVecino(self, vecino:str):
        respuesta = NO_ES_VECINO
        for vecinoIesimo in self.vecinos:
            if vecinoIesimo == vecino:
                respuesta = SI_ES_VECINO
        return respuesta
    
    def getClon(self):
        return vertice(self.codigo)

    def __str__(self):
        return self.codigo