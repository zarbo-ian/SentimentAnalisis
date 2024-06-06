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

datos_is_loaded = False


continuar = True
current_menu = 0

while continuar:
    if current_menu == 0:
        opcion = mostrar_menu()

        while opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida, por favor elige una opción del 1 al 4.")
            opcion = mostrar_menu()

        if opcion == "1":
            current_menu = 1
            while current_menu == 1:
                print("\nCarga de Datos:")
                print("Funcionalidad de carga de datos en desarrollo...")
                positivos, negativos = cargar_sentimientos(input("Ingrese el nombre del archivo de sentimientos: "))
                #positivos, negativos = cargar_sentimientos("sentimientos.txt")
                
                id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(input("Ingrese el nombre del archivo de comentarios: "))
                #id_publicacion_com, usuario_comentador, comentario = cargar_comentarios("comentarios.csv")
                usuario_comentador = quitar_apostrofe(usuario_comentador)
                
                id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(input("Ingrese el nombre del archivo de publicaciones: "))
                #id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones("publicaciones.csv")
                usuario_publicador = quitar_apostrofe(usuario_publicador)
                
                comentario = a_min_comentarios(comentario)    
                publicacion = a_min_comentarios(publicacion) 
                puntajes_comentarios = calcular_puntaje_comentarios(comentario, positivos, negativos)
                puntajes_publicaciones = calcular_puntaje_publicaciones(puntajes_comentarios, id_publicacion_com, id_publicacion_pub)
                datos_is_loaded = True
                current_menu = volver_atras(current_menu)


        elif opcion == "2" and datos_is_loaded:
            
            current_menu = 2
            while current_menu == 2:
                print("\nAnálisis de la Actividad de los Influencers:")
                print("1. Las 5 publicaciones con mejor calificación")
                print("2. El usuario publicador con más comentarios positivos")
                print("3. El usuario con mayor participación")
                print("4. Volver al menú anterior")
                n = input("A qué opción quieres ir (1-4)? ")

                if n == "1":
                    print("Las 5 publicaciones con mejor calificación")
                    mayor_promedio_publicacion, mayor_promedio_puntaje = usuarios_mejor_promedio(publicacion, puntajes_publicaciones)
                    #print("Usuarios con mejor promedio:", mayor_promedio_publicacion, mayor_promedio_puntaje)
                    print("PUBLICACION\t\tPUNTAJE")
                    i = 0
                    while i < len(mayor_promedio_publicacion):
                        print(mayor_promedio_publicacion[i] + "\t" + str(mayor_promedio_puntaje[i]))
                        i+=1
                elif n == "2":
                    print("El usuario publicador con más comentarios positivos")
                    top_user = usuario_mas_votado(usuario_publicador, puntajes_publicaciones)
                    print("Usuario mas votado:", top_user)
                elif n == "3":
                    print("El usuario con mayor participación")
                    usuario_mas_activo, participaciones, lista_actividad = usuario_mayor_participacion(usuario_comentador, usuario_publicador, id_publicacion_com, id_publicacion_pub)
                    print("El usuario más activo es:", usuario_mas_activo, "con", participaciones, "participaciones")
                    lista_actividad, lista_duplicas = ordenar_lista_actividad(lista_actividad)
                    print("Porque aparece en las publicaciones:", str(lista_actividad)[1:-1], "y aparece múltiples veces en las publicaciones:", str(lista_duplicas)[1:-1])
                elif n == "4":
                    current_menu = 0  # Volver al menú principal
                else:
                    print("Opción no válida, por favor elige una opción del 1 al 4.")
        
            if current_menu == 2 and n != "4":
                current_menu = volver_atras(current_menu)    

        elif opcion == "3" and datos_is_loaded:
            current_menu = 3
    
            while current_menu == 3:
                is_valid_input = False
                times_failed = 0
                while is_valid_input == False and current_menu == 3:
                    nom_usuario = input("Ingrese un nombre de usuario, alternativamente, escriba 'Salir' para volver al menú principal: ")
                    if nom_usuario in usuario_comentador or nom_usuario in usuario_publicador:
                        is_valid_input = True
                    elif nom_usuario == "SALIR" or nom_usuario == "Salir" or nom_usuario == "salir":
                        current_menu = volver_atras(current_menu)
                    else:
                        print("Nombre de usuario invalido. ", end= "")
                        is_valid_input = False
                        times_failed += 1
                        if times_failed >= 3:
                            current_menu = 0
                            is_valid_input = True  
                escribir_reporte(nom_usuario, usuario_comentador, usuario_publicador)          

        elif opcion == "4":
            print("Saliendo del programa...")
            continuar = False
        
        elif datos_is_loaded == False:
            print("Error. Debe cargar los datos primero")
            current_menu = 0