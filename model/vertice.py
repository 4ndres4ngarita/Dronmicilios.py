SI_ES_VECINO = True
NO_ES_VECINO = False
class vertice:
    def __init__(self, codigo:str="", calle = 0.0, carrera = 0.0):
        self.codigo = codigo
        self.vecinos = []#este atributo deberá ser modificado directamente por un grafo
        self.direccion = {
            "calle": calle,
            "carrera": carrera
        }
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
    
    def copiarAtributos(self, verticeBase):#copiarAtributos
        self.codigo = verticeBase.codigo
        self.direccion = {
            "calle": verticeBase.direccion['calle'],
            "carrera": verticeBase.direccion['carrera']
        }

    def __str__(self):
        return self.codigo