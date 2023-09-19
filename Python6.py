#========================================
# Juan David Garcia Vargas
#========================================
# Paradigmas de Programacion
# Matematica Algoritmica 
# ESFM-IPN 
#========================================

#===================================
# MI primer fumcion
#====================================
def saludo():
    #========================================
    # Documentacion rapida de la funcion 
    #=========================================
    """Esta funcion saluda"""
    print('¡Quiuboles!, ¿como estas?')

#=====================================================
# Llamado de la funcion 
#=====================================================
saludo()

#====================================
# SE ejecuta pero no se asigna 
#=====================================
salida = saludo()

#===================
# Esto no funciona
#====================
print(salida)

#===================
# ESto no funciona
#===================
print(salida)

#==============================
# Mostrar documentacion
#=============================
#help(saludo)

#===============================================
# Funcion con argumento
#==============================================
def salu2(nombre):
   """Esta funcion te saluda por tu nombre"""
   print("¡Que onda ese",nombre,"!")
salu2("Julian")
salu2("David")

#===========================================================
# Ahorrar trabajo del interprete 
# nombre:str la variable nombre es un str 
#============================================================
def saludos(nombre:str):
   """Esta funcion te saluda por tu nombre estrictamente"""
   print("¡Que onda ese", nombre,"!")
saludos("JUlian")
a = 123
print(type(a))
saludos(a)

#========================================
# Funcion con muchos argumentos 
#=========================================
def saludos_multiples(nombre1,nombre2,nombre3):
    """ESta funcion saluda a 3 personas al mismo tiempo"""
    print("Hola",nombre1,",",nombre2,"y", nombre3)
saludos_multiples("Hugo","Paco","Luis")

#================================================
# Funcion con cualquier numero de argumentos
#================================================
def muchos_saludos(*nombres):
    """Esta funcion saluda a todos los que quieras"""
    i = 0
    #============================================
    # end= es para ponerlo corrido
    #============================================
    print("Hola", end="")
    while len(nombres) > i:
      # ultimo nombre
      if (i==len(nombres)-1):
        print(nombres[i])
    else:
        # cualquier otro nombre 
        print(nombres[i], end=", ")
    i+=1

muchos_saludos("Armando","Paz","Diego","Mau","Nia","Pao","Ian","Luis","Angel","David")

def greet(firstname, lastname):
    print ('Hello', firstname, lastname)

#===========================================================================
# Llamar a la funcion con argumentos
#==========================================================================
greet(lastname='Jobs', firstname='Steve')

#====================================================
# Funcion con argumentos escondidos **
#====================================================
def greet(**person):
    #=============================================================
    # persona tiene caracteristicas firstname y lastname
    #================================================================
    print('Hello', person['firstname'], person['lastname']) 

greet(firstname='Steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates')  # se pueden pasar mas parametros de los necesarios

#=========================================
# Funcion con valores por defecto
#========================================
def greet(name = 'Guest'):
    print ('Hello', name)

greet() # Utiliza el valor dado de antemano
greet('Steve')

#======================================
# Funcion con resultado
#=======================================
def suma(a, b):
    return a + b

#=============================================================
# Programa funcional
# Se puede usar funciones dentro de funciones 
#================================================================
total=suma(5, suma(10, 20))
print(total)

#==========================================================
# Calculo lambda
# nombre de la funcion = lambda variable : funcion 
#==========================================================
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a1)


#================================
# Lambda de varias variables
#==================================
suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#=============================================
# Uso de una funcion anonima 
# El argumento va afuera entre parentesis
#==============================================
print((lambda x: x*x)(6)) # Funcion anonima

#==========================================
# Funcion con variable global
# EVITE EL EXCESO !!!!!!!!
#==========================================
name = 'Steve'
def greet():
    global name # Para utilizar una variable global (que viene fuera del bloque)
    name = 'Bill'
    print('Hello', name)
