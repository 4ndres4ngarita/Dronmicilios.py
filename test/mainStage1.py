RUTA_RAIZ = "D:/Proyectos/Dronmicilios.py/"#path del directorio de origen.Mantenga el nombre del directorio plis.

import json,sys
sys.path.append( RUTA_RAIZ)
from model.base import *
from model.comparadoresDeIVertices import *
from model.buscadoresDeAristas import *
def __main__():
    vertices = cargarIVerticesEnMemoria()
    realizarPruebas_ComparadoresDeIVertices_(vertices)
    realizarPruebas_BuscadoresDeAristas_(vertices)
    

#funciones para abstraer datos Json a Objetos
def cargarIVerticesEnMemoria():
    #with open("D:/Proyectos/ProyectoIn7egrador/test/graphStage1.json") as json_file:
    documento = importarArchivo( RUTA_RAIZ+"/graphStage1.json")
    datosJson = importarJsonDesdeArchivo( documento)
    vertices = importarIVerticesDesdeJson(datosJson)
    importarAristasDesdeJson( datosJson, vertices)
    del documento
    del datosJson
    print("Importacion Json cargado :)")
    return vertices
def importarArchivo( rutaDelArchivo:str):
    documento = open( rutaDelArchivo)
    return documento
def importarJsonDesdeArchivo( archivo):
    jsonCrudo = json.load( archivo)
    return jsonCrudo
def importarIVerticesDesdeJson( baseDeDatosJson):
    listaDeIVertices= []
    for jsonIesimo in baseDeDatosJson["vertices"]:
        nuevoIVertice = IVertice(
            jsonIesimo["codigo"],
            jsonIesimo["nombre"]
        )
        listaDeIVertices.append( nuevoIVertice)
        del nuevoIVertice
    return listaDeIVertices

def importarPaqueteDeAristasJson( baseDeDatosJson, codigoDelIVertice:str):
    paqueteDeAristasJson = []
    BaseDeDatosDeAristas = baseDeDatosJson["aristas"]
    for paqueteIesimo in BaseDeDatosDeAristas:
        if paqueteIesimo["vertice"] == codigoDelIVertice:
            paqueteDeAristasJson = paqueteIesimo["lista"]
            break
    del BaseDeDatosDeAristas
    return paqueteDeAristasJson
def abstraerAristasJson( paqueteDeAristas, listaDeIVertices:list):
    listaDeAristas = []
    for aristaJsonIesimo in paqueteDeAristas:
        nuevaArista = Arista()
        nuevaArista.setCostos( aristaJsonIesimo["costo"])
        nuevaArista.setNumeroDeArista(aristaJsonIesimo["numeroDeArista"])
        for verticeIesimo in listaDeIVertices:
            if verticeIesimo.getCodigo() == aristaJsonIesimo["verticeConectado"]:
                nuevaArista.setIVerticeConectado( verticeIesimo)
                break
        listaDeAristas.append( nuevaArista)
    return listaDeAristas
def importarAristasDeUnIVertice( baseDeDatosJson, codigoDelIVertice:str, listaDeIVertices:list):
    paqueteDeAristasEnCrudo = importarPaqueteDeAristasJson( baseDeDatosJson, codigoDelIVertice)
    listaDeAristas = abstraerAristasJson( paqueteDeAristasEnCrudo, listaDeIVertices)
    return listaDeAristas
def importarAristasDesdeJson( baseDeDatosJson, listaDeIVertices:list):
    for verticeIesimo in listaDeIVertices:
        listaDeAristas = importarAristasDeUnIVertice(
            baseDeDatosJson,
            verticeIesimo.getCodigo(), 
            listaDeIVertices)
        verticeIesimo.setListaDeAristas( listaDeAristas)

def presentarIVertice( vertice:IVertice):
    print(
        "{ codigo : "+ vertice.getCodigo() +
        ", nombre : "+ vertice.getNombre() +
        ", numero de aristas : "+ str(len(vertice.getListaDeAristas()))+
        " }"
    )
def presentarIVertices( listaDeIVertices:list):
    for verticeIesimo in listaDeIVertices:
        presentarIVertice( verticeIesimo)


#funciones de pruebas
def realizarPruebas_ComparadoresDeIVertices_( vertices):
    n1 = vertices[0]
    n2 = vertices[1]
    n3 = vertices[2]
    n4 = vertices[3]
    n1copia = vertices[0]
    if(
        not ComparadorDeIVerticesPorCodigo.sonIguales( n1,n2) and
        not ComparadorDeIVerticesPorNombre.sonIguales( n1,n3) and
        not ComparadorDeIVerticesPorListaDeAristas.sonIguales(n2,n3) and
        not ComparadorDeIVertices.sonIVerticesIdenticos( n1, n2) and
        ComparadorDeIVertices.sonIVerticesIdenticos(n1, n1copia)
    ):
        print("test comparadoresDeIVertices : okey!")
    else:
        print("test comparadoresDeIVertices: not okey :/")
def realizarPruebas_BuscadoresDeAristas_( vertices):
    n1 = vertices[0]
    n2 = vertices[1]
    n3 = vertices[2]
    n4 = vertices[3]
    buscadorPorIVerticesEn_n1 = BuscadorDeAristasPorIVertice( n1.getListaDeAristas())
    buscadorPorCodigoDeIVerticeEn_n1 = BuscadorDeAristasPorCodigoDelIVertice( n1.getListaDeAristas())
    subTest1 = (
        buscadorPorIVerticesEn_n1.getAristas( n2) ==
        buscadorPorCodigoDeIVerticeEn_n1.getAristas( n2.getCodigo())
    )
    buscadorPorCodigoDeIVerticeEn_n3 = BuscadorDeAristasPorCodigoDelIVertice( n3.getListaDeAristas())
    aristasDeN3conN2 = buscadorPorCodigoDeIVerticeEn_n3.getAristas( "2")
    buscadorPorNumeroDeAristaEn_n3 = BuscadorDeAristasPorNumeroDeArista( aristasDeN3conN2)
    subTest2 = len(buscadorPorNumeroDeAristaEn_n3.getAristas( 1)) == 1
    if( subTest1 and subTest2):
        print("test buscadoresDeAristas : okey!")
    else:
        print("test buscadoresDeAristas : not okey :/")
__main__()