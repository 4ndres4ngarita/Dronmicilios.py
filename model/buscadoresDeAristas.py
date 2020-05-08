try:
    from base import *
    from comparadoresDeIVertices import *  
except:
    from model.base import *
    from model.comparadoresDeIVertices import *

class IbuscadorDeAristas:

    def __init__(self, listaDeAristas:list):
        self.__listaDeAristas = listaDeAristas
        self.__aristasEncontradas = []

    def getAristas( self, condicion):
        pass
    
    def __añadirAristaEncontrada(self, aristaEncontrada:Arista):
        self.__aristasEncontradas.append( aristaEncontrada)
#buscadores con la lista directa de un vertice.
class BuscadorDeAristasPorIVertice(IbuscadorDeAristas):
    def __init__(self, listaDeAristas):
        super().__init__(listaDeAristas)
    
    def getAristas( self, verticeBuscado:IVertice):
        for aristaIesima in self._IbuscadorDeAristas__listaDeAristas:
            verticeDeUnaArista = aristaIesima.getIVerticeConectado()
            unaAristaTieneElIVerticeBuscado = (
                ComparadorDeIVertices.sonIVerticesIdenticos( verticeDeUnaArista, verticeBuscado)
            )
            if unaAristaTieneElIVerticeBuscado:
                self._IbuscadorDeAristas__añadirAristaEncontrada( aristaIesima)
            del unaAristaTieneElIVerticeBuscado
        return self._IbuscadorDeAristas__aristasEncontradas

class BuscadorDeAristasPorCodigoDelIVertice(IbuscadorDeAristas):
    def __init__(self, listaDeAristas):
        super().__init__(listaDeAristas)

    def getAristas(self, codigoDelIVerticeBuscado:str):
        for aristaIesima in self._IbuscadorDeAristas__listaDeAristas:
            verticeDeUnaArista = aristaIesima.getIVerticeConectado()
            unIVerticeTieneElCodigoBuscado =(
                ComparadorDeCodigoDeIVertices.sonIguales
                ( verticeDeUnaArista.getCodigo(), codigoDelIVerticeBuscado)
            )
            if unIVerticeTieneElCodigoBuscado: 
                self._IbuscadorDeAristas__añadirAristaEncontrada( aristaIesima)
            del unIVerticeTieneElCodigoBuscado
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

