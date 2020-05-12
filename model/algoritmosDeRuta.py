try:
    from vertice import *
    from arista import *
    from grafo import *
    from algoritmosDeRecorrido import *
    from algoritmosDeOrdenamiento import *
except:
    from model.vertice import *
    from model.arista import *
    from model.grafo import *
    from model.algoritmosDeRecorrido import *
    from model.algoritmosDeOrdenamiento import *

class IAlgoritmoDeRuta:
    def ejecutarAlgoritmo(self):
        pass
    def getGrafoDeRutaMinima(self):
        pass

class Kruskal(IAlgoritmoDeRuta):
    def __init__(self, grafoBase:grafo):
        super().__init__()
        self.grafoDeEstudio = grafoBase
        self.grafoConRutaMinima = grafo()

    def estaTotalmenteConectado(self):
        dfs = DepthFirstSearch(self.grafoDeEstudio, self.grafoDeEstudio.verticesV[0])
        dfs.ejecutarAlgoritmo()
        respuesta = dfs.estaTotalmenteConectado()
        return respuesta

    def susVerticesEstanUsadas(self, aristaPrueba:arista):
        respuesta:bool
        estaUsadoVerticeU = self.__estaUsado(
            aristaPrueba.vertices["u"])
        estaUsadoVerticeV = self.__estaUsado(
            aristaPrueba.vertices["v"])
        respuesta = estaUsadoVerticeU and estaUsadoVerticeV
        return respuesta

    def ordenarAristas(self, algoritmo:IAlgoritmoDeOrdenamiento):
        algoritmo.ordenarAristas(self.grafoDeEstudio.aristasE)

    def existeRutaEntreVertices(self, aristaPrueba:arista, algoritmo:IAlgoritmoDeRecorrido):
        algoritmoImplementado = algoritmo( self.grafoConRutaMinima, vertice())
        respuesta = algoritmoImplementado.existeRutaCon( 
            aristaPrueba.vertices["u"],
            aristaPrueba.vertices["v"])
        return respuesta

    def agregarAristaYvertices(self, aristaNueva:arista):
        pass

    def calcularCostoTotal(self):
        pass
    
    def __estaUsado(self, verticeBuscado:vertice):
        for i in self.grafoConRutaMinima.verticesUsados:
            if i == verticeBuscado:
                return True
        return False

va = vertice("a",["b","c"])
vb = vertice("b",["a"])
vc = vertice("c",["a"])
aab = arista(va,vb,5)
aca = arista(vc,va,2)
g = grafo([va,vb,vc],[aab,aca])
k = Kruskal(g)
#cuerpo del algoritmo
print(k.estaTotalmenteConectado())#Determinar si esta totalmente conectado
ss = selectionSort()
k.ordenarAristas(ss)
print(k.existeRutaEntreVertices( aab, DepthFirstSearch))

print("Okey! 😀")