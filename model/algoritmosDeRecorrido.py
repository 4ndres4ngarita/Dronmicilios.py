from model.vertice import *
from model.arista import *
from model.grafo import *

NO_VISITADO=0
PARCIALMENTE_VISITADO=2
TOTALMENTE_VISITADO = 1

class IAlgoritmoDeRecorrido:
    def existeRutaEntre(self, verticeInicio:str, verticeDestino:str, grafoBase:grafo):
        pass
    def estaTotalmenteConectado(self, grafoBase:grafo, verticeSemilla:vertice):
        pass

class DepthFirstSearch(IAlgoritmoDeRecorrido):
    def __init__(self):
        super().__init__()
        self.diccionarioDeVisitas = {}
        

    def __alistarDiccionarioDeVisitas(self, grafoBase:grafo):
        diccionarioNuevo = {}
        for verticeIesimo in grafoBase.verticesV:
            diccionarioNuevo[verticeIesimo.codigo] = NO_VISITADO
        self.diccionarioDeVisitas = diccionarioNuevo
    
    def __visitar(self, verticeSemilla:vertice, grafoBase:grafo):
        print("vertice '"+verticeSemilla.codigo+"' parcialmente visitado")
        self.diccionarioDeVisitas[verticeSemilla.codigo] = PARCIALMENTE_VISITADO

        listaDeAristas = grafoBase.buscarAristasConVertice(verticeSemilla)
        for aristaIesima in listaDeAristas:
            verticeVecino = aristaIesima.getVerticeVecino( verticeSemilla)
            if self.diccionarioDeVisitas[verticeVecino.codigo] == NO_VISITADO:
                self.__visitar(verticeVecino, grafoBase)

        self.diccionarioDeVisitas[verticeSemilla.codigo] = TOTALMENTE_VISITADO
        print("vertice '"+verticeSemilla.codigo+"' totalmente visitado")
    
    def estaTotalmenteConectado(self, grafoBase:grafo, verticeSemilla:vertice):
        respuesta = True
        self.__alistarDiccionarioDeVisitas( grafoBase)
        self.__visitar( verticeSemilla, grafoBase)
        for unVerticeIesimo in self.diccionarioDeVisitas.values():
            if unVerticeIesimo is NO_VISITADO:
                respuesta = False
                break
        return respuesta

    def existeRutaEntre(self, verticeInicio:str, verticeDestino:str, grafoBase:grafo):
        self.__alistarDiccionarioDeVisitas( grafoBase)
        return self.__existeRutaCon(
            grafoBase.getVertice( verticeInicio),
            grafoBase.getVertice( verticeDestino),
            grafoBase)

    def __existeRutaCon(self, verticeInicio:vertice, verticeDestino:vertice, grafoBase:grafo):
        respuesta = False
        self.diccionarioDeVisitas[verticeInicio.codigo] = PARCIALMENTE_VISITADO
        for codigoVecinoIesimo in verticeInicio.vecinos:
            verticeVecino = grafoBase.getVertice(codigoVecinoIesimo)
            if verticeVecino == verticeDestino:
                respuesta = True
                break
            elif self.diccionarioDeVisitas[codigoVecinoIesimo] == NO_VISITADO:
                respuesta = self.__existeRutaCon( verticeVecino, verticeDestino, grafoBase)
            if respuesta:
                break
        return respuesta