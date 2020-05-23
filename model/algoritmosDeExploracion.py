from model.vertice import *
from model.arista import *
from model.grafo import *

NO_VISITADO=0
PARCIALMENTE_VISITADO=2
TOTALMENTE_VISITADO = 1

class IAlgoritmoDeExploracion:
    def ejecutarArlgoritmo(self, grafoBase:grafo, verticeRaiz:vertice):
        pass
    def estaTotalmenteConectado(self):
        pass
    def existeRutaEntre(self, verticeInicio:str, verticeDestino:str, grafoBase:grafo):
        pass
    def imprimirRecorrido(self):
        pass

class DepthFirstSearch(IAlgoritmoDeExploracion):
    def __init__(self):
        super().__init__()
        self.diccionarioDeVisitas = {}
        self.ordenDeVerticesVisitados = []

    def __alistarDiccionarioDeVisitas(self, grafoBase:grafo):
        diccionarioNuevo = {}
        for verticeIesimo in grafoBase.verticesV:
            diccionarioNuevo[verticeIesimo.codigo] = NO_VISITADO
        self.diccionarioDeVisitas = diccionarioNuevo
        self.ordenDeVerticesVisitados.clear()
    
    def ejecutarArlgoritmo(self, grafoBase:grafo, verticeRaiz:vertice):
        self.__alistarDiccionarioDeVisitas( grafoBase)
        self.__visitar( verticeRaiz, grafoBase)

    def __visitar(self, verticeRaiz:vertice, grafoBase:grafo):
        self.ordenDeVerticesVisitados.append(verticeRaiz.codigo)
        self.diccionarioDeVisitas[verticeRaiz.codigo] = PARCIALMENTE_VISITADO

        listaDeAristas = grafoBase.buscarAristasConVertice(verticeRaiz)
        for aristaIesima in listaDeAristas:
            verticeVecino = aristaIesima.getVerticeVecino( verticeRaiz)
            if self.diccionarioDeVisitas[verticeVecino.codigo] == NO_VISITADO:
                self.__visitar(verticeVecino, grafoBase)
        self.ordenDeVerticesVisitados.append(verticeRaiz.codigo)
        self.diccionarioDeVisitas[verticeRaiz.codigo] = TOTALMENTE_VISITADO

    def estaTotalmenteConectado(self):
        respuesta = True
        for unVerticeIesimo in self.diccionarioDeVisitas.values():
            if unVerticeIesimo is NO_VISITADO:
                respuesta = False
                break
        return respuesta

    def existeRutaEntre(self, verticeInicio:str, verticeDestino:str, grafoBase:grafo):
        self.__alistarDiccionarioDeVisitas( grafoBase)
        return self.__existeRutaCon(
            grafoBase.getVertice( verticeInicio),
            grafoBase.getVertice( verticeDestino),
            grafoBase)

    def __existeRutaCon(self, verticeInicio:vertice, verticeDestino:vertice, grafoBase:grafo):
        respuesta = False
        self.diccionarioDeVisitas[verticeInicio.codigo] = PARCIALMENTE_VISITADO
        for codigoVecinoIesimo in verticeInicio.vecinos:
            verticeVecino = grafoBase.getVertice(codigoVecinoIesimo)
            if verticeVecino == verticeDestino:
                respuesta = True
                break
            elif self.diccionarioDeVisitas[codigoVecinoIesimo] == NO_VISITADO:
                respuesta = self.__existeRutaCon( verticeVecino, verticeDestino, grafoBase)
            if respuesta:
                break
        return respuesta
    
    def imprimirRecorrido(self):
        totalDatos = len(self.ordenDeVerticesVisitados)/2
        i = 0
        for verticeI in self.ordenDeVerticesVisitados:
            if i < totalDatos:
                print("vertice :" + verticeI + " parcialmente visitado.")
                i+=1
            else:
                print("vertice :" + verticeI + " Totalmente visitado.")

class BreadthFirstSearch(IAlgoritmoDeExploracion):
    def __init__(self):
        super().__init__()
        self.diccionarioDeVisitas = {}
        self.ordenDeVerticesVisitados = []

    def __alistarDiccionarioDeVisitas(self, grafoBase:grafo):
        diccionarioNuevo = {}
        for verticeIesimo in grafoBase.verticesV:
            diccionarioNuevo[verticeIesimo.codigo] = NO_VISITADO
        self.diccionarioDeVisitas = diccionarioNuevo
        self.ordenDeVerticesVisitados.clear()
    
    def ejecutarArlgoritmo(self, grafoBase:grafo, verticeRaiz:vertice):
        self.__alistarDiccionarioDeVisitas( grafoBase)
        verticesParaVisitar = [ verticeRaiz]
        self.diccionarioDeVisitas[verticeRaiz.codigo] = TOTALMENTE_VISITADO 

        while verticesParaVisitar != [] :
            verticeVisitado:vertice = verticesParaVisitar.pop(0)
            self.ordenDeVerticesVisitados.append(verticeVisitado)

            aristasConVecinos = grafoBase.buscarAristasConVertice(verticeVisitado)
            for aristaIesima in aristasConVecinos:
                verticeVecino = aristaIesima.getVerticeVecino( verticeVisitado)
                if self.diccionarioDeVisitas[verticeVecino.codigo] == NO_VISITADO:
                    self.diccionarioDeVisitas[verticeVecino.codigo] = TOTALMENTE_VISITADO
                    verticesParaVisitar.append( verticeVecino)
                elif verticesParaVisitar == []:
                        break

    def estaTotalmenteConectado(self):
        respuesta = True
        for unVerticeIesimo in self.diccionarioDeVisitas.values():
            if unVerticeIesimo is NO_VISITADO:
                respuesta = False
                break
        return respuesta

    def existeRutaEntre(self, verticeInicio:str, verticeDestino:str, grafoBase:grafo):
        self.__alistarDiccionarioDeVisitas( grafoBase)
        return self.__existeRutaCon(
            grafoBase.getVertice( verticeInicio),
            grafoBase.getVertice( verticeDestino),
            grafoBase)

    def __existeRutaCon(self, verticeInicio:vertice, verticeDestino:vertice, grafoBase:grafo):
        respuesta = False

        verticesParaVisitar = [ verticeInicio]
        self.diccionarioDeVisitas[verticeInicio.codigo] = TOTALMENTE_VISITADO 

        while verticesParaVisitar != [] and respuesta != True:
            verticeVisitado:vertice = verticesParaVisitar.pop(0)
            self.ordenDeVerticesVisitados.append(verticeVisitado)
            
            aristasConVecinos = grafoBase.buscarAristasConVertice(verticeVisitado)
            for aristaIesima in aristasConVecinos:
                verticeVecino = aristaIesima.getVerticeVecino( verticeVisitado)
                if verticeVecino == verticeDestino:
                    respuesta = True
                    break
                elif self.diccionarioDeVisitas[verticeVecino.codigo] == NO_VISITADO:
                    self.diccionarioDeVisitas[verticeVisitado.codigo] = TOTALMENTE_VISITADO
                    verticesParaVisitar.append( verticeVecino)
        return respuesta
    
    def imprimirRecorrido(self):
        for verticeI in self.ordenDeVerticesVisitados:
            print("vertice " + str(verticeI) + " visitado.")