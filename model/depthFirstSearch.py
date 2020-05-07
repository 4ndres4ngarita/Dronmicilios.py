try:
    from base import *
except:
    from model.base import *

class BuscadorDepthFirst:
    def __init__(self, grafo:Grafo, verticeSemilla:Vertice):
        self.mapa = grafo
        self.totalDeVertices = grafo.contarVertices()
        self.__verticeInicio = verticeSemilla
        self.__verticesTotalmenteVisitados = 0

    def ejecutarBusqueda(self):
        vertices = self.mapa.getVertices().values()
        self.__visitar( self.__verticeInicio)

    def __visitar(self, vertice:Vertice):
        print("vertice '"+vertice.getNombre()+"' parcialmente visitado")
        listaDeAristas = vertice.getListaDeAristas()
        vertice.estado = PARCIALMENTE_VISITADO
        for aristaIesima in listaDeAristas:
            verticeVecino = aristaIesima.getVerticeConectado()
            if verticeVecino.estado == NO_VISITADO:
                self.__visitar(verticeVecino)
        self.__verticesTotalmenteVisitados -= 1
        print("vertice '"+vertice.getNombre()+"' totalmente visitado")
        