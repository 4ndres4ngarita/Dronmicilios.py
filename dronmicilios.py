from model.vertice import *
from model.arista import *
from model.grafo import *
from model.depthFirstSearch import *
from model.ordenamiento import *
import time
def getVerticesDesdeCSV( archivo):
    vertices = []
    for lineaIesima in archivo:

        codigoNuevoVertice = getCodigoDeVertice(lineaIesima.strip())
        nuevoVertice = vertice(codigoNuevoVertice)
        vertices.append( nuevoVertice)
    archivo.close()
    return vertices

def getAristasDesdeCSV(archivo, vertices:list):
    aristas = []
    longitudMatrizAdyacencia = len(vertices)
    posicionVerticeU = 0
    
    for lineaIesima in archivo:
        posicionVerticeV = 1 + posicionVerticeU
        columnaInicio = getLongitudDeNombre( lineaIesima) + 1 + (posicionVerticeV * 2)
        columnaFin = len(lineaIesima)
        for columnaIesima in range( columnaInicio , columnaFin, 2):
            siguienteColumna = lineaIesima[columnaIesima]
            if siguienteColumna == '1':
                nuevaArista = arista()
                verticeU = vertices[posicionVerticeU]
                verticeV = vertices[posicionVerticeV]
                verticeU.añadirVecino( verticeV.codigo)
                verticeV.añadirVecino( verticeU.codigo)
                nuevaArista.vertices["u"] = verticeU
                nuevaArista.vertices["v"] = verticeV
                aristas.append( nuevaArista)
            posicionVerticeV += 1
        posicionVerticeU += 1
    del posicionVerticeU
    del posicionVerticeV
    archivo.close()
    return aristas
    
def importarGrafoDesdeCSV(rutaArchivo):
    verticesAbstraidos = getVerticesDesdeCSV( open(rutaArchivo))
    aristasAbstraidas = getAristasDesdeCSV( open(rutaArchivo), verticesAbstraidos)
    return grafo(verticesAbstraidos, aristasAbstraidas)

def getCodigoDeVertice( linea:str):
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

semilla = grafo.buscarVertice('A')
dfs = BuscadorDepthFirst( grafo,semilla)
dfs.ejecutarBusqueda()
tiempoFin = time.time()
print("inicio : "+str(tiempoInicio)+"\n"
    +"fin : "+str(tiempoFin)+"\n"
    +"diferencia : "+str(tiempoFin - tiempoInicio))