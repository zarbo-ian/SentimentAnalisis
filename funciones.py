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
