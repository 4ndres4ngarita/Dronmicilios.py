try:
    from base import *
except:
    from model.base import *

#region status values
NO_VISITADO=0
PARCIALMENTE_VISITADO=2
TOTALMENTE_VISITADO = 1
#endregion

class BuscadorDepthFirst:
    def __init__(self, grafo:IGrafo, verticeSemilla:IVertice):
        self.grafo = grafo
        self.verticeInicio = verticeSemilla

    def ejecutarBusqueda(self):
        verticesPorVisitar = self.getDiccionarioDeVisitas()
        self.__visitar( self.verticeInicio, verticesPorVisitar)

    def getDiccionarioDeVisitas(self):
        diccionarioDeVisitas = {}
        for codigoDeVertice in self.grafo.getVertices():
            diccionarioDeVisitas[codigoDeVertice] = NO_VISITADO
        return diccionarioDeVisitas

    def __visitar(self, vertice:IVertice, dictDeVisitas:dict):
        print("vertice '"+vertice.getNombre()+"' parcialmente visitado")
        dictDeVisitas[vertice.getCodigo()] = PARCIALMENTE_VISITADO
        listaDeAristas = vertice.getListaDeAristas()
        for aristaIesima in listaDeAristas:
            verticeVecino = self.__getVerticeVecino( aristaIesima)
            if dictDeVisitas[verticeVecino.getCodigo()] == NO_VISITADO:
                self.__visitar(verticeVecino, dictDeVisitas)

        dictDeVisitas[vertice.getCodigo()] = TOTALMENTE_VISITADO
        print("vertice '"+vertice.getNombre()+"' totalmente visitado")
    
    def __getVerticeVecino(self, aristaIesima:IArista):
        return aristaIesima.getVerticeConectado()
        