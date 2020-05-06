import json,sys
sys.path.append("D:/Proyectos/Parcial - 2Corte/")
from model.base import *
from model.comparadoresDeVertices import *
from model.buscadoresDeAristas import *
def __main__():
    vertices = cargarVerticesEnMemoria()
    realizarPruebas_ComparadoresDeVertices_(vertices)
    realizarPruebas_BuscadoresDeAristas_(vertices)
    

#funciones para abstraer datos Json a Objetos
def cargarVerticesEnMemoria():
    #with open("D:/Proyectos/ProyectoIn7egrador/test/graphStage1.json") as json_file:
    documento = importarArchivo( "D:/Proyectos/Parcial - 2Corte/test/graphStage1.json")
    datosJson = importarJsonDesdeArchivo( documento)
    vertices = importarVerticesDesdeJson(datosJson)
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
def importarVerticesDesdeJson( baseDeDatosJson):
    listaDeVertices= []
    for jsonIesimo in baseDeDatosJson["vertices"]:
        nuevoVertice = Vertice(
            jsonIesimo["codigo"],
            jsonIesimo["nombre"]
        )
        listaDeVertices.append( nuevoVertice)
        del nuevoVertice
    return listaDeVertices

def importarPaqueteDeAristasJson( baseDeDatosJson, codigoDelVertice:str):
    paqueteDeAristasJson = []
    BaseDeDatosDeAristas = baseDeDatosJson["aristas"]
    for paqueteIesimo in BaseDeDatosDeAristas:
        if paqueteIesimo["vertice"] == codigoDelVertice:
            paqueteDeAristasJson = paqueteIesimo["lista"]
            break
    del BaseDeDatosDeAristas
    return paqueteDeAristasJson
def abstraerAristasJson( paqueteDeAristas, listaDeVertices:list):
    listaDeAristas = []
    for aristaJsonIesimo in paqueteDeAristas:
        nuevaArista = Arista()
        nuevaArista.setCostos( aristaJsonIesimo["costo"])
        nuevaArista.setNumeroDeArista(aristaJsonIesimo["numeroDeArista"])
        for verticeIesimo in listaDeVertices:
            if verticeIesimo.getCodigo() == aristaJsonIesimo["verticeConectado"]:
                nuevaArista.setVerticeConectado( verticeIesimo)
                break
        listaDeAristas.append( nuevaArista)
    return listaDeAristas
def importarAristasDeUnVertice( baseDeDatosJson, codigoDelVertice:str, listaDeVertices:list):
    paqueteDeAristasEnCrudo = importarPaqueteDeAristasJson( baseDeDatosJson, codigoDelVertice)
    listaDeAristas = abstraerAristasJson( paqueteDeAristasEnCrudo, listaDeVertices)
    return listaDeAristas
def importarAristasDesdeJson( baseDeDatosJson, listaDeVertices:list):
    for verticeIesimo in listaDeVertices:
        listaDeAristas = importarAristasDeUnVertice(
            baseDeDatosJson,
            verticeIesimo.getCodigo(), 
            listaDeVertices)
        verticeIesimo.setListaDeAristas( listaDeAristas)

def presentarVertice( vertice:Vertice):
    print(
        "{ codigo : "+ vertice.getCodigo() +
        ", nombre : "+ vertice.getNombre() +
        ", numero de aristas : "+ str(len(vertice.getListaDeAristas()))+
        " }"
    )
def presentarVertices( listaDeVertices:list):
    for verticeIesimo in listaDeVertices:
        presentarVertice( verticeIesimo)


#funciones de pruebas
def realizarPruebas_ComparadoresDeVertices_( vertices):
    n1 = vertices[0]
    n2 = vertices[1]
    n3 = vertices[2]
    n4 = vertices[3]
    n1copia = vertices[0]
    if(
        not ComparadorDeVerticesPorCodigo.sonIguales( n1,n2) and
        not ComparadorDeVerticesPorNombre.sonIguales( n1,n3) and
        not ComparadorDeVerticesPorListaDeAristas.sonIguales(n2,n3) and
        not ComparadorDeVertices.sonVerticesIdenticos( n1, n2) and
        ComparadorDeVertices.sonVerticesIdenticos(n1, n1copia)
    ):
        print("test comparadoresDeVertices : okey!")
    else:
        print("test comparadoresDeVertices: not okey :/")
def realizarPruebas_BuscadoresDeAristas_( vertices):
    n1 = vertices[0]
    n2 = vertices[1]
    n3 = vertices[2]
    n4 = vertices[3]
    buscadorPorVerticesEn_n1 = BuscadorDeAristasPorVertice( n1.getListaDeAristas())
    buscadorPorCodigoDeVerticeEn_n1 = BuscadorDeAristasPorCodigoDelVertice( n1.getListaDeAristas())
    subTest1 = (
        buscadorPorVerticesEn_n1.getAristas( n2) ==
        buscadorPorCodigoDeVerticeEn_n1.getAristas( n2.getCodigo())
    )
    buscadorPorCodigoDeVerticeEn_n3 = BuscadorDeAristasPorCodigoDelVertice( n3.getListaDeAristas())
    aristasDeN3conN2 = buscadorPorCodigoDeVerticeEn_n3.getAristas( "2")
    buscadorPorNumeroDeAristaEn_n3 = BuscadorDeAristasPorNumeroDeArista( aristasDeN3conN2)
    subTest2 = len(buscadorPorNumeroDeAristaEn_n3.getAristas( 1)) == 1
    if( subTest1 and subTest2):
        print("test buscadoresDeAristas : okey!")
    else:
        print("test buscadoresDeAristas : not okey :/")
__main__()