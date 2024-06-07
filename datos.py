###########################################################
###En este archivo están las funciones de carga de datos###
###########################################################

import csv

def cargar_sentimientos(FILE):
    input_invalid = True
    while input_invalid == True:
        input_invalid = False
        try:
            positivos = []
            negativos = []
        
            with open(FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
                def my_split(line): # sustituto de .split
                    descriptor_end = False #El descriptor es la primera palabra "Positivas:" o "Negativas:"
                    words = []
                    word = []
                    for char in line:
                        if char == ":":
                            descriptor_end = True
                        elif descriptor_end:
                            if char == ",":
                                if word:
                                    words.append(my_join(word)) #Hace append, a insistencia de mi compañero explicaré lo que es un append: The append() method appends an element to the end of the list.
                                    word = []
                            elif char != " " and char != "\n":
                                word.append(char)
                    if word:
                        words.append(my_join(word))
                    return words
            
                def my_join(char_list): # sustituto de .join
                    result = ""
                    for char in char_list:
                        result += char
                    return result

            positivos = my_split(lines[0])
            negativos = my_split(lines[1])
            return positivos, negativos #los comantarios ahora están separados
        except FileNotFoundError:
            FILE = input("Error, Archivo no valido. Ingrese el nombre del archivo de sentimientos: ")
            input_invalid = True

def cargar_comentarios(FILE_COM):
    input_invalid = True
    while input_invalid == True:
        input_invalid = False
        try:
            id_publicacion_com = []
            usuario_comentador = []
            comentario = []

            with open(FILE_COM, "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                header_skipped = False #Saltea la primer fila, los descriptores
                for line in reader:
                    if not header_skipped:
                        header_skipped = True
                    else:
                        id_publicacion_com.append(int(line[0]))
                        usuario_comentador.append(line[1])
                        comentario.append(line[2])

            return id_publicacion_com, usuario_comentador, comentario
        except FileNotFoundError:
            FILE_COM = input("Error, Archivo no valido. Ingrese el nombre del archivo de comentarios: ")
            input_invalid = True

def cargar_publicaciones(FILE_PUB): #ඞ
    input_invalid = True
    while input_invalid == True:
        input_invalid = False
        try:
            id_publicacion_pub = []
            usuario_publicador = []
            publicacion = []

            with open(FILE_PUB, "r", encoding="utf-8") as file:
                reader = csv.reader(file)

                header_skipped = False #Saltea la primera fila
                for line in reader:
                    if not header_skipped:
                        header_skipped = True
                    else:
                        id_publicacion_pub.append(int(line[0]))
                        usuario_publicador.append(line[1])
                        publicacion.append(line[2])
    
            return id_publicacion_pub, usuario_publicador, publicacion
        except FileNotFoundError:
            FILE_PUB = input("Error, Archivo no valido. Ingrese el nombre del archivo de publicaciones: ")
            input_invalid = True
