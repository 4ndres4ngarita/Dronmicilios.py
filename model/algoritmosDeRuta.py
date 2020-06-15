import sys
from model.vertice import *
from model.arista import *
from model.grafo import *

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def imprimirSolucion(self, distancias): 
        print("Tabla de Costos")

        nombresDeVertices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

        for node in range(self.V): 
            print(nombresDeVertices[node], "\t", distancias[node] )
  
    def minimaDistancia(self, distancias, sptSet): 

        minimoCosto = sys.maxsize
 
        for v in range(self.V): 
            if distancias[v] < minimoCosto and sptSet[v] == False: 
                minimoCosto = distancias[v] 
                minimoCosto_index = v 
  
        return minimoCosto_index

    def dijkstra(self, src): 
  
        distancias = [sys.maxsize] * self.V 
        distancias[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V):
            u = self.minimaDistancia(distancias, sptSet)
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and (
                distancias[v] > distancias[u] + self.graph[u][v]): 
                        distancias[v] = distancias[u] + self.graph[u][v] 
  
        self.imprimirSolucion(distancias)

class IAlgoritmoDeRuta:
    pass

class dijkstra(IAlgoritmoDeRuta):

    def __init__(self, grafoBase:grafo):
        super().__init__()
        self.grafoBase = grafoBase
        self.rutas = []
        self.pilaDeLlamada = []

    def ejecutar(self, verticeRaiz:vertice):
        etiquetaVerticeRaiz = self.crearEtiqueta( verticeRaiz.codigo,0.0, 0.0, None)
        self.pilaDeLlamada.append( etiquetaVerticeRaiz)
        existenLlamadas = True if len(self.pilaDeLlamada) > 0 else False
        while existenLlamadas:
            llamadaEntrante = self.pilaDeLlamada.pop(0)
            aristasConVecinos = self.grafoBase.buscarAristasConVertice( self.grafoBase.getVertice(llamadaEntrante['codigo']))
            for aristaConVecinoI in aristasConVecinos:
                costoAcumulado = llamadaEntrante['costoTotal']
                vecino = aristaConVecinoI.getVerticeVecino( llamadaEntrante['codigo'])
                costoAcumulado += aristaConVecinoI.costo
                """
                if self.noExisteEtiquetaPara(vecino.codigo):
                    nuevaEtiquetaParaVecino = self.crearEtiqueta( vecino.codigo, aristaConVecinoI.costo, costoAcumulado, llamadaEntrante['codigo'])
                    self.añadirEnPila( nuevaEtiquetaParaVecino)
                elif self.estaEnLaPila(vecino.codigo) and costoAcumulado < llamadaEntrante['costoTotal']:
                    llamadaEntrante['costoTotal'] = costoAcumulado
                """
            self.rutas.append(llamadaEntrante)
            existenLlamadas = True if len(self.pilaDeLlamada) > 0 else False

    def crearEtiqueta(self, codigo, costoBase, costoTotal, verticePredecesor):
        return {
            'codigo' : codigo,
            'costoBase' : costoBase,
            'costoTotal' : costoTotal,
            'predecesor' : verticePredecesor
        }

    def noExisteEtiquetaPara(self, codigoVertice):
        if not self.estaEnLaPila( codigoVertice) and not self.estaPermanente( codigoVertice):
            return True
        else:
            return False
    
    def estaEnLaPila(self, codigoVertice):
        estaEnLaPila = False
        for etiquetaI in self.pilaDeLlamada:
            if etiquetaI['codigo'] == codigoVertice:
                estaEnLaPila = True
                break
        return estaEnLaPila

    def estaPermanente(self, codigoVertice):
        estaEnLaPila = False
        for etiquetaI in self.rutas:
            if etiquetaI['codigo'] == codigoVertice:
                estaEnLaPila = True
                break
        return estaEnLaPila
    
    def añadirEnPila(self, etiquetaNueva):
        for i in range( 0, len(self.pilaDeLlamada)):
            etiquetaI = self.pilaDeLlamada[i]
            if etiquetaNueva['costoTotal'] < etiquetaI['costoTotal']:
                self.pilaDeLlamada.insert( i, etiquetaNueva)
                break