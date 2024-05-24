import csv

def cargar_sentimientos(FILE):
    try:
        positivos = []
        negativos = []

        with open(FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            def my_split(line):
                descriptor_end = False
                words = []
                word = []
                for char in line:
                    if char == ":":
                        descriptor_end = True
                    elif char == ",":
                        if descriptor_end:
                            words.append("".join(word).strip())
                            word = []
                    else:
                        if descriptor_end:
                            word.append(char)
                if word:
                    words.append("".join(word).strip())
                return words
        positivos = my_split(lines[0])
        negativos = my_split(lines[1])
        return positivos, negativos
    except FileNotFoundError:
        FILE = input("Error, Archivo no valido. Ingrese el nombre del archivo de sentimientos: ")

positivos, negativos = cargar_sentimientos("sentimientos.txt")
print(positivos)

def cargar_comentarios(FILE_COM):
    try:
        id_publicacion_com = []
        usuario_comentador = []
        comentario = []

        with open(FILE_COM, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            lines = list(reader)[1:]

            for row in lines:
                id_publicacion_com.append(int(row[0]))
                usuario_comentador.append(row[1])
                comentario.append(row[2])

        return id_publicacion_com, usuario_comentador, comentario
    except FileNotFoundError:
        FILE_COM = input("Error, Archivo no valido. Ingrese el nombre del archivo de comentarios: ")

def cargar_publicaciones(FILE_PUB):
    try:
        id_publicacion_pub = []
        usuario_publicador = []
        publicacion = []

        with open(FILE_PUB, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            lines = list(reader)[1:]

            for row in lines:
                id_publicacion_pub.append(int(row[0]))
                usuario_publicador.append(row[1])
                publicacion.append(row[2])
    
        return id_publicacion_pub, usuario_publicador, publicacion
    except FileNotFoundError:
        FILE_PUB = input("Error, Archivo no valido. Ingrese el nombre del archivo de publicaciones: ")
