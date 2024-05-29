from datos import *

fn = "comentarios.csv"
id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(fn)

fo = "publicaciones.csv"
id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(fo)

def mostrar_reportes():
    is_valid_input = False
    times_failed = 0
    while is_valid_input == False:
        nom_usuario = input("Ingrese un nombre de usuario: ")
        if nom_usuario in usuario_comentador or nom_usuario in usuario_publicador:
            is_valid_input = True
        else:
            print("Nombre de usuario invalido. ", end= "")
            is_valid_input = False
            times_failed += 1
            if times_failed >= 3:
                #volver al menú principal
                pass
    #volver al menú principal

def a_min(S):
    rta = ""
    for i in range(len(S)):
        if 'A' <= S[i] <= 'Z':
            rta += chr(ord(S[i]) + 32)
        else:
            rta += S[i]
    return  rta


###########################
####### FUNCION MENU ##########
###########################
# def mostrar_menu():
#     print("Menú principal")
#     print("1. Carga de datos")
#     print("2. Análisis de la actividad de Influencers")
#     print("3. Reportes")
#     print("4. Salir")
#     n = input("Elige una opción (1-4): ")
#     return n

# def menu_analisis():
#     print("1. Las 5 publicaciones con mejor calificación")
#     print("2. El usuario publicador con más comentarios positivos")
#     print("3. El usuario con mayor participación")
#     print("4. Volver al menú anterior")
#     n = int(input("A que menu queres ir?"))
#     if n == "1":
#         print("1. Las 5 publicaciones con mejor calificación")
#     elif n == "2":
#         print("El usuario publicador con más comentarios positivos")
#     elif n == "3":
#         print("3. El usuario con mayor participación")
#     else:
#         print("Volver al menu principal")
     
    
    

# continuar = True

# while continuar:
#     opcion = mostrar_menu()

#     while opcion not in ["1", "2", "3", "4"]:
#         print("Opción no válida, por favor elige una opción del 1 al 4.")
#         opcion = mostrar_menu()

#     if opcion == "1":
#         print("Todo lo relacionado con datos")
    
#     elif opcion == "2":
#         menu_analisis()
    
    
#     elif opcion == "3":
#         print("Generación de reportes")
        
#     elif opcion == "4":
#         print("Saliendo del programa...")
#         continuar = False
#     else:
#         continuar = True  # Opcional, para dejar claro que el bucle sigue si ninguna condición previa se cumple.

#     if opcion != "4" and continuar:
#         volver = input("¿Quieres volver al menú principal? (s/n): ")
#         if volver != 's':
#             print("Saliendo del programa...")
#             continuar = False








# #####################################################
# ################ FUNCION MENU_ANALISIS###############
# #####################################################

# def menu_analisis():
#     print("Análisis de la Actividad de los Influencers:")
#     print("1. Las 5 publicaciones con mejor calificación")
#     print("2. El usuario publicador con más comentarios positivos")
#     print("3. El usuario con mayor participación")
#     print("4. Volver al menú anterior")
#     n = int(input("A que menu queres ir?"))
#     if n == "1":
#         print("1. Las 5 publicaciones con mejor calificación")
#     elif n == "2":
#         print("El usuario publicador con más comentarios positivos")

#     elif n == "3":
#         print("3. El usuario con mayor participación")
#     else:
#         print("Volver al menu principal")
# ########################################################################################
# ###################### FUNCION FILTRAR COMENTARIOS #####################################
# ########################################################################################