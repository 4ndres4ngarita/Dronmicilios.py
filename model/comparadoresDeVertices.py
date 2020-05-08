try:
    from base import *
except:
    from model.base import *

class ComparadorDeIVertices:

    @staticmethod
    def sonIVerticesIdenticos( unIVertice:IVertice, otroIVertice:IVertice):
        tienenElMismoCodigo = ComparadorDeIVerticesPorCodigo.sonIguales(unIVertice, otroIVertice)
        tienenElMismoNombre = ComparadorDeIVerticesPorNombre.sonIguales(unIVertice,otroIVertice)
        tienenLaMismaLista = ComparadorDeIVerticesPorListaDeAristas.sonIguales( unIVertice, otroIVertice)
        sonIguales = tienenElMismoCodigo and tienenElMismoNombre and tienenLaMismaLista
        return sonIguales

#Comparadores de vertices por atributo
class ComparadorDeIVerticesPorCodigo:
    @staticmethod
    def sonIguales( unIVertice:IVertice, otroIVertice:IVertice):
        return (
            ComparadorDeCodigoDeIVertices.sonIguales( 
                unIVertice.getCodigo(), otroIVertice.getCodigo()
            )
        )

class ComparadorDeIVerticesPorNombre:
    @staticmethod
    def sonIguales( unIVertice:IVertice, otroIVertice:IVertice):
        return (
            ComparadorDeNombreDeIVertices.sonIguales(
                unIVertice.getNombre(), otroIVertice.getNombre()
            )
        )

class ComparadorDeIVerticesPorListaDeAristas:
    @staticmethod
    def sonIguales( unIVertice:IVertice, otroIVertice:IVertice):
        return(
            ComparadorDeAristasDeIVertices.sonIguales(
                unIVertice.getListaDeAristas(),
                otroIVertice.getListaDeAristas()
            )
        )

#Comparadores de atributos
class ComparadorDeCodigoDeIVertices:
    @staticmethod
    def sonIguales( unCodigo:type(IVertice().getCodigo()), otroCodigo:type(IVertice().getCodigo())):
        return unCodigo == otroCodigo

class ComparadorDeNombreDeIVertices:
    @staticmethod
    def sonIguales( unNombre:type(IVertice().getNombre()), otroNombre:type(IVertice().getNombre())):
        return unNombre == otroNombre

class ComparadorDeAristasDeIVertices:

    @staticmethod
    def sonIguales( unaListaDeAristas:list, otraListaDeAristas:list):
        return unaListaDeAristas == otraListaDeAristas

class ComparadorDeNumeroDeAristas:

    @staticmethod
    def sonIguales( unNumero:int, otroNumero:int):
        return unNumero == otroNumero