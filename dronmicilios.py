from model.base import *
from model.depthFirstSearch import *
import time
def getVerticesDesdeCSV( archivo):
    vertices = {}
    siguienteCodigo = 1
    for lineaIesima in archivo:

        nombreNuevoVertice = getNombre(lineaIesima.strip())
        nuevoVertice = Vertice( siguienteCodigo, nombreNuevoVertice)
        vertices[siguienteCodigo] = nuevoVertice
        siguienteCodigo += 1
    archivo.close()
    return vertices

def agregarAristasDesdeCSV(archivo, vertices:dict):
    longitudMatrizAdyacencia = len(vertices)
    codigoVerticeBase = 1    
    for lineaIesima in archivo:
        posicionInicio = getLongitudDeNombre( lineaIesima) + 1
        posicionSiguiente = posicionInicio
        codigoArista = 1
        for columnaIesima in range(0, longitudMatrizAdyacencia):
            caracterSiguiente = lineaIesima[posicionSiguiente]
            if caracterSiguiente == "1":
                verticeConectado = vertices[ codigoArista ]
                nuevaArista = Arista()
                nuevaArista.setVerticeConectado( verticeConectado)
                verticeBase = vertices[codigoVerticeBase]
                verticeBase.añadirArista( nuevaArista)
            posicionSiguiente += 2
            codigoArista += 1
        codigoVerticeBase += 1
    archivo.close()

def importarGrafoDesdeCSV(rutaArchivo):
    grafo = Grafo()
    vertices = getVerticesDesdeCSV( open(rutaArchivo))
    grafo.setVertices( vertices)
    agregarAristasDesdeCSV( open(rutaArchivo), grafo.getVertices())
    return grafo

def getNombre( linea:str):
    posicionDelCaracter = 0
    nombre = ""
    while linea[posicionDelCaracter] != ";":
        nombre += linea[posicionDelCaracter]
        posicionDelCaracter += 1
    return nombre

def getLongitudDeNombre( linea:str):
    posicionDelCaracter = 0
    contador = 0
    while linea[contador] != ";":
        contador += 1
    return contador

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
tiempoInicio = time.time()
ruta = "doc/Adyacencia.csv"
grafo = importarGrafoDesdeCSV( ruta)
imprimirBanner()

semilla = grafo.getVertice(1)
dfs = BuscadorDepthFirst( grafo, semilla)
dfs.ejecutarBusqueda()

tiempoFin = time.time()
print("inicio : "+str(tiempoInicio)+"\n"
    +"fin : "+str(tiempoFin)+"\n"
    +"diferencia : "+str(tiempoFin - tiempoInicio))