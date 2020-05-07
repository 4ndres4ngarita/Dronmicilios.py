# dronmicilios.py

Considere una  empresa de  domicilios,  que en  tiempos del  **COVID19**,  usa drones  para la  en-trega de pedidos. Los drones tienen un alcance de **2Km** a la redonda desde el punto de partida.Las cuadras son de **100mX100m** y el ancho de las vías es despreciable en este contexto. Parasimplificar la situaci ́on se considera que la sede central de la empresa y los clientes se encuentranen la intersecci ́on entre las carreras (horizontales) y las calles (verticales) en el mapa propuesto.El punto de partida de los drones se encuentra en el nodo **j**. El *archivoGrafo01.csv* ubica tantoa los clientes como a la empresa en la ciudad y el *archivoAdyacencia.csv* presenta la matriz deadyacencia en la situaci ́on descrita. Los desplazamientos entre cada par de nodos adyacentes sehace en l ́ınea recta. N ́otese que las distancias entre cada par de nodos adyacentes, el peso de laarista, debe ser calculado considerando los datos dados

Commit 20.05.06
 =

## modulos núcleo, abstracción desde .csv e implementacion Depth-First Search 

* En el archivo principal, se creó metodos que procesan el archvo Adyacencia.csv, en donde se ubica, en cristiano, una representación de la matriz de relaciones o aristas entre los nodos.

* Creé un banner lo mas de bacáno, me demoré **1h** y **30min**

* El modulo model.base tiene las clases bases, vertice, arista y grafo, Sin embargo hay una cuestion:

        Debido a que el proyecto (examen), requiere una implementacion para arbol de expansion, reconocimiento automatico, fue necesario añadir un atributo extra a clase vertice ('estado'); la mejor opcion, en realidad considero es hacer clases que hereden de la base, para tener una uniformidad en las capas de abstraccion y procurando ejercer los principios **SOLID**.

* A lo mejor son caprichos mios, no lo se, el tiempo y el estrés lo dirán.