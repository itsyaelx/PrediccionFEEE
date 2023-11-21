from diametroHidraulico import get_d_c

# """

# """
# "Arriba, abajo"


# S_t  = input("Ingrese paso transversal de los tubos en mm")
# S_f  = input("Ingrese paso de aleta en mm")
# t_f  = input("Espesor de la aleta en mm")
# d_o  = input("Diametro exterior del tubo en mm")
# S_l  = input("Paso longitudinal de los tubos en mm")
# TipoAletado = input("El aletado es plano (P) o corrugado (W)")

# #Diametro collar
# d_c = get_d_c(d_o, t_f) 


# if TipoAletado == "W":
#     P_d = input("Profundidad del patrón de corrugado en mm")
#     DP_f = input("Distancia proyectada del patrón de corrugado en mm")

# #Longitud de zona aletada
# Wt = input("Ancho de la entrada de aire en m")

# Ht = input("Altura de la entrada de aire en m")
# Wav = input("Ancho de la zona de alta velocidad en m")
# Hav = input("Altura de la zona de alta velocidad en m")

# # Se quita Ltub porque esta dimensión puede estar fuera de la 
# # zona en la que sí fluye el aire. 
# #Ltub = input("Longitud de los tubos en m") 

# Vbaja = input("Velocidad en la zona de baja velocidad en m/s")
# Valta = input("Velocidad en la zona de alta velocidad en m/s")
# Tipo = input("Es escalonado(S) o Lineal (I)")
# N_ele_tub = input("Número de elementos por tubo: ")

def getConfig(Tipo, S_t, Hav, d_c, Ntub, posTub=None):
    S_t = float(S_t)
    Hav = float(Hav)
    d_c = float(d_c)
    Ntub = int(Ntub)

    if Tipo == "I":

        #Altura que ocupan los tubos [mm]
        Htub = (Ntub*float(S_t)) - S_t 

        # Diferencia de alturas de tubos y la zona de alta velocidad [mm]
        Dif_alt_tub_Hav = Htub-(Hav * 1000) 

        if Dif_alt_tub_Hav < d_c:
            # En este caso todos los tubos están en la zona 
            # alta velocidad caso 1
            return 1
        else:
            Rel_1 = (Dif_alt_tub_Hav/2)/S_t

            if Rel_1 <= 1.1:
                #Caso en el que un tubo arriba y otro abajo en la
                #zona de baja velocidad
                return 2
            
            elif Rel_1 > 1.1 and Rel_1 <= 2.1:
                #Caso en el que hay dos tubos arriba y dos abajo
                #en la zona de baja velocidad
                return 3

            elif Rel_1 > 2.1 and Rel_1 <= 3.1:
                #Caso en el que hay tres tubos arriba y tres abajo
                #en la zona de baja velocidad
                return 4
            
            elif Rel_1 > 3.1 and Rel_1 <= 4.1:
                #Caso en el que hay cuatro tubos arriba y cuatro abajo
                #en la zona de baja velocidad
                return 5
            
            elif Rel_1 > 4.1:
                #Caso en el que hay más de cuatro tubos arriba y abajo
                #en la zona de baja velocidad
                return 6

    elif Tipo == "S":

        Ntub_non, Ntub_par = Ntub

        if Ntub_non == Ntub_par:

            Htub = (Ntub_par*S_t) - 0.5*S_t

            if posTub == 1:
                Dif_alt_tub_Hav = Htub - (Hav*1000)
                if Dif_alt_tub_Hav < d_c:
                    #Todos los tubos están dentro de la zona de alta velocidad
                    return 7
                else:
                    Rel_1 = (Dif_alt_tub_Hav/2)/(0.5*S_t)
                    
                    if Rel_1 <= 1.1:
                        # Caso en el que un tubo arriba de las filas nones 
                        # y otro abajo en las filas pares en la zona de 
                        # baja velocidad
                        return 8
                    
                    elif Rel_1 > 1.1 and Rel_1 <= 2.1:
                        # Caso en el que dos tubo de las filas nones (1 arriba y
                        # otro abajo) y dos tubos en las filas pares (1 arriba y 
                        # otro abajo) en la zona de baja velocidad
                        return 9
                    
                    elif Rel_1 > 2.1 and Rel_1 <= 3.1:
                        # Caso en el que tres tubo de las filas nones (2 arriba y
                        # otro abajo) y tres tubos en las filas pares (1 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 10
                    
                    elif Rel_1 > 3.1 and Rel_1 <= 4.1:
                        # Caso en el que cuatro tubo de las filas nones (2 arriba y
                        # 2 abajo) y cuatro tubos en las filas pares (2 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 11

                    elif Rel_1 > 4.1 and Rel_1 <= 5.1:
                        # Caso en el que cinco tubo de las filas nones (3 arriba y
                        # 2 abajo) y cinco tubos en las filas pares (2 arriba y 
                        # 3 abajo) en la zona de baja velocidad
                        return 12

                    elif Rel_1 > 5.1:

                        #Caso en el que hay más de cinco tubos arriba y abajo
                        #en la zona de baja velocidad
                        return 13

            elif posTub == 2:

                Dif_alt_tub_Hav = Htub - (Hav*1000)

                if Dif_alt_tub_Hav < d_c:
                    #Todos los tubos están dentro de la zona de alta velocidad
                    return 14
                else:
                    Rel_1 = (Dif_alt_tub_Hav/2)/(0.5*S_t)

                    if Rel_1 <= 1.1:
                        #Caso en el que un tubo arriba de las filas nones 
                        # y otro abajo en las filas pares en la zona de 
                        # baja velocidad
                        return 15

                    elif Rel_1 > 1.1 and Rel_1 <= 2.1:
                        # Caso en el que dos tubo de las filas nones (1 arriba y
                        # otro abajo) y dos tubos en las filas pares (1 arriba y 
                        # otro abajo) en la zona de baja velocidad
                        return 16

                    elif Rel_1 > 2.1 and Rel_1 <= 3.1:
                        # Caso en el que tres tubo de las filas nones (1 arriba y
                        # 2 abajo) y tres tubos en las filas pares (2 arriba y 
                        # 1 abajo) en la zona de baja velocidad
                        return 17

                    elif Rel_1 > 3.1 and Rel_1 <= 4.1:
                        # Caso en el que cuatro tubo de las filas nones (2 arriba y
                        # 2 abajo) y cuatro tubos en las filas pares (2 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 18

                    elif Rel_1 > 4.1 and Rel_1 <= 5.1:
                        # Caso en el que cinco tubo de las filas nones (2 arriba y
                        # 3 abajo) y cinco tubos en las filas pares (3 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 19

                    elif Rel_1 > 5.1:

                        #Caso en el que hay más de cinco tubos arriba y abajo
                        #en la zona de baja velocidad
                        return 20
        
        elif Ntub_par != Ntub_non:
            if posTub == 2:

                Htub = (Ntub_par*S_t) - S_t

                Dif_alt_tub_Hav = Htub - (Hav*1000)

                if Dif_alt_tub_Hav < d_c:
                    #Todos los tubos están dentro de la zona de alta velocidad
                    return 21
                else:
                    Rel_1 = (Dif_alt_tub_Hav/2)/(0.5*S_t)

                    if Rel_1 <= 1.1:
                        # Caso en el que dos tubos de las filas pares (1 arriba y 
                        # otro abajo ) en la zona de baja velocidad

                        return 22

                    elif Rel_1 > 1.1 and Rel_1 <= 2.1:
                        # Caso en el que dos tubo de las filas nones (1 arriba y
                        # otro abajo) y dos tubos en las filas pares (1 arriba y 
                        # otro abajo) en la zona de baja velocidad
                        return 23

                    elif Rel_1 > 2.1 and Rel_1 <= 3.1:
                        # Caso en el que dos tubo de las filas nones (1 arriba y
                        # 1 abajo) y cuatro tubos en las filas pares (2 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 24

                    elif Rel_1 > 3.1 and Rel_1 <= 4.1:
                        # Caso en el que cuatro tubo de las filas nones (2 arriba y
                        # 2 abajo) y cuatro tubos en las filas pares (2 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 25

                    elif Rel_1 > 4.1 and Rel_1 <= 5.1:
                        # Caso en el que cuatro tubo de las filas nones (2 arriba y
                        # 2 abajo) y seis tubos en las filas pares (3 arriba y 
                        # 3 abajo) en la zona de baja velocidad
                        return 26

                    elif Rel_1 > 5.1:

                        #Caso en el que hay más de cinco tubos arriba y abajo
                        #en la zona de baja velocidad
                        return 27

            elif posTub ==  1:

                Htub = (Ntub_non*S_t) - S_t
                Dif_alt_tub_Hav = Htub - (Hav*1000)

                if Dif_alt_tub_Hav < d_c:
                    #Todos los tubos están dentro de la zona de alta velocidad
                    return 28
                else:
                    Rel_1 = (Dif_alt_tub_Hav/2)/(0.5*S_t)

                    if Rel_1 <= 1.1:
                        # Caso en el que dos tubos de las filas nones (1 arriba y 
                        # otro abajo ) en la zona de baja velocidad
                        return 29

                    elif Rel_1 > 1.1 and Rel_1 <= 2.1:
                        # Caso en el que dos tubo de las filas nones (1 arriba y
                        # otro abajo) y dos tubos en las filas pares (1 arriba y 
                        # otro abajo) en la zona de baja velocidad
                        return 30

                    elif Rel_1 > 2.1 and Rel_1 <= 3.1:
                        # Caso en el que cuatro tubo de las filas nones (2 arriba y
                        # 2 abajo) y dos tubos en las filas pares (1 arriba y 
                        # 1 abajo) en la zona de baja velocidad
                        return 31

                    elif Rel_1 > 3.1 and Rel_1 <= 4.1:
                        # Caso en el que cuatro tubo de las filas nones (2 arriba y
                        # 2 abajo) y cuatro tubos en las filas pares (2 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 32

                    elif Rel_1 > 4.1 and Rel_1 <= 5.1:
                        # Caso en el que seis tubo de las filas nones (3 arriba y
                        # 3 abajo) y cuatro tubos en las filas pares (2 arriba y 
                        # 2 abajo) en la zona de baja velocidad
                        return 33

                    elif Rel_1 > 5.1:

                        #Caso en el que hay más de cinco tubos arriba y abajo
                        #en la zona de baja velocidad
                        return 34

# # Ancho de la zona de baja velocidad [m]
# Wbv = (Wt - Wav) / 2

# # Longitud de cada elemento en el tubo [m]
# Lon_ele = Wt/N_ele_tub

# # Cantidad de elementos en el inicio y al final del tubo 
# # que deberán llevar baja velocidad.
# Ele_bv = int(Wbv/Lon_ele) 



