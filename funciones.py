from datos import *

# Variable para rastrear el menú actual
current_menu = 0

def mostrar_menu(): #Muestra el menu
    print("\nMenú principal")
    print("1. Carga de datos")
    print("2. Análisis de la actividad de Influencers")
    print("3. Reportes")
    print("4. Salir")
    n = input("Elige una opción (1-4): ")
    return n

def volver_atras(current_menu):
    respuesta = input("¿Qué deseas hacer? Si tu respuesta es 'S', volverás al menú anterior. Si es 'N', no te moverás de donde estás: ")
    while respuesta not in ['S', 's', 'N', 'n']:
        respuesta = input("Elige una opción válida ('S' o 'N'): ")
    if respuesta == 'S' or respuesta == 's':
        current_menu = 0  # Volver al menú principal
    return current_menu

def carga_datos():#Menu de carga de datos opcion 1
    current_menu = 1
    while current_menu == 1:
        print("\nCarga de Datos:")
        print("Funcionalidad de carga de datos en desarrollo...")
        current_menu = volver_atras(current_menu) #Vuelve al menu principal
    return current_menu

def menu_analisis(): #Menu de carga de analisis opcion 2
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
        elif n == "2":
            print("El usuario publicador con más comentarios positivos")
        elif n == "3":
            print("El usuario con mayor participación")
        elif n == "4":
            current_menu = 0  # Volver al menú principal
        else:
            print("Opción no válida, por favor elige una opción del 1 al 4.")
        
        if current_menu == 2 and n != "4":
            current_menu = volver_atras(current_menu)
    return current_menu

def menu_reportes(): #Menu de reportes opcion 3
    current_menu = 3
    while current_menu == 3:
        print("\nGeneración de reportes:")
        print("1. Reporte A")
        print("2. Reporte B")
        print("3. Reporte C")
        print("4. Volver al menú anterior")
        
        n = input("A qué opción quieres ir (1-4)? ")
        
        value = ["1","2","3","4"]
        
        while n not in value:
            print("Opcion Invalida, elija una opcion valida") 
            n = str(input("Ingrese una opcion valida"))
            if n == "1":
                print("Generando Reporte A")
            elif n == "2":
                print("Generando Reporte B")
            elif n == "3":
                print("Generando Reporte C")
            elif n == "4":
                mostrar_menu() # Volver al menú principal
        
        if current_menu == 3 and n != "4":
            current_menu = volver_atras(current_menu)
    return current_menu

fn = "comentarios.csv"
id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(fn)

fo = "publicaciones.csv"
id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(fo)

def my_split(line): #sustituto de .split()
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

def my_join(char_list): #sustituto de .join()
    result = ""
    for char in char_list:
        result += char
    return result

def my_count(comentario, frase): #sustituto de .count()
    counter = 0
    frase_len = len(frase)
    i = 0
    while i <= len(comentario) - frase_len:
        if comentario[i:i+frase_len] == frase:
            counter += 1
            i += frase_len
        else:
            i += 1
    return counter

def calcular_puntaje_comentarios(comentarios, positivos, negativos):
    puntajes = []
    for comentario in comentarios:
        puntaje = 0
        
        for i in positivos:
            puntaje += my_count(comentario, i)
        for i in negativos:
            puntaje -= my_count(comentario, i)
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
        
def quitar_apostrofe(strings):
    return [s[1:] for s in strings]


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

def usuario_mas_votado(usuarios, puntajes):
    puntaje_usuario = {}

    for i in range(len(usuarios)):
        usuario = usuarios[i]
        puntaje = puntajes[i]

        if usuario in puntaje_usuario:
            puntaje_usuario[usuario] += puntaje
        else:
            puntaje_usuario[usuario] = puntaje

    puntaje_maximo_usuario = None
    puntaje_maximo = float("-inf") #una infinidad negativa, para que cualquier valor, por más negativo que sea pueda comenzar la cuenta sigueinte

    for usuario, puntaje in puntaje_usuario.items():
        if puntaje > puntaje_maximo:
            puntaje_maximo = puntaje
            puntaje_maximo_usuario = usuario

    return puntaje_maximo_usuario

def usuarios_mejor_promedio(usuarios, puntajes):
    
    puntajes_usuarios = {}
    count_usuario = {}

    for i in range(len(usuarios)):
        usuario = usuarios[i]
        puntaje = puntajes[i]

        if usuario in puntajes_usuarios:
            puntajes_usuarios[usuario] += puntaje
            count_usuario[usuario] += 1
        else:
            puntajes_usuarios[usuario] = puntaje
            count_usuario[usuario] = 1

    
    promedio_usuarios = {}
    for usuario in puntajes_usuarios:
        promedio_usuarios[usuario] = round(puntajes_usuarios[usuario] / count_usuario[usuario], 1)

    usuarios_top = []
    puntajes_top = []

    while len(usuarios_top) < 5 and promedio_usuarios:
        usuario_max = None
        puntaje_max = float('-inf')

        for user in promedio_usuarios:
            if promedio_usuarios[user] > puntaje_max:
                puntaje_max = promedio_usuarios[user]
                usuario_max = user

        if usuario_max is not None:
            usuarios_top.append(usuario_max)
            puntajes_top.append(promedio_usuarios[usuario_max])
            del promedio_usuarios[usuario_max]

    return usuarios_top, puntajes_top

def usuario_mayor_participacion(comentadores, publicadores, id_pub_com, id_pub_pub):
    usuario_count = {}

    for user in comentadores:
        if user in usuario_count:
            usuario_count[user] += 1
        else:
            usuario_count[user] = 1
    
    for user in publicadores:
        if user in usuario_count:
            usuario_count[user] += 1
        else:
            usuario_count[user] = 1

    max_usuario = None
    max_count = 0

    for user, count in usuario_count.items():
        if count > max_count:
            max_usuario = user
            max_count = count

    #Lo siguiente dice en qué posts interactuó
    #si ya establecimos quien es el usuario con mas participaciones, aquí se verifica con cada lista
    #y se agrega el id de publicacion con el mismo index a la lista de actividad
    resultados = []
    i = 0
    while i < len(comentadores):
        if comentadores[i] == max_usuario:
            resultados.append(id_pub_com[i])
        i += 1
    i = 0
    while i < len(publicadores):
        if publicadores[i] == max_usuario:
            resultados.append(id_pub_pub[i]) 
        i += 1

    return max_usuario, max_count, resultados

#ordena la lista de de actividad con un insertion sort
def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

def ordenar_lista_actividad(array):
    sorted_array = insertion_sort(array)
    lista_completa = []
    lista_duplicas = []

    for num in sorted_array:
        if num in lista_completa:
            lista_duplicas.append(num)
        else:
            lista_completa.append(num)
    return lista_completa, lista_duplicas

# Analiza la cantidad de comentarios y publicaciones de un usuario y escribe el reporte
def escribir_reporte(user, archivo_1, archivo_2):
    numero_comentarios = 0
    for nombre in archivo_1:
        if nombre == user:
            numero_comentarios += 1
    
    numero_publicaciones = 0
    for nombre in archivo_2:
        if nombre == user:
            numero_publicaciones += 1
    
    with open("REPORTE.txt", "a") as file:
        file.write(f"Usuario: {user}\n")
        file.write(f"Cantidad de publicaciones: {numero_publicaciones}\n")
        file.write(f"Cantidad de comentarios: {numero_comentarios}\n")