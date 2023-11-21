from Condensador import Condensador

configuraciones = {
    #  Inline
    #  Arriba, abajo 
    1  : (0, 0),
    2  : (1, 1),
    3  : (2, 2),
    4  : (3, 3),
    5  : (4, 4),
    6  : None,
    #  Stagered
    #  Nones, pares
    7  : [(0, 0), (0, 0)],
    8  : [(1, 0), (0, 1)],
    9  : [(1, 1), (1, 1)],
    10 : [(2, 1), (1, 2)],
    11 : [(2, 2), (2, 2)],
    12 : [(3, 2), (2, 3)],
    13 : None,
    #     Nones, pares
    14 : [(0, 0), (0, 0)],
    15 : [(1, 0), (0, 1)],
    16 : [(1, 1), (1, 1)],
    17 : [(1, 2), (2, 1)],
    18 : [(2, 2), (2, 2)],
    19 : [(2, 3), (3, 2)],
    20 : None,
    #     Nones, pares
    21 : [(0, 0), (0, 0)],
    22 : [(0, 0), (1, 1)],
    23 : [(1, 1), (1, 1)],
    24 : [(1, 1), (2, 2)],
    25 : [(2, 2), (2, 2)],
    26 : [(2, 2), (3, 3)],
    27 : None,
    #     Nones, pares
    28 : [(0, 0), (0, 0)],
    29 : [(1, 1), (0, 0)],
    30 : [(1, 1), (1, 1)],
    31 : [(2, 2), (1, 1)],
    32 : [(2, 2), (2, 2)],
    33 : [(3, 3), (2, 2)],
    34 : None
}
def crearCondensador(Tipo, config, Ntub, posTub=None):
    if config == 6:
        print(("""Hay más de 4 tubos arriba y más de 4 abajo 
                        en la zona de baja velociadad, 
                        ¿Es esto correcto?, Si es así, es un caso no 
                        considerado en el script"""))
        return None
    
    if config == 13:
        print(("""Hay más de 5 tubos arriba y más de 5 abajo 
                                en la zona de baja velociadad, 
                                ¿Es esto correcto?, Si es así, es un caso no 
                                considerado en el script"""))
        return None
    
    if config == 20:
        print(("""Hay más de 5 tubos arriba y más de 5 abajo 
                                en la zona de baja velociadad, 
                                ¿Es esto correcto?, Si es así, es un caso no 
                                considerado en el script"""))
        return None
    
    if config == 27:
        print(("""Hay más de 5 tubos arriba y más de 5 abajo 
                                en la zona de baja velociadad, 
                                ¿Es esto correcto?, Si es así, es un caso no 
                                considerado en el script"""))
        return None
    
    if config == 34:
        print(("""Hay más de 5 tubos arriba y más de 5 abajo 
                                en la zona de baja velociadad, 
                                ¿Es esto correcto?, Si es así, es un caso no 
                                considerado en el script"""))
        return None
    
    tubos_en_baja = configuraciones[config]
    
    return Condensador(Tipo, Ntub, posTub, tubos_en_baja)
    