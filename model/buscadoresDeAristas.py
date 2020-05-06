try:
    from base import *
    from comparadoresDeVertices import *  
except:
    from model.base import *
    from model.comparadoresDeVertices import *

class IbuscadorDeAristas:

    def __init__(self, listaDeAristas:list):
        self.__listaDeAristas = listaDeAristas
        self.__aristasEncontradas = []

    def getAristas( self, condicion):
        pass
    
    def __añadirAristaEncontrada(self, aristaEncontrada:Arista):
        self.__aristasEncontradas.append( aristaEncontrada)
#buscadores con la lista directa de un vertice.
class BuscadorDeAristasPorVertice(IbuscadorDeAristas):
    def __init__(self, listaDeAristas):
        super().__init__(listaDeAristas)
    
    def getAristas( self, verticeBuscado:Vertice):
        for aristaIesima in self._IbuscadorDeAristas__listaDeAristas:
            verticeDeUnaArista = aristaIesima.getVerticeConectado()
            unaAristaTieneElVerticeBuscado = (
                ComparadorDeVertices.sonVerticesIdenticos( verticeDeUnaArista, verticeBuscado)
            )
            if unaAristaTieneElVerticeBuscado:
                self._IbuscadorDeAristas__añadirAristaEncontrada( aristaIesima)
            del unaAristaTieneElVerticeBuscado
        return self._IbuscadorDeAristas__aristasEncontradas

class BuscadorDeAristasPorCodigoDelVertice(IbuscadorDeAristas):
    def __init__(self, listaDeAristas):
        super().__init__(listaDeAristas)

    def getAristas(self, codigoDelVerticeBuscado:str):
        for aristaIesima in self._IbuscadorDeAristas__listaDeAristas:
            verticeDeUnaArista = aristaIesima.getVerticeConectado()
            unVerticeTieneElCodigoBuscado =(
                ComparadorDeCodigoDeVertices.sonIguales
                ( verticeDeUnaArista.getCodigo(), codigoDelVerticeBuscado)
            )
            if unVerticeTieneElCodigoBuscado: 
                self._IbuscadorDeAristas__añadirAristaEncontrada( aristaIesima)
            del unVerticeTieneElCodigoBuscado
        return self._IbuscadorDeAristas__aristasEncontradas

#buscadores con listas procesadas.
class BuscadorDeAristasPorNumeroDeArista(IbuscadorDeAristas):
    
    def __init__(self, listaDeAristas):
        super().__init__(listaDeAristas)
    
    def getAristas(self, numeroDeAristaBuscado:int):
        for aristaIesima in self._IbuscadorDeAristas__listaDeAristas:
            numeroDeUnaArista = aristaIesima.getNumeroDeArista()
            unaAristaTieneElNumeroBuscado = (
                ComparadorDeNumeroDeAristas.sonIguales(
                    numeroDeUnaArista, numeroDeAristaBuscado
                )
            )
            if unaAristaTieneElNumeroBuscado:
                self._IbuscadorDeAristas__añadirAristaEncontrada( aristaIesima)
        return self._IbuscadorDeAristas__aristasEncontradas

