#========================================
# Juan David Garcia Vargas
#========================================
# Paradigmas de Programacion
# Matematica Algoritmica 
# ESFM-IPN 
#=======================================


#=====================================================================
# Importar numpy, matplotlib, mpl_toolkits, time
#===================================================================
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm
import time 

#==================================================================
# Parametros que se pueden cambiar
#=====================================================
# Numero de celdas 
n = np.array([512,512])
# Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0])
# Constante de difusion 
k = 0.2
# Pasos de tiempo
pasos = 100

#=======================================================
# Parametros secundarios (no se deben cambiar)
#=======================================================
# Tamaño de las celdas 
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0],dx[1])**2)/k
print("dt = ", dt)
# Total de celdas 
nt = n[0]*n[1]
print("celdas = ",nt)

#=======================================================
# Arreglos Iniciales 
#============================================================
#Llenar la solucion con ceros
u = np.zeros(nt,dtype=np.float64)  # arreglo de lectura 
un = np.zeros(nt,dtype=np.float64)  # arreglo de escritura 

#=================================================================
# Evolucion temporal de la ecuacion diferencial parcial 
# u_t = k*laplaciano(u) (ecuacion de difusion de calor)
#=================================================================

