# dronmicilios.py

Considere una  empresa de  domicilios,  que en  tiempos del  **COVID19**,  usa drones  para la  en-trega de pedidos. Los drones tienen un alcance de **2Km** a la redonda desde el punto de partida.Las cuadras son de **100mX100m** y el ancho de las vías es despreciable en este contexto. Parasimplificar la situaci ́on se considera que la sede central de la empresa y los clientes se encuentranen la intersecci ́on entre las carreras (horizontales) y las calles (verticales) en el mapa propuesto.El punto de partida de los drones se encuentra en el nodo **j**. El *archivoGrafo01.csv* ubica tantoa los clientes como a la empresa en la ciudad y el *archivoAdyacencia.csv* presenta la matriz deadyacencia en la situaci ́on descrita. Los desplazamientos entre cada par de nodos adyacentes sehace en l ́ınea recta. N ́otese que las distancias entre cada par de nodos adyacentes, el peso de laarista, debe ser calculado considerando los datos dados

Commit 20.05.12
 =

## version #1 del algoritmo Kruskal y DFS

* Partimos desde la teoria matematica de los grafos.Esto quiere decir que se consideran las estructuras vertice ( antes nodos), arista (antes conexion) y grafo.

* No esta comentado el codigo en el 99% de su extension.

* ejGraficador.py es un archivo que permite graficar un grafo, pero sin aprobechar las clases creadas en el proyecto.

* dristan.py es un algoritmo encontrado en internet que implementa el algoritmo de kruskal.

* El grafo que se importa, no tiene los costos de cada arista.
