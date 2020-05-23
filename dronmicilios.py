from model.vertice import *
from model.arista import *
from model.grafo import *
from model.algoritmosDeExpansion import *
from model.algoritmosDeExploracion import *
from model.algoritmosDeOrdenamiento import *
from grafoDeClientes import MAPA
import time

def imprimirBanner():
    print("\n")
    print("\t ----|---- ----|----")
    print("\t  \==|=========|==/")
    print("\t  /       @       \\")
    print("\t\t / \\")
    print("\t\t/   \\")
    print("\t  [DRONMICILIOS.PY]")
    print("\n")

def provarAlgoritmoDFS( grafo, raiz, repeticiones:int):
    dfs = DepthFirstSearch()
    tiempos = []
    for repeticionDePrueba in range(0, repeticiones):
        tiempoInicio = time.time()#inicio del cronometraje

        dfs.ejecutarArlgoritmo( grafo, raiz)
        print(dfs.estaTotalmenteConectado())
        dfs.imprimirRecorrido()
        tiempoFin = time.time()#fin del cronometraje
        tiempos.append( tiempoFin-tiempoInicio)
    print("prueba completa tiempos totales:")
    print(tiempos)

def provarAlgoritmoBFS( grafo, raiz, repeticiones:int):
    bfs = BreadthFirstSearch()
    tiempos = []
    for repeticionDePrueba in range(0, repeticiones):
        tiempoInicio = time.time()#inicio del cronometraje

        bfs.ejecutarArlgoritmo( grafo, raiz)

        tiempoFin = time.time()#fin del cronometraje
        tiempos.append( tiempoFin-tiempoInicio)
    print("prueba completa tiempos totales:")
    print(tiempos)

def provarAlgoritmoKrustal( grafo, algoritmoDeRecorrido, repeticiones:int):
    algoritmoKrustal = Kruskal()
    tiempos = []
    for repeticionDePrueba in range(0, repeticiones):
        tiempoInicio = time.time()#inicio del cronometraje

        grafoDeRutasMinimas = algoritmoKrustal.getGrafoDeExpansionMinima( grafo, algoritmosDeExploracion=algoritmoDeRecorrido)

        tiempoFin = time.time()#fin del cronometraje
        tiempos.append( tiempoFin-tiempoInicio)
    print("prueba completa tiempos totales:")
    print(tiempos)

print("inicio")

raiz = MAPA.getVertice('J')
imprimirBanner()

#test algoritmo Depth Fisrt Search
provarAlgoritmoDFS( MAPA, raiz, 10)

#test algoritmo Kruskal, con algoritmo dfs
provarAlgoritmoKrustal( MAPA, DepthFirstSearch, 10)

#test algoritmo Breadth Fisrt Search
provarAlgoritmoBFS(MAPA, raiz, 10)