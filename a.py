from model.vertice import *
from model.arista import *
from model.grafo import *
from model.algoritmosDeExpansion import *
from model.algoritmosDeExploracion import *
from model.algoritmosDeOrdenamiento import *
from model.algoritmosDeRuta import *
from grafoDeClientes import MAPA, EMPRESA_J

miDijkstra = dijkstra( MAPA)
miDijkstra.ejecutar( EMPRESA_J)