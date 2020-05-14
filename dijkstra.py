from model.vertice import *
from model.arista import *
from model.grafo import *
from model.algoritmosDeOrdenamiento import selectionSort
from grafoDeClientes import MAPA, EMPRESA_J

def existenVisitasPendientes( direcciones:dict):
    respuesta = True
    for codigoVerticeI in direcciones:
        estaVisitado = direcciones[codigoVerticeI]['estaVisitado']
        if not estaVisitado:
            respuesta = False
            break
    return respuesta

def dijkstra_v1( grafo, raiz):#pagina 175 del libro
    direcciones:dict = {}
    u:str = raiz.codigo

    for verticeI in grafo.vertices:
        direcciones[verticeI.codigo] = {
            'costo': float('inf'),
            'predecesor': None,
            'estaVisitado':False
        }

    direcciones[raiz.codigo]['costo'] = 0.0

    selectionSort.ordenarLista()

    while existenVisitasPendientes( direcciones):#vertices sin visitar

        for codigoVerticeI in direcciones:
            estaVisitado = direcciones[codigoVerticeI]['estaVisitado']
            esVerticeImenorQueU = (
                direcciones[codigoVerticeI]['costo'] < direcciones[u]['costo']
            )
            if esVerticeImenorQueU and not estaVisitado:
                u = codigoVerticeI# este es el vertice, no visitado, con el menor peso.
        
        
        direcciones[u]['estaVisitado'] = True

        for codigoVecinoI in grafo.getVertice(u).vecinos:
            costoParaIrAlVecino = grafo.buscarAristasConVertices( u, codigoVecinoI)
            nuevoCostoAlternativo = direcciones[u]['costo'] + costoParaIrAlVecino
            if nuevoCostoAlternativo < direcciones[codigoVecinoI]['costo']:
                direcciones[codigoVecinoI]['costo'] = nuevoCostoAlternativo
                direcciones[codigoVecinoI]['predecesor'] = u
    
    return direcciones

tablaDeDireccionesParaJ = dijkstra_v1( MAPA, EMPRESA_J)

"""
-------------------------WARNING-------------------------
                    CODIGO NO PROVADO
"""