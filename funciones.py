from datos import *

fn = "comentarios.csv"
id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(fn)

fo = "publicaciones.csv"
id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(fo)

def my_split(line): #sustituto de .split
    descriptor_end = False
    words = []
    word = []
    for char in line:
        if char == ":":
            descriptor_end = True
        elif descriptor_end:
            if char == ",":
                if word:
                    words.append(my_join(word))
                    word = []
            elif char != " " and char != "\n":
                word.append(char)
    if word:
        words.append(my_join(word))
    return words

def my_join(char_list): #sustituto de .join
    result = ""
    for char in char_list:
        result += char
    return result

def calcular_puntaje_comentarios(comentarios, positivos, negativos):
    puntajes = []
    for comentario in comentarios:
        puntaje = 0
        
        for i in positivos:
            puntaje += comentario.count(i)
        for i in negativos:
            puntaje -= comentario.count(i)
        puntajes.append(puntaje) 
    
    return puntajes

def calcular_puntaje_publicaciones(puntaje_com, id_comentario, id_publicacion):
    puntaje_pub = {post: 0 for post in id_publicacion}

    for i in range(len(puntaje_com)):
        puntaje = puntaje_com[i]
        coment = id_comentario[i]
        if coment in puntaje_pub:
            puntaje_pub[coment] += puntaje
    puntaje_final = [puntaje_pub[post] for post in id_publicacion]
    return puntaje_final
        


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
    for i in S:
        if 'A' <= i <= 'Z':
            rta += chr(ord(i) + 32)
        else:
            rta += i
    return  rta

def a_min_comentarios(comentarios):
    return [a_min(item) for item in comentarios]

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

import sys

def reporte():
    
    #abre y estructura el primer csv
    with open("itba\publicaciones.csv") as file:
        publicaciones = file.readlines()
        publicaciones = estructurar_csv(publicaciones)
    
    #abre y estructura el segundo csv
    with open("itba\comentarios.csv") as file:
        comentarios = file.readlines()
        comentarios = estructurar_csv(comentarios)

    user = get_valid_user(comentarios,publicaciones)
    escribir_reporte(user,comentarios,publicaciones)
    
    print(user)

#devuelve csv estructurado
def estructurar_csv(archivo):
    archivo_estructurado = []
    for linea in archivo:
        linea = linea.strip("\n").split(",")
        archivo_estructurado.append(linea)
    return archivo_estructurado

#devuelve un usuario valido que se encuentre en al menos un archivo
def get_valid_user(archivo_1,archivo_2):
    for intentos in range(3):
        check_1 = False
        check_2 = False
        
        user = input("Escribe el usuario de la persona que quieres buscar: ")
        
        for linea in archivo_1:
            if user == linea[1]:
                check_1 = True
                break

        for linea in archivo_2:
            if user == linea[1]:
                check_2 = True
                break

        if (check_1 == True) or (check_2 == True):
            return user
        
    sys.exit("Exediste el numero maximo de intentos")

#analiza la cantidad de comentarios y publicaciones de un usuario y escribe el reporte
def escribir_reporte(user,archivo_1,archivo_2):
    numero_comentarios = 0
    for usuario in archivo_1:
        if user == usuario[1]:
            numero_comentarios +=1
    
    numero_publicaciones = 0
    for usuario in archivo_2:
        if user == usuario[1]:
            numero_publicaciones +=1
    
    with open("itba\REPORTES.txt","a") as file:
        file.write(f"Usuario: {user}\n")
        file.write(f"Cantidad de publicaciones: {numero_publicaciones}\n")
        file.write(f"Cantidad de comentarios: {numero_comentarios}\n")
reporte()
