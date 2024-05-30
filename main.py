###########################
####### FUNCION MENU ##########
###########################

from datos import *

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

sentimientos_is_loaded = False
comentarios_is_loaded = False
publicaciones_is_loaded = False

while continuar :
    opcion = mostrar_menu()

    while opcion not in ["1", "2", "3", "4"]:
        print ("Opción no válida, por favor elige una opción del 1 al 4.")
        opcion = mostrar_menu()

    if opcion == "1":
        print ("Todo lo relacionado con datos")
        positivos, negativos = cargar_sentimientos(input("Ingrese el nombre del archivo de sentimientos: "))
        sentimientos_is_loaded = True
        id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(input("Ingrese el nombre del archivo de comentarios: "))
        comentarios_is_loaded = True
        id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(input("Ingrese el nombre del archivo de publicaciones: "))
        publicaciones_is_loaded = True

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


