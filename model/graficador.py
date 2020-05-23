from model.vertice import *
from model.arista import *
from model.grafo import *
from model.vias import *
import networkx as nx

def showGrafo(pgrafo:grafo):#showGrafico
    
    G=nx.Graph()
    nodo_anterior = ""
    for nodo in pgrafo.verticesV:
        G.add_node(nodo.codigo,pos=(nodo.direccion['calle'],nodo.direccion['carrera']))
        print("codigo: ",nodo.codigo,"calle: ",nodo.direccion['calle'],"carrera: ",nodo.direccion['carrera'])
        
        for vecino in nodo.vecinos:
            if nodo.codigo != nodo_anterior:
                G.add_edge
                
        nodo_anterior = nodo.codigo
    
    pos=nx.get_node_attributes(G,"pos")    
    nx.draw(G,pos,with_labels=True )