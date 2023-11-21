from Segmento import Segmento

class Tubo:
    segmentos = {}
    def __init__(self, Nsegmentos, baja_velocidad, alta_velocidad, segmentos_baja) -> None:
        self.Nsegmentos = Nsegmentos
        self.baja_Velocidad = baja_velocidad
        self.alta_Velocidad = alta_velocidad
        self.segmentos_baja = segmentos_baja
        for i in range(Nsegmentos):
            if i >= Nsegmentos - segmentos_baja or i < segmentos_baja:
                # self.segmentos[i + 1] = Segmento("baja_velocidad")
                self.segmentos[i + 1] = "baja_velocidad"
                continue
            # self.segmentos[i + 1] = Segmento("alta_velocidad")
            self.segmentos[i + 1] = "alta_velocidad"
