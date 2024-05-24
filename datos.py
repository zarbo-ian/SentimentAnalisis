import csv

def cargar_sentimientos(FILE):
    

    with open(FILE, "r") as file:
        lines = file.readlines()

    descriptor1, words_line1 = lines[0].split(":", 1)
    positivos = [word.strip() for word in words_line1.split(",")]

    descriptor2, words_line2 = lines[1].split(":", 1)
    negativos = [word.strip() for word in words_line2.split(",")]
    return positivos, negativos

file_name = "sentimientos.txt"
positivos, negativos = cargar_sentimientos(file_name)

def cargar_comentarios(FILE_COM):

    id_publicacion_com = []
    usuario_comentador = []
    comentario = []

    with open(FILE_COM, "r") as file:
        reader = csv.reader(file)

        lines = list(reader)[1:]

        for row in lines:
            id_publicacion_com.append(int(row[0]))
            usuario_comentador.append(row[1])
            comentario.append(row[2])

    return id_publicacion_com, usuario_comentador, comentario

def cargar_publicaciones(FILE_PUB):
    id_publicacion_pub = []
    usuario_publicador = []
    publicacion = []

    with open(FILE_PUB, "r") as file:
        reader = csv.reader(file)

        lines = list(reader)[1:]

        for row in lines:
            id_publicacion_pub.append(int(row[0]))
            usuario_publicador.append(row[1])
            publicacion.append(row[2])
    
    return id_publicacion_pub, usuario_publicador, publicacion

