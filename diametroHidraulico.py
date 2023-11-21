import math
from math import pi

def FEL_f(P_d, DP_f):
    """Cálculo de factor de extensión de longitud 
    para el caso de aletado corrugado"""
    return math.sqrt(P_d**2 + DP_f**2)/DP_f

def get_d_c(d_o, t_f):
    """Cálculo de diámetro collar
    retorna en mm"""
    return d_o + (2*t_f)

def Dh_HE_plane(S_t, S_l, S_f, d_c, t_f, FEL_f=1):
    """Cálculo del diámetro hidráulico
    del intercambiador para aletado plano o wavy"""
    return 4 * (
        ( (S_t*S_l*S_f) 
         - 0.25*( (pi * d_c**2 * (S_f-t_f)) + 4 * (S_t*FEL_f*S_l*t_f)) )
         / ( (0.5*((4*S_t*FEL_f*S_l)- pi * d_c**2)) + (pi * d_c**2 * (S_f-t_f)) )
    )

