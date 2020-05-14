from model.vertice import *
from model.arista import *
from model.grafo import *

class IAlgoritmoDeRuta:
    def getGrafoDeRutaMinimaPara(self, vertice:vertice, grafoBase:grafo):
        pass
    def getRutaPara(self, inicio:vertice, fin:vertice, grafoBase:grafo):
        pass

class Dijkstra(IAlgoritmoDeRuta):
    def __init__(self):
        super().__init__()
        self.verticeRaiz:vertice = None
        self.direcciones:list = []
        self.grafoBase:grafo = None

    def getGrafoDeRutaMinimaPara(self, vertice:vertice, grafoBase:grafo):
        verticesParaVisitar = grafoBase.verticesV
        for verticeIesimo in grafoBase.verticesV:
            verticeIesimo:vertice
            distancias[verticeIesimo.codigo] = 0.0
        

        while verticesParaVisitar != []:
            break

    def getCostoHasta(self, destino:str):
        costoTotal = 0
        destino = self.direcciones
    def __cargarDirecciones(self):
        for verticeIesimo in self.grafoBase.verticesV:
            verticeIesimo:vertice
            if verticeIesimo != self.verticeRaiz:
                nuevaDireccion = {
                    'destino':verticeIesimo.codigo,
                    'costo':0.0,
                    'predecesor':''
                }
                self.direcciones.append( nuevaDireccion)