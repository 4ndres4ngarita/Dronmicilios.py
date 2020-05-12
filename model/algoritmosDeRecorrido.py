try:
    from vertice import *
    from arista import *
    from grafo import *
except:
    from model.vertice import *
    from model.arista import *
    from model.grafo import *

NO_VISITADO=0
PARCIALMENTE_VISITADO=2
TOTALMENTE_VISITADO = 1

class IAlgoritmoDeRecorrido:
    def __init__(self, grafoBase:grafo, verticeSemilla:vertice):
        self.grafoBase = grafoBase
        self.verticeInicio = verticeSemilla
    def ejecutarAlgoritmo(self):
        pass
    def existeRutaCon(self, verticeInicio:vertice, verticeDestino:vertice):
        pass
    def estaTotalmenteConectado(self):
        pass

class DepthFirstSearch(IAlgoritmoDeRecorrido):
    def __init__(self, grafoBase:grafo, verticeSemilla):
        super().__init__(grafoBase, verticeSemilla)
        self.diccionarioDeVisitas = {}
        self.__resetDiccionarioDeVisitas()

    def __resetDiccionarioDeVisitas(self):
        diccionarioNuevo = {}
        for verticeIesimo in self.grafoBase.verticesV:
            diccionarioNuevo[verticeIesimo.codigo] = NO_VISITADO
        self.diccionarioDeVisitas = diccionarioNuevo

    def ejecutarAlgoritmo(self):
        self.__visitar( self.verticeInicio)
    
    def __visitar(self, verticeSemilla:vertice):
        print("vertice '"+verticeSemilla.codigo+"' parcialmente visitado")
        self.diccionarioDeVisitas[verticeSemilla.codigo] = PARCIALMENTE_VISITADO

        listaDeAristas = self.grafoBase.buscarAristasConVertice(verticeSemilla)
        for aristaIesima in listaDeAristas:
            verticeVecino = self.__getVerticeVecino( aristaIesima, verticeSemilla)
            if self.diccionarioDeVisitas[verticeVecino.codigo] == NO_VISITADO:
                self.__visitar(verticeVecino)

        self.diccionarioDeVisitas[verticeSemilla.codigo] = TOTALMENTE_VISITADO
        print("vertice '"+verticeSemilla.codigo+"' totalmente visitado")
    
    def __getVerticeVecino(self, arista:arista, vertice:vertice):
        return arista.getVerticeVecino(vertice)
    
    def estaTotalmenteConectado(self):
        respuesta = True
        for unVerticeIesimo in self.diccionarioDeVisitas.values():
            if unVerticeIesimo is NO_VISITADO:
                respuesta = False
                break
        return respuesta

    def existeRutaCon(self, verticeInicio:vertice, verticeDestino:vertice):
        self.__resetDiccionarioDeVisitas()
        return self.__existeRuta( verticeInicio, verticeDestino)

    def __existeRuta(self, verticeInicio:vertice, verticeDestino:vertice):
        respuesta = False
        self.diccionarioDeVisitas[verticeInicio.codigo] = PARCIALMENTE_VISITADO
        for codigoVecinoIesimo in verticeInicio.vecinos:
            verticeVecino = self.grafoBase.buscarVertice(codigoVecinoIesimo)
            if verticeVecino == verticeDestino:
                respuesta = True
                break
            elif self.diccionarioDeVisitas[codigoVecinoIesimo] == NO_VISITADO:
                respuesta = self.__existeRuta( verticeVecino, verticeDestino)
        return respuesta


"""
#test
va = vertice("a",["b","c"])
vb = vertice("b",["a"])
vc = vertice("c",["a"])
aab = arista(va,vb,5)
aca = arista(vc,va,2)
g = grafo([va,vb,vc],[aab,aca])
dfs = DepthFirstSearch(g,g.verticesV[0])
dfs.ejecutarAlgoritmo()
print(dfs.estaTotalmenteConectado())
print(dfs.existeRutaCon( vb, vc))
"""