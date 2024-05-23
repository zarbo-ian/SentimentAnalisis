import funciones as func
import datos

print("Elija: Carga de datos, Análisis de la actividad de los influencers, Reportes, Salir")

comando = input()
while comando != "Carga de datos" and comando != "Analisis" and comando != "Reportes" and comando != "Salir":
    comando = input("Comando invalido, ingrese nuevamente: ")

if comando == "Carga de datos":
    pass
elif comando == "Analisis":
    pass
elif comando == "Reportes":
    pass
elif comando == "Salir": 
    pass