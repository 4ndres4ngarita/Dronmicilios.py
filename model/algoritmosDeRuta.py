try:
    from model.vertice import *
    from model.arista import *
    from model.grafo import *
    from model.algoritmosDeRecorrido import *
    from model.algoritmosDeOrdenamiento import *
except:
    #from vertice import *
    pass

class IAlgoritmoDeRuta:
    def getGrafoDeRutaMinima(self, grafoBase:grafo):
        pass
    def getCostoTotalDeRutaMinima(self):
        pass

class Kruskal(IAlgoritmoDeRuta):
    def __init__(self):
        super().__init__()
        self.grafoDeEstudio = grafo([],[])
        self.__grafoDeRutaMinima = grafo([],[])

    def getGrafoDeRutaMinima(self, grafoBase:grafo):
        self.grafoDeEstudio = grafoBase
        if self.estaTotalmenteConectado( DepthFirstSearch):
            self.ordenarAristas(selectionSort)
            for aristaIesima in self.grafoDeEstudio.aristasE:
                if not self.estanSusVerticesAñadidos( aristaIesima):
                    print("toca añadir la arista : " + str(aristaIesima) + "porque no existen uno de los dos vertices")
                    self.agregarAristaYvertices( aristaIesima)
                elif (not self.existeRutaEntreVertices(
                        aristaIesima, DepthFirstSearch)):
                        print("toca añadir la arista : " + str(aristaIesima) + "porque no existen una ruta para uno de los dos vertices")
                        self.agregarAristaYvertices( aristaIesima)
        return self.__grafoDeRutaMinima
    
    def getCostoTotalDeRutaMinima(self):
        costoTotal = 0.0
        for aristaIesima in self.__grafoDeRutaMinima.aristasE:
            costoTotal += aristaIesima.costo
        return costoTotal

    def estaTotalmenteConectado(self, algoritmo:IAlgoritmoDeRecorrido):
        algoritmoDeRecorrido = algoritmo()
        return algoritmoDeRecorrido.estaTotalmenteConectado(
            self.grafoDeEstudio, self.grafoDeEstudio.verticesV[0])

    def ordenarAristas(self, algoritmo:IAlgoritmoDeOrdenamiento):
        algoritmo.ordenarAristas(self.grafoDeEstudio.aristasE)

    def estanSusVerticesAñadidos(self, aristaPrueba:arista):
        estaUsandoVerticeU = self.__grafoDeRutaMinima.existeVertice(
            aristaPrueba.vertices["u"].codigo)
        estaUsandoVerticeV = self.__grafoDeRutaMinima.existeVertice(
            aristaPrueba.vertices["v"].codigo)
        respuesta = estaUsandoVerticeU and estaUsandoVerticeV
        return respuesta

    def existeRutaEntreVertices(self, aristaPrueba:arista, algoritmo:IAlgoritmoDeRecorrido):
        algoritmoImplementado = algoritmo()
        respuesta = algoritmoImplementado.existeRutaEntre( 
            aristaPrueba.vertices["u"].codigo,
            aristaPrueba.vertices["v"].codigo,
            self.__grafoDeRutaMinima)
        return respuesta

    def agregarAristaYvertices(self, aristaNueva:arista):#no esta completo
        #if not self.__grafoDeRutaMinima.existeVertice(aristaNueva.vertices["u"]):
        self.__grafoDeRutaMinima.añadirVertice( aristaNueva.vertices["u"])
        self.__grafoDeRutaMinima.añadirVertice( aristaNueva.vertices["v"])
        self.__grafoDeRutaMinima.añadirArista( aristaNueva)
    
    def calcularCostoTotal(self):
        pass
    
    def __estaUsado(self, verticeBuscado:vertice):
        respuesta = False
        for i in self.__grafoDeRutaMinima.verticesV:
            if i == verticeBuscado:
                respuesta = True
                break
        return respuesta