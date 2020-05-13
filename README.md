# dronmicilios.py

Considere una  empresa de  domicilios,  que en  tiempos del  **COVID19**,  usa drones  para la  en-trega de pedidos. Los drones tienen un alcance de **2Km** a la redonda desde el punto de partida.Las cuadras son de **100mX100m** y el ancho de las vías es despreciable en este contexto. Parasimplificar la situaci ́on se considera que la sede central de la empresa y los clientes se encuentranen la intersecci ́on entre las carreras (horizontales) y las calles (verticales) en el mapa propuesto.El punto de partida de los drones se encuentra en el nodo **j**. El *archivoGrafo01.csv* ubica tantoa los clientes como a la empresa en la ciudad y el *archivoAdyacencia.csv* presenta la matriz deadyacencia en la situaci ́on descrita. Los desplazamientos entre cada par de nodos adyacentes sehace en l ́ınea recta. N ́otese que las distancias entre cada par de nodos adyacentes, el peso de laarista, debe ser calculado considerando los datos dados

Commit 20.05.12
 =

## Sin importacion de tipo CSV.

* No se hizo una importacion y abstracion de datos, sino que directamente en el archivo "grafoDeClientes.py", se tiene directamente los objetos, o el mapa del caso de estudio para el examen.

* No esta comentado el codigo en el 99.999% de su extension.

* Esta vez se esta usando o teniendo en cuenta los costos de cada arista para formar el arbol minimo de expansion partiendo de una interfaz (IAlgoritmoDeRuta) hasta una implementacion de la misma, en este caso y por el momento el algoritmo de Kruskal.

* Se hicieron arreglos, o tratar de optimizar la programacion de los algoritmos.

* Se esta usando toma de tiempo separada para cada algoritmo en el archivo principal ("dronmicilios.py")
