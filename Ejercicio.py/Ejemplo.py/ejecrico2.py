
#n = int(input("Ingresa un número:"))
#print(n >= 100)
# Se leen dos números
#number1 = int(input("Ingresa el primer número: "))
#number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
#if number1 > number2: larger_number = number1
#else: larger_number = number2

# Imprime el resultado
#print("El número más grande es:", larger_number)

#numero1 = int(input("Ingrese numero: "))
#numero2 = int(input("Ingrese numero: "))
#numero3 = int(input("Ingrese numero: "))

#numero_largo = numero1

#if numero2 > numero_largo:
    #numero_largo = numero2
    
#if numero3 > numero_largo:
    #numero_largo = numero3
    
#print("El numero mayor es: ", numero_largo)

##########################
#name = input("Introduce nombre: ")

#if name == "ESPATIFILIO":
 #   print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
#elif name == "espatifilio":
 #   print("su mamá hpta")
#else:
   #("Espatalitio,  no:", name )


# i = 2
# while i <= 30:
#      print(i)
#      i += 1

# for i in range(2,33,2):
#     print("El numero es: ", i)


# for i in range(20):
#     i+=1
#     print("El numero es: ", i)
# print("La suma es: ", 1*10)

##################
# Almacena el actual número más grande aquí.
# largest_number = -999999999

# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))

# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))

# # Imprime el número más grande.
# print("El número más grande es:", largest_number)
# ####
# identificador de numeros pares: if number % 2 == 1:
############## Counter ########
# counter = 5
# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)
####################

####################################### Bucle Mago #####

# secret_number = 777
# resultado= int(input("Ingresa un numero entero: "))

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)

# while resultado != secret_number:
#  print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
 
 
# if resultado == 777:
#    print("¡Bien hecho, muggle! Eres libre ahora.")

##################### Contar #######################
# print("Jugaremos a las escondidas")
# import time

# for expo in range(1,6):# Escribe un bucle for que cuente hasta cinco.
#     print(expo, "Mississippi")# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
#     time.sleep(1)# Cuerpo del bucle, emplea : time.sleep(1)

# print("¡Listos o no, ahí voy!")#

# break - ejemplo
# ################################### break y continue #######################################
# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

# resultado= input("Ingrese una palabra: ")
# chupacabra="chupacabra"

#  while resultado == chupacabra:
#      print("Eso es todo")
#      break
#  if resultado != chupacabra:
#      print("dentro del bucle")


########## Listas ##########
 
# n= [1,2,3,4,5,6,7,8,9]

# print(n[-1])
# print(n[-3])






################---------------------------------  ejercicios-----------------------------------------##########################
#-------------------------------------------------------------------------------------------------------------------------------



#------- ejercicio 1 --------#

# Nombre= input("ingrese su nombre: ")
# Edad=input("Ingrese su edad: ")
# Ciudad= input("Ingrese su ciudad de residencia: ")

# print("\nSus datos a continuación: " "\nSu nombre es: ", Nombre,"\nSu Edad es: ", Edad, "\nSu ciudad de residancia es: ", Ciudad )

# -------------- ejercicio 2 ----------------#

# Dias_trabajados= int(input("Ingrese el numero de dias trabajados: "))
# Valor_dias =80000

# print("Su paga es de: ", Dias_trabajados * Valor_dias)

# ---------------------------------------- ejercicio 3 -------------------------------#

# print("Bienvenido a la calculadora:" "\n")

# num1= float(input("Ingrese el primer numero: "))
# num2= float(input("Ingrese el segundo numero"))
# print("La suma es: ", num1 + num2)
# print("La resta es: ", num1 - num2)
# print("La multiplicación es: ", num1 * num2)
# print("La división es: ", num1 / num2)

#------------------------------------------ ejecicio 4 -----------------------------------------#

# monto= float(input("Ingrese el monto de su salario actual:"))
# descuento= monto-monto*0.5
# print("Su descueto es del 50%", descuento)

# ----------------------------------------- ejercicio 5 ----------------------------------------#

# ninos= 50
# ninas= 20
# total_ninos= ninos*100/70
# total_ninas= ninas*100/70


# print(f"Porcentaje niños: {total_ninos:.1f}""%")
# print(f"Porcentaje niñas: {total_ninas:.1f}""%")

#---------------------------------------- ejercicio 6 ------------------------------------------#

# import math

# r= float(input("Ingrese el radio: "))
# h= float(input("Ingrese la altura: "))
# Area = 2*math.pi*r*(r+h)
# Volumen= math.pi*r**2*h

# print("Area: ",Area)
# print("Volumen ", Volumen)

#--------------------------------------- ejercicio 7 -------------------------------------------#


# Valor_factura= float(input("Ingrese el valor de la factura: "))
# IVA= 0.19
# Valor_final= Valor_factura + Valor_factura * IVA

# print("EL monto del IVA es del 19%, por lo tanto el valor total es:", Valor_final)

#--------------------------------------- ejercicio 8 -------------------------------------------#

# nota1= float(input("Inserte nota 1 de la Evaluacion: "))
# nota2= float(input("Inserte nota 2 de la Evaluacion: "))
# nota3= float(input("Inserte nota 3 de la Evaluacion: "))

# porcentaje1=nota1*0.25
# porcentaje2=nota2*0.45
# porcentaje3=nota3*0.30

# total=porcentaje1+porcentaje2+porcentaje3

# print("Su nota final es; ", total)

#------------------------------------- ejercicio 9 ----------------------------------------------#

# salario_actual= float(input("Ingrese su salario actual: "))
# aumento:0.25
# subtotal= salario_actual*0.25
# total= salario_actual+subtotal

# print("Su total es de: ", total)

#------------------------------------- ejercicio 10 ---------------------------------------------#

# parcial1= float(input("Inserte Nota Parcial 1: "))
# parcial2= float(input("Inserte Nota Parcial 2: "))
# parcial3= float(input("Inserte Nota Parcial 3: "))
# examen_final= float(input("Inserte Nota Examen Final: "))
# trabajo_final= float(input("Inserte Nota Trabajo Final: "))

# subtotal1=((parcial1+parcial2+parcial3)/3)*0.55
# subtotal2=examen_final*0.3
# subtotal3=trabajo_final*0.15
# total=subtotal1+subtotal2+subtotal3

# print(f"\nNota Parciales: {subtotal1} \nNota Examen Final: {subtotal2}\nNota Trabajo Final: {subtotal3}\nSu nota final es de: {total}")

#------------------------------------ ejercicio 11 ----------------------------------------------#

# valor=float(input("Inserte el valor de su Salario: "))
# dias=float(input("Inserte el número de dias trabajados: "))

# salario_inicial=valor*dias
# pension=salario_inicial*0.05
# fondo=salario_inicial*0.03
# seguro=salario_inicial*0.024
# descuento=pension+fondo+seguro
# salario_final=salario_inicial-descuento

# print(f"\nSu salario es de: ${salario_final}\nPension: ${pension}\nFondo de Administracion: ${fondo}\nSeguro de discapacidad: ${seguro}\nDescuento: ${descuento}")

# number= 5
# number2= 4
# def message(number):
#     print("Ingresa un número:", number)

# message(number2)


# def message(what, number):
#     print("Ingresa", what, "número", number)

# message("teléfono", 11)
# message("precio", 5)
# message("número", "number")

# def introducción(first_name, last_name):
#  print("Hola, mi nombre es", first_name, last_name)

# introducción (first_name = "James", last_name = "Bond")
# introducción (last_name = "Skywalker", first_name = "Luke")

# def adding(a, b, c):
#  print(a, "+", b, "+", c, "=", a + b + c)

# adding(3, c = 1, b = 2)



# def xxdxdxdxdxdxdxdxdxdxdxd(Ig_de_la_minita, Id_de_tiktok):
#   print("Nombre de la loba es ", Ig_de_la_minita, "y el id es", Id_de_tiktok)

# xxdxdxdxdxdxdxdxdxdxdxd("nimuTV", "007" )
# xxdxdxdxdxdxdxdxdxdxdxd("Quiet","008")

#-----------------------------------------------------#

id_factura= input("Ingrese id de factura: ")
def ola(id_factura,numero_pago=500):
  print("El numero de pago esta en ", numero_pago, ", a la vez, la id de la factura es: ", id_factura)

ola(id_factura)










