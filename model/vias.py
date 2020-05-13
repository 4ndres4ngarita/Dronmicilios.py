from model.vertice import *
from model.arista import *
import math
DISTANCIA_ENTRE_ESQUINAS_EN_METROS = 100

class esquina(vertice):
    def __init__(self, codigo='', calle=0.0, carrera =0.0):
        super().__init__(codigo=codigo)
        self.direccion = {
            "calle": calle,
            "carrera": carrera
        }

class rutaAerea(arista):
    def __init__(self, esquinaA:esquina, esquinaB:esquina):
        super().__init__( esquinaA, esquinaB)
        self.__ponderarCosto()

    def __ponderarCosto(self):
        costoPonderadoEnMetros = math.sqrt(
            self.__calcularCatetoCarrera()**2 +
            self.__calcularCatetoCalle()**2
        )
        self.costo = costoPonderadoEnMetros
        return costoPonderadoEnMetros

    def __calcularCatetoCarrera(self):
        unidadesDeCarrera = (
            self.vertices["u"].direccion["carrera"] -
            self.vertices["v"].direccion["carrera"]
        )
        return self.__convertirUnidadesPorMetros( unidadesDeCarrera)

    def __calcularCatetoCalle(self):
        unidadesDeCalle = (
            self.vertices["u"].direccion["calle"] -
            self.vertices["v"].direccion["calle"]
        )
        return self.__convertirUnidadesPorMetros( unidadesDeCalle)

    def __convertirUnidadesPorMetros(self, distanciaEnUnidades):
        return abs( distanciaEnUnidades) * DISTANCIA_ENTRE_ESQUINAS_EN_METROS

class cliente(esquina):
    def __init__(self, codigo='', calle=0.0, carrera =0.0):
        super().__init__( codigo, calle, carrera)

class empresa(esquina):
    def __init__(self, codigo='', calle=0.0, carrera =0.0):
        super().__init__(codigo=codigo, calle=calle, carrera=carrera)