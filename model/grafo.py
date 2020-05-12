try:
    from vertice import *
    from arista import *
except:
    from model.vertice import *
    from model.arista import *
    
class grafo:

    __SI_EXISTE_EL_VERTICE_EN_EL_GRAFO = True
    __NO_EXISTE_EL_VERTICE_EN_EL_GRAFO = False
    __SI_EXISTE_EL_ARISTA_EN_EL_GRAFO = True
    __NO_EXISTE_EL_ARISTA_EN_EL_GRAFO = False

    def __init__(self, verticesV = [], aristasE = []):
        self.verticesV = verticesV
        self.aristasE = aristasE
    
    def añadirVertices(self, vertices:list):
        for nuevoVerticeIesimo in vertices:
            self.añadirVertice( nuevoVerticeIesimo)

    def añadirVertice(self, vertice:vertice):
        noEstaEnLaLista = not self.existeVertice( vertice)
        if noEstaEnLaLista:
            self.verticesV.append(vertice)

    def existeVertice(self, vertice:vertice):
        respuesta = __NO_EXISTE_EL_VERTICE_EN_EL_GRAFO
        for verticeIesimo in self.verticesV:
            if verticeIesimo == vertice:
                respuesta = __SI_EXISTE_EL_VERTICE_EN_EL_GRAFO
        return respuesta
    
    def añadirAristas(self, aristas:list):
        for nuevaAristaIesima in aristas:
            self.añadirArista( nuevaAristaIesima)

    def buscarVertice(self, codigo:str):
        verticeRespuesta = vertice()
        for verticeIesimo in self.verticesV:
            if verticeIesimo.codigo == codigo:
                verticeRespuesta = verticeIesimo
                break
        return verticeRespuesta

    def añadirArista(self, arista:arista):
        noEstaEnLaLista = not self.existeArista( arista)
        if noEstaEnLaLista:
            self.aristasE.append(arista)

    def existeArista(self, arista:arista):
        respuesta = __NO_EXISTE_EL_ARISTA_EN_EL_GRAFO
        for aristaIesimo in self.aristasE:
            if aristaIesimo == arista:
                respuesta = __SI_EXISTE_EL_ARISTA_EN_EL_GRAFO
        return respuesta
    
    def buscarAristasConVertice(self, verticeBuscado:vertice):
        aristasEncontradas = []
        for aristaIesima in self.aristasE:
            if aristaIesima.estaElVertice(verticeBuscado):
                aristasEncontradas.append(aristaIesima)
        return aristasEncontradas
    
    def __str__(self):
        formato = "G = (V,E) \nV = ["
        iteracion = 1
        for verticeIesimo in self.verticesV:
            if iteracion == len(self.verticesV):
                formato += verticeIesimo.codigo + " ]\nE = ["
            else:
                formato += verticeIesimo.codigo + " , "
            iteracion += 1
        iteracion = 1
        for aristaIesima in self.aristasE:
            if iteracion == len(self.aristasE):
                formato += "(" + aristaIesima.vertices["u"].codigo +","+ aristaIesima.vertices["v"].codigo +")]\n"
            else:
                formato += "(" + aristaIesima.vertices["u"].codigo +","+ aristaIesima.vertices["v"].codigo +") , "
            iteracion += 1
        del iteracion
        return formato

        

