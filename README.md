# dronmicilios.py

Considere una  empresa de  domicilios,  que en  tiempos del  **COVID19**,  usa drones  para la  en-trega de pedidos. Los drones tienen un alcance de **2Km** a la redonda desde el punto de partida.Las cuadras son de **100mX100m** y el ancho de las vías es despreciable en este contexto. Parasimplificar la situaci ́on se considera que la sede central de la empresa y los clientes se encuentranen la intersecci ́on entre las carreras (horizontales) y las calles (verticales) en el mapa propuesto.El punto de partida de los drones se encuentra en el nodo **j**. El *archivoGrafo01.csv* ubica tantoa los clientes como a la empresa en la ciudad y el *archivoAdyacencia.csv* presenta la matriz deadyacencia en la situaci ́on descrita. Los desplazamientos entre cada par de nodos adyacentes sehace en l ́ınea recta. N ́otese que las distancias entre cada par de nodos adyacentes, el peso de laarista, debe ser calculado considerando los datos dados

Commit 20.05.08
 =

## separacion atributo 'estado' de clase 'vertice' para uso exclusivo de DFS

* Para mantener vivo los principios SOLID, especificamente Abierto/Cerrado. Por lo tanto se creará un diccionario de 'visitas' para reemplazar el atributo 'estado'.

* La creacion de '__getVerticeVecino()' en la clase DFS, se debe a que el IDE usado, o mejor el lenguaje no reconoce, de forma concreta, las clases a las que pertenecen algunos objetos encapsulados en listas.