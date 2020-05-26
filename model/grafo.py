try:
    from model.vertice import *
    from model.arista import *
    from model.vias import *
except:
    #from vertice import *
    pass
SI_EXISTE_EL_VERTICE_EN_EL_GRAFO = True
NO_EXISTE_EL_VERTICE_EN_EL_GRAFO = False
SI_EXISTE_EL_ARISTA_EN_EL_GRAFO = True
NO_EXISTE_EL_ARISTA_EN_EL_GRAFO = False

class grafo:
    def __init__(self, verticesV:list, aristasE:list):
        self.verticesV = []
        if len(verticesV) > 0:
            self.añadirVertices( verticesV)
        self.aristasE = []
        if len(aristasE) > 0:
            self.añadirAristas( aristasE)
    
    def añadirVertices(self, vertices:list):
        for nuevoVerticeIesimo in vertices:
            self.añadirVertice( nuevoVerticeIesimo)

    def añadirVertice(self, verticeParaAgregar:cliente):
        noEstaEnLaLista = not self.existeVertice( verticeParaAgregar.codigo)
        if noEstaEnLaLista:
            verticeNuevo = verticeParaAgregar.getClon()
            self.verticesV.append(verticeNuevo)

    def existeVertice(self, codigoVertice:str):
        respuesta = NO_EXISTE_EL_VERTICE_EN_EL_GRAFO
        for verticeIesimo in self.verticesV:
            if verticeIesimo.codigo == codigoVertice:
                respuesta = SI_EXISTE_EL_VERTICE_EN_EL_GRAFO
        return respuesta
    
    def añadirAristas(self, aristas:list):
        for nuevaAristaIesima in aristas:
            self.añadirArista( nuevaAristaIesima)

    def getVertice(self, codigo:str):
        verticeRespuesta = vertice()
        for verticeIesimo in self.verticesV:
            if verticeIesimo.codigo == codigo:
                verticeRespuesta = verticeIesimo
                break
        return verticeRespuesta

    def añadirArista(self, aristaParaAgregar):
        codigoVerticeU = aristaParaAgregar.vertices["u"].codigo
        codigoVerticeV = aristaParaAgregar.vertices["v"].codigo
        del aristaParaAgregar.vertices["u"]
        del aristaParaAgregar.vertices["v"]
        existeVerticeU = self.existeVertice( codigoVerticeU)
        existeVerticeV = self.existeVertice( codigoVerticeV)
        existenVertices = existeVerticeU and existeVerticeV
        if existenVertices:
            aristaParaAgregar.vertices["u"] = self.getVertice(codigoVerticeU)
            aristaParaAgregar.vertices["u"].añadirVecino(
               codigoVerticeV
            )
            aristaParaAgregar.vertices["v"] = self.getVertice(codigoVerticeV)
            aristaParaAgregar.vertices["v"].añadirVecino(
                codigoVerticeU
            )
            
            self.aristasE.append(aristaParaAgregar)
        del codigoVerticeU
        del codigoVerticeV
            
    def existeArista(self, arista):
        respuesta = NO_EXISTE_EL_ARISTA_EN_EL_GRAFO
        for aristaIesimo in self.aristasE:
            if aristaIesimo == arista:
                respuesta = SI_EXISTE_EL_ARISTA_EN_EL_GRAFO
        return respuesta
    
    def buscarAristasConVertice(self, verticeBuscado):# -> list<arista>
        aristasEncontradas = []
        for aristaIesima in self.aristasE:
            if aristaIesima.estaElVertice(verticeBuscado):
                aristasEncontradas.append(aristaIesima)
        return aristasEncontradas

    """
        TODO: este metodo no debe limitarse a entregar una sola arista,
        deberia entregar todas las aristas que encuentre.
    """
    def buscarAristasConVertices(self, verticeU, verticeV):
        """
            WARNING: al asignar el vertice u a la variable verticeU, estoy
            cambiando lo que es verticeU dentro de este metodo? o estoy
            afectando tambien al que llamó esta función?
        """
        if (type(verticeU) is str) and (type(verticeV) is str):
            verticeU = self.getVertice( verticeU)
            verticeV = self.getVertice( verticeV)

        aristasEncontradas = []
        for aristaIesima in self.aristasE:
            estaElVerticeU:bool = aristaIesima.estaElVertice( verticeU)
            estaElVerticeV:bool = aristaIesima.estaElVertice( verticeV)
            if estaElVerticeU and estaElVerticeV:
                aristasEncontradas.append(aristaIesima)
                break
        return aristasEncontradas[0]

    def __str__(self):
        formato = "G = (V,E) \nV = ["
        iteracion = 1
        for verticeIesimo in self.verticesV:
            if iteracion == len(self.verticesV):
                formato += verticeIesimo.codigo + " ]\nE = \n[\n"
            else:
                formato += verticeIesimo.codigo + " , "
            iteracion += 1
        iteracion = 1
        for aristaIesima in self.aristasE:
            if iteracion == len(self.aristasE):
                formato += "\t(" + aristaIesima.vertices["u"].codigo +","+ aristaIesima.vertices["v"].codigo +")\n]"
            else:
                formato += "\t(" + aristaIesima.vertices["u"].codigo +","+ aristaIesima.vertices["v"].codigo +"), \n"
            iteracion += 1
        del iteracion
        return formato