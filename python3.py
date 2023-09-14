#========================================
# Juan David Garcia Vargas
#========================================
# Paradigmas de Programacion
# Matematica Algoritmica 
# ESFM-IPN 
#========================================

#==============================================
# Listas 
# Las listas 
#==============================================
miprimeralista =  [] # Lista vacia
print(miprimeralista)

#==================================================
# LLenado de lista
#==================================================
miprimeralista = [1,"David",1.34,"Bosco","Angel","Abigail",True]
print(miprimeralista)
#================================================
# list: hacer una lista 
# range(i,j) : secuencia de i hasta j-1 
#=================================================
nums = list(range(1,61))

for i in nums:
    print(i)

#====================================================
#  Incluir nuevos elementos en la lista 
#=======================================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#===========================================================
#  Quitar elementos de la lista
#===========================================================
nums.remove(61)
print(nums)

#================================================================
# Quitar elemento con indice i
#================================================================
i = 61
del nums[i]
print(nums)

#============================================
# Borrar la lista
#============================================
del nums


#=======================================
# Sumar  listas
#=======================================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#===================================================
# Llenado a mano 
#====================================================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])



                                                              37,1         
