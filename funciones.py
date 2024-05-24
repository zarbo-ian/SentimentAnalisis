from datos import *

fn = "comentarios.csv"
id_publicacion_com, usuario_comentador, comentario = cargar_comentarios(fn)

fo = "publicaciones.csv"
id_publicacion_pub, usuario_publicador, publicacion = cargar_publicaciones(fo)

def mostrar_reportes():
    is_valid_input = False
    while is_valid_input == False:
        nom_usuario = input("Ingrese un nombre de usuario: ")
        if nom_usuario in usuario_comentador or nom_usuario in usuario_publicador:
            is_valid_input = True
        else:
            print("Nombre de usuario invalido. ", end= "")
            is_valid_input = False
    #volver al menú principal