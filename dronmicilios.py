from model.vertice import *
from model.arista import *
from model.grafo import *
from model.algoritmosDeRuta import *
from model.algoritmosDeRecorrido import *
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

print("inicio")

semilla = MAPA.getVertice('J')
imprimirBanner()

#test algoritmo Depth Fisrt Search

dfs = DepthFirstSearch()

print("inicio del algoritmo Depth Fisrt Search")
print("\n\n")
tiempoInicio = time.time()#inicio conteo del tiempo
dfs.estaTotalmenteConectado( MAPA, semilla)
tiempoFin = time.time()#fin del tiempo
dfs.imprimirRecorrido()
print("\n\n")
print("\tTiempo del agloritmo (Depth Fisrt Search):")
print("\t\tinicio : "+str(tiempoInicio)+"\n"
    +"\t\tfin : "+str(tiempoFin)+"\n"
    +"\t\tdiferencia : "+str(tiempoFin - tiempoInicio))

print("\n\n")

#test algoritmo Kruskal
mspKrustal = Kruskal()
print("inicio del algoritmo Kruskal")
print("\n")
tiempoInicio = time.time()#inicio conteo del tiempo
grafoDeRutasMinimas = mspKrustal.getGrafoDeRutaMinima(MAPA)
tiempoFin = time.time()#fin del tiempo
print("\n\n")
print("\tTiempo del agloritmo (Kruskal):")
print("\t\tinicio : "+str(tiempoInicio)+"\n"
    +"\t\tfin : "+str(tiempoFin)+"\n"
    +"\t\tdiferencia : "+str(tiempoFin - tiempoInicio))

print(grafoDeRutasMinimas)
print("el costo total del grafo con las rutas minimas es : " + str(mspKrustal.getCostoTotalDeRutaMinima()))