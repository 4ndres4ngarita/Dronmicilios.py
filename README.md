# dronmicilios.py

Considere una  empresa de  domicilios,  que en  tiempos del  **COVID19**,  usa drones  para la  en-trega de pedidos. Los drones tienen un alcance de **2Km** a la redonda desde el punto de partida.Las cuadras son de **100mX100m** y el ancho de las vías es despreciable en este contexto. Parasimplificar la situaci ́on se considera que la sede central de la empresa y los clientes se encuentranen la intersecci ́on entre las carreras (horizontales) y las calles (verticales) en el mapa propuesto.El punto de partida de los drones se encuentra en el nodo **j**. El *archivoGrafo01.csv* ubica tantoa los clientes como a la empresa en la ciudad y el *archivoAdyacencia.csv* presenta la matriz deadyacencia en la situaci ́on descrita. Los desplazamientos entre cada par de nodos adyacentes sehace en l ́ınea recta. N ́otese que las distancias entre cada par de nodos adyacentes, el peso de laarista, debe ser calculado considerando los datos dados

Commit 20.05.17
 =

## Entrega del parcial.

* fue necesario inyectar los atributos
* En este punto, es inutil el codigo que almacenaba la carpeta 'test'.
* Fue necesario cortar y pegar el atributo 'direcciones' desde la clase esquina hasta vertice, debido a que la clase grafo,en el metodo grafo.'añadirVertice()' utiliza el metodo vertice.'copiarAtributos()', entonces en el caso de trabajar con clases que heredan de vertice, dentro del grafo se agregaran como vertices, mas no guardaran los atributos extras que, en este caso poseia la clase esquina ( en este caso).
* graficador.py posee una funcial enfocada en graficar un objeto 'grafo'.

