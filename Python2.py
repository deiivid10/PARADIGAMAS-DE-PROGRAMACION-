#========================================
# Juan David Garcia Vargas
#========================================
# Paradigmas de Programacion
# Matematica Algoritmica 
# ESFM-IPN 
#========================================

#=========================================================
# Input permite obtener datos del usuario en prompter
#=========================================================
nombre = input("Dame tu nombre: ")
int("Hola como estas",nombre)

#======================================================================
# Los enteros son de precision ilimitada 
#=====================================================================
y = 5000000000000000000000000000000000000000000
print(y)

#==========================================
# La función int() cambia strings y floats a enteros
#==========================================
número = int(input("Dame tu edad: "))
type(numero)

#==========================================
# La notación científica de flotantes  utiliza e o E
#===========================================
# 1.2 x 10^{-9}
#===========================================
y = float("14.3")
print(y)

#=========================================================
# Los complejos se escriben con la raiz de menos uno
# j Siempre con su número como prefijo 
# No acepta la j suelta
#=========================================================
z = 1+1j

# Suma +
# Resta -
# Multiplicación *
# División /
# Módulo%
# Exponente **
# // Función Piso
# Funciones para transformar numeros int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159,4))

#=========================
# Strings de varias lineas 
#===========================
parrafo = """ En el bosque de la china 
 la chinita se perdio """
print(parrafo)
#================================
n=len(parrafo)
print(n)

#===================================================
# Las letras en un string ocupan lugares como un arreglo 
#  (También de atrás adelante comenzando en -1 el ultimo)
#==========================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])
