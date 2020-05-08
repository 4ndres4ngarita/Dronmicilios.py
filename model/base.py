class IVertice:
    __codigo:str
    __nombre: str
    __listaDeAristas: list

    estado:int

    def __init__(self, codigoInicial = "", nombreInicial = ""):
        self.__codigo = codigoInicial
        self.__nombre = nombreInicial
        self.__listaDeAristas = []

    """
        definimos getCodigo ( de un vertice) para:
         retornar el codigo de un vertice.
    """

    def getCodigo( self):
        return self.__codigo

    def getNombre( self):
        return self.__nombre

    def getListaDeAristas( self):
        return self.__listaDeAristas
    """
        definimos setCodigo ( de un vertice, un nuevo codigo) para:
         asignale un nuevo codigo al codigo de un vertice.
    """

    def setCodigo(  self, nuevoCodigo:str):
        self.__codigo = nuevoCodigo

    def setNombre( self, nuevoNombre:str):
        self.__nombre = nuevoNombre
    
    def setListaDeAristas( self, nuevaListaDeAristas:list):
        self.__listaDeAristas = nuevaListaDeAristas
    
    def añadirArista(self, nuevaArista):
        self.__listaDeAristas.append( nuevaArista)

class IArista:
    __verticeConectado: IVertice
    __costo: float
    __numeroDeArista:int

    def __init__(self):
        self.__verticeConectado = IVertice()
        self.__costo = 0.0
        self.__numeroDeArista = 0

    def getVerticeConectado( self):
        return self.__verticeConectado

    def getCosto( self):
        return self.__costo
    
    def getNumeroDeArista( self):
        return self.__numeroDeArista
    
    def setVerticeConectado( self, nuevoVerticeConectado:IVertice):
        self.__verticeConectado = nuevoVerticeConectado
    
    def setCostos( self, nuevaCostos:float):
        self.__costo = nuevaCostos
    
    def setNumeroDeArista( self, nuevoNumeroDeArista:int):
        self.__numeroDeArista = nuevoNumeroDeArista

class IGrafo:
    __vertices:dict

    def __init__(self):
        self.__vertices={}
    
    def getVertices(self):
        return self.__vertices

    def getVertice(self, palabraClave:int):
        return self.__vertices[palabraClave]

    def setVertices(self, nuevosVertices:dict):
        self.__vertices = nuevosVertices
    
    def añadirVertice(self, nuevoVertice:IVertice):
        palabraClave = nuevoVertice.getCodigo
        self.__vertices[palabraClave] = nuevoVertice
    
    def quitarVertice(self, palabraClave:int=0):
        self.__vertices.pop(palabraClave)
    
    def contarVertices(self):
        return len(self.__vertices)