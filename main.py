###########################
####### FUNCION MENU ##########
###########################

from datos import *
from funciones import *

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
        #positivos, negativos = cargar_sentimientos("sentimientos.txt")
        sentimientos_is_loaded = True
        id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(input("Ingrese el nombre del archivo de comentarios: "))
        #id_publicacion_com, usuario_comentador, comentario = cargar_comentarios("comentarios.csv")
        comentarios_is_loaded = True
        id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(input("Ingrese el nombre del archivo de publicaciones: "))
        #id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones("publicaciones.csv")
        publicaciones_is_loaded = True
        

    elif opcion == "2":
        print ("Análisis detallado de la actividad de Influencers")
        comentario = a_min_comentarios(comentario)    
        publicacion = a_min_comentarios(publicacion) 
        puntajes_comentarios = calcular_puntaje_comentarios(comentario, positivos, negativos)
        puntajes_publicaciones = calcular_puntaje_publicaciones(puntajes_comentarios, id_publicacion_com, id_publicacion_pub)
        print(puntajes_comentarios)
        print(puntajes_publicaciones)    
    elif opcion == "3":
        print ("Generación de reportes")
        top_user = usuario_mas_votado(usuario_publicador, puntajes_publicaciones)
        print("Usuario mas votado:", top_user)
        mayor_promedio_usuario, mayor_promedio_puntaje = usuarios_mejor_promedio(usuario_publicador, puntajes_publicaciones)
        print("Usuarios con mejor promedio:", mayor_promedio_usuario, mayor_promedio_puntaje)
        usuario_mas_activo, participaciones = usuario_mayor_participacion(usuario_comentador, usuario_publicador)
        print("El usuario más activo es:", usuario_mas_activo, "con", participaciones, "participaciones")
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


