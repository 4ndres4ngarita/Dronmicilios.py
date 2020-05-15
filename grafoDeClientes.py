from model.vias import *
from model.grafo import *

CLIENTE_A = cliente('A',2,1)
CLIENTE_B = cliente('B',19,1)
CLIENTE_C = cliente('C',5,2)
CLIENTE_D = cliente('D',11,3)
CLIENTE_E = cliente('E',18,5)
CLIENTE_F = cliente('F',4,6)
CLIENTE_G = cliente('G',12,7)
CLIENTE_H = cliente('H',20,8)
CLIENTE_I = cliente('I',16,10)
EMPRESA_J = empresa('J',10,10)
CLIENTE_K = cliente('K',7,11)
CLIENTE_L = cliente('L',5,13)
CLIENTE_M = cliente('M',11,13)
CLIENTE_N = cliente('N',19,14)
CLIENTE_O = cliente('O',16,16)
CLIENTE_P = cliente('P',4,17)
CLIENTE_Q = cliente('Q',9,17)
CLIENTE_R = cliente('R',11,19)
CLIENTE_S = cliente('S',1,20)
CLIENTE_T = cliente('T',20,20)

RUTA_A_B = rutaAerea( CLIENTE_A, CLIENTE_B)
RUTA_A_C = rutaAerea( CLIENTE_A, CLIENTE_C)
RUTA_A_F = rutaAerea( CLIENTE_A, CLIENTE_F)
RUTA_A_G = rutaAerea( CLIENTE_A, CLIENTE_G)
RUTA_B_D = rutaAerea( CLIENTE_B, CLIENTE_D)
RUTA_B_E = rutaAerea( CLIENTE_B, CLIENTE_E)
RUTA_B_G = rutaAerea( CLIENTE_B, CLIENTE_G)
RUTA_B_H = rutaAerea( CLIENTE_B, CLIENTE_H)
RUTA_C_D = rutaAerea( CLIENTE_C, CLIENTE_D)
RUTA_C_F = rutaAerea( CLIENTE_C, CLIENTE_F)
RUTA_C_G = rutaAerea( CLIENTE_C, CLIENTE_G)
RUTA_D_E = rutaAerea( CLIENTE_D, CLIENTE_E)
RUTA_D_F = rutaAerea( CLIENTE_D, CLIENTE_F)
RUTA_D_G = rutaAerea( CLIENTE_D, CLIENTE_G)
RUTA_D_H = rutaAerea( CLIENTE_D, CLIENTE_H)
RUTA_D_J = rutaAerea( CLIENTE_D, EMPRESA_J)
RUTA_D_K = rutaAerea( CLIENTE_D, CLIENTE_K)
RUTA_E_G = rutaAerea( CLIENTE_E, CLIENTE_G)
RUTA_E_H = rutaAerea( CLIENTE_E, CLIENTE_H)
RUTA_E_I = rutaAerea( CLIENTE_E, CLIENTE_I)
RUTA_F_K = rutaAerea( CLIENTE_F, CLIENTE_K)
RUTA_F_L = rutaAerea( CLIENTE_F, CLIENTE_L)
RUTA_F_S = rutaAerea( CLIENTE_F, CLIENTE_S)
RUTA_G_H = rutaAerea( CLIENTE_G, CLIENTE_H)
RUTA_G_I = rutaAerea( CLIENTE_G, CLIENTE_I)
RUTA_G_J = rutaAerea( CLIENTE_G, EMPRESA_J)
RUTA_H_I = rutaAerea( CLIENTE_H, CLIENTE_I)
RUTA_I_M = rutaAerea( CLIENTE_I, CLIENTE_M)
RUTA_I_N = rutaAerea( CLIENTE_I, CLIENTE_N)
RUTA_I_O = rutaAerea( CLIENTE_I, CLIENTE_O)
RUTA_J_K = rutaAerea( EMPRESA_J, CLIENTE_K)
RUTA_J_M = rutaAerea( EMPRESA_J, CLIENTE_M)
RUTA_J_N = rutaAerea( EMPRESA_J, CLIENTE_N)
RUTA_J_O = rutaAerea( EMPRESA_J, CLIENTE_O)
RUTA_J_Q = rutaAerea( EMPRESA_J, CLIENTE_Q)
RUTA_K_L = rutaAerea( CLIENTE_K, CLIENTE_L)
RUTA_K_Q = rutaAerea( CLIENTE_K, CLIENTE_Q)
RUTA_L_M = rutaAerea( CLIENTE_L, CLIENTE_M)
RUTA_L_O = rutaAerea( CLIENTE_L, CLIENTE_O)
RUTA_L_P = rutaAerea( CLIENTE_L, CLIENTE_P)
RUTA_L_Q = rutaAerea( CLIENTE_L, CLIENTE_Q)
RUTA_M_P = rutaAerea( CLIENTE_M, CLIENTE_P)
RUTA_M_Q = rutaAerea( CLIENTE_M, CLIENTE_Q)
RUTA_M_R = rutaAerea( CLIENTE_M, CLIENTE_R)
RUTA_N_O = rutaAerea( CLIENTE_N, CLIENTE_O)
RUTA_N_T = rutaAerea( CLIENTE_N, CLIENTE_T)
RUTA_O_Q = rutaAerea( CLIENTE_O, CLIENTE_Q)
RUTA_O_R = rutaAerea( CLIENTE_O, CLIENTE_R)
RUTA_O_T = rutaAerea( CLIENTE_O, CLIENTE_T)
RUTA_P_Q = rutaAerea( CLIENTE_P, CLIENTE_Q)
RUTA_P_S = rutaAerea( CLIENTE_P, CLIENTE_S)
RUTA_Q_S = rutaAerea( CLIENTE_Q, CLIENTE_S)
RUTA_R_S = rutaAerea( CLIENTE_R, CLIENTE_S)
RUTA_R_T = rutaAerea( CLIENTE_R, CLIENTE_T)
RUTA_S_T = rutaAerea( CLIENTE_S, CLIENTE_T)

CLIENTES = [
    CLIENTE_A,
    CLIENTE_B,
    CLIENTE_C,
    CLIENTE_D,
    CLIENTE_E,
    CLIENTE_F,
    CLIENTE_G,
    CLIENTE_H,
    CLIENTE_I,
    EMPRESA_J,
    CLIENTE_K,
    CLIENTE_L,
    CLIENTE_M,
    CLIENTE_N,
    CLIENTE_O,
    CLIENTE_P,
    CLIENTE_Q,
    CLIENTE_R,
    CLIENTE_S,
    CLIENTE_T
]

RUTAS_AEREAS = [
    RUTA_A_B,
    RUTA_A_C,
    RUTA_A_F,
    RUTA_A_G,
    RUTA_B_D,
    RUTA_B_E,
    RUTA_B_G,
    RUTA_B_H,
    RUTA_C_D,
    RUTA_C_F,
    RUTA_C_G,
    RUTA_D_E,
    RUTA_D_F,
    RUTA_D_G,
    RUTA_D_H,
    RUTA_D_J,
    RUTA_D_K,
    RUTA_E_G,
    RUTA_E_H,
    RUTA_E_I,
    RUTA_F_K,
    RUTA_F_L,
    RUTA_F_S,
    RUTA_G_H,
    RUTA_G_I,
    RUTA_G_J,
    RUTA_H_I,
    RUTA_I_M,
    RUTA_I_N,
    RUTA_I_O,
    RUTA_J_K,
    RUTA_J_M,
    RUTA_J_N,
    RUTA_J_O,
    RUTA_J_Q,
    RUTA_K_L,
    RUTA_K_Q,
    RUTA_L_M,
    RUTA_L_O,
    RUTA_L_P,
    RUTA_L_Q,
    RUTA_M_P,
    RUTA_M_Q,
    RUTA_M_R,
    RUTA_N_O,
    RUTA_N_T,
    RUTA_O_Q,
    RUTA_O_R,
    RUTA_O_T,
    RUTA_P_Q,
    RUTA_P_S,
    RUTA_Q_S,
    RUTA_R_S,
    RUTA_R_T,
    RUTA_S_T,
]

MAPA = grafo( CLIENTES, RUTAS_AEREAS)
for e in MAPA.aristasE:
    print(e)