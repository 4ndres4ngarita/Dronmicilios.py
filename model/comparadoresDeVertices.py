try:
    from base import *
except:
    from model.base import *

class ComparadorDeVertices:

    @staticmethod
    def sonVerticesIdenticos( unVertice:Vertice, otroVertice:Vertice):
        tienenElMismoCodigo = ComparadorDeVerticesPorCodigo.sonIguales(unVertice, otroVertice)
        tienenElMismoNombre = ComparadorDeVerticesPorNombre.sonIguales(unVertice,otroVertice)
        tienenLaMismaLista = ComparadorDeVerticesPorListaDeAristas.sonIguales( unVertice, otroVertice)
        sonIguales = tienenElMismoCodigo and tienenElMismoNombre and tienenLaMismaLista
        return sonIguales

#Comparadores de vertices por atributo
class ComparadorDeVerticesPorCodigo:
    @staticmethod
    def sonIguales( unVertice:Vertice, otroVertice:Vertice):
        return (
            ComparadorDeCodigoDeVertices.sonIguales( 
                unVertice.getCodigo(), otroVertice.getCodigo()
            )
        )

class ComparadorDeVerticesPorNombre:
    @staticmethod
    def sonIguales( unVertice:Vertice, otroVertice:Vertice):
        return (
            ComparadorDeNombreDeVertices.sonIguales(
                unVertice.getNombre(), otroVertice.getNombre()
            )
        )

class ComparadorDeVerticesPorListaDeAristas:
    @staticmethod
    def sonIguales( unVertice:Vertice, otroVertice:Vertice):
        return(
            ComparadorDeAristasDeVertices.sonIguales(
                unVertice.getListaDeAristas(),
                otroVertice.getListaDeAristas()
            )
        )

#Comparadores de atributos
class ComparadorDeCodigoDeVertices:
    @staticmethod
    def sonIguales( unCodigo:type(Vertice().getCodigo()), otroCodigo:type(Vertice().getCodigo())):
        return unCodigo == otroCodigo

class ComparadorDeNombreDeVertices:
    @staticmethod
    def sonIguales( unNombre:type(Vertice().getNombre()), otroNombre:type(Vertice().getNombre())):
        return unNombre == otroNombre

class ComparadorDeAristasDeVertices:

    @staticmethod
    def sonIguales( unaListaDeAristas:list, otraListaDeAristas:list):
        return unaListaDeAristas == otraListaDeAristas

class ComparadorDeNumeroDeAristas:

    @staticmethod
    def sonIguales( unNumero:int, otroNumero:int):
        return unNumero == otroNumero