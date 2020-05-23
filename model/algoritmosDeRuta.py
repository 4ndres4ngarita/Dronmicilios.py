import sys 

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def imprimirSolucion(self, distancias): 
        print("Tabla de Costos")

        nombresDeVertices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

        for node in range(self.V): 
            print(nombresDeVertices[node], "\t", distancias[node] )
  
    def minimaDistancia(self, distancias, sptSet): 

        minimoCosto = sys.maxsize
 
        for v in range(self.V): 
            if distancias[v] < minimoCosto and sptSet[v] == False: 
                minimoCosto = distancias[v] 
                minimoCosto_index = v 
  
        return minimoCosto_index

    def dijkstra(self, src): 
  
        distancias = [sys.maxsize] * self.V 
        distancias[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V):
            u = self.minimaDistancia(distancias, sptSet)
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and (
                distancias[v] > distancias[u] + self.graph[u][v]): 
                        distancias[v] = distancias[u] + self.graph[u][v] 
  
        self.imprimirSolucion(distancias)