try:
    from vertice import *
except:
    from model.vertice import *

class arista:
    def __init__(self, verticeU:vertice = vertice(), verticeV:vertice = vertice(), costo:float = 0.0):
        self.vertices = {"u":verticeU,"v":verticeV}
        self.costo = costo
    
    def estaElVertice(self, verticeBuscado:vertice):
        respuesta = (self.vertices["u"] == verticeBuscado or 
            self.vertices["v"] == verticeBuscado)
        return respuesta
    
    def getVerticeVecino(self, vertice:vertice):
        if self.vertices["u"] == vertice:
            return self.vertices["v"]
        elif self.vertices["v"] == vertice:
            return self.vertices["u"]

    def __str__(self):
        return "("+self.vertices["u"].codigo+ ","+self.vertices["v"].codigo+")"