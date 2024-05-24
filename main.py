###########################
####### FUNCION MENU ##########
###########################

from datos import id_publicacion_com , usuario_comentador , comentario
from datos import id_publicacion_pub , usuario_publicador , publicacion
from datos import positivos , negativos
import csv

def mostrar_menu() :
    print ("\nMenú principal")
    print ("1. Carga de datos")
    print ("2. Análisis de la actividad de Influencers")
    print ("3. Reportes")
    print ("4. Salir")
    n = input ("Elige una opción (1-4): ")
    return n

continuar = True

while continuar :
    opcion = mostrar_menu()

    while opcion not in ["1", "2", "3", "4"]:
        print ("Opción no válida, por favor elige una opción del 1 al 4.")
        opcion = mostrar_menu()

    if opcion == "1":
        print ("Todo lo relacionado con datos")
    elif opcion == "2":
        print ("Análisis detallado de la actividad de Influencers")
    elif opcion == "3":
        print ("Generación de reportes")
    elif opcion == "4":
        print ("Saliendo del programa...")
        continuar = False
    else:
        continuar = True  # Opcional, para dejar claro que el bucle sigue si ninguna condición previa se cumple.

    if opcion != "4" and continuar:
        volver = input ("¿Quieres volver al menú principal? (s/n): ")
        if volver != 's':
            print ("Saliendo del programa...")
            continuar = False


