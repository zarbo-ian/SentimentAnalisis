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

fn= "comentarios.csv"

def cargar_datos_csv(comentarios):

    id_publicacion = []
    usuario_comentador = []
    comentario = []

    with open( comentarios ,"r" ) as archivo:
        lector = csv.reader( archivo )
        encabezados = next( lector ) #cambiar el next

        for linea in lector :
            id_publicacion.append ( linea[0] )
            usuario_comentador.append ( linea[1] )
            comentario.append ( linea[2] ) 
    
    return encabezados,id_publicacion,usuario_comentador,comentario


encabezados, id_publicacion_com, usuario_comentador, comentario = cargar_datos_csv(fn)

fl = "publicaciones.csv"

print(usuario_comentador)

def cargar_publicaciones(PUBLICACION):

    id_publicacion = []
    usuario_publicador = []
    publicacion = []

    with open(PUBLICACION, "r") as archivo:
        lector = csv.reader( archivo )
        encabezados = next( lector ) 

        for linea in lector :
            id_publicacion.append ( linea[0] )
            usuario_publicador.append ( linea[1] )
            publicacion.append ( linea[2] ) 
    
    return encabezados,id_publicacion,usuario_publicador,publicacion

encabezados,id_publicacion_pub,usuario_publicador,publicacion = cargar_publicaciones(fl)

print(publicacion)