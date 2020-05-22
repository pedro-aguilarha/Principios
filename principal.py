import re #se importa el modulo re para trabajar con funciones regex
import csv #se importa el modulo csv para usar funciones de csv
import os   #se importa el modulo de sistema operativo
from clasepia import CONTACTO  #se importa la clase objeto del arhcivo clasepia
#se declara la lista donde se almacenaran los objetos de la clase contacto en el namespaces
conj_contactos=[]
#lo primero que hara el porgrama sera cargar el arhivo donde se guardan los contactos
# funcion con el nombre cargar_archivo
def Cargar_Archivo():
    #esta funcion crea un bloque donde se abrira el archivo csv
    with open('contactos_mobil.csv') as archivo_csv: #se guarda con un alias
        #la variable lector guardara lo que se lea del archivo contactos_mobil
        lector = csv.reader(archivo_csv,delimiter="|")  #se delimita por |
        contador_lineas = 0   #se crea un contador para contar cada linea que se lea del archivo
        for linea in lector:   # hacemos un barrido secuencial de lector donde
            if contador_lineas == 0:                 #se guardaron los datos del archivo csv
                # cuando contador empiece en 0, es decir en la liena de encabezados
                #se imprimirá los encabezados con la funcion para concatenar
                print(f'Los nombres de columna son {", ".join(linea)}')
            else:
                #se intancia el objeto temporal con los encabezados como atributos del objeto
                #de la clase CONTACTO
                objeto_temporal = CONTACTO({linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]})
                conj_contactos.append(objeto_temporal) # se agrega a la lista de contactos
            # Se incrementa el número de líneas, pase lo que pase.
            contador_lineas += 1
    #se imprime cuantos contactos se cargaron
    print(f"{len(conj_contactos)} Contactos Cargados")

#se define la funcion que despliega el menu principal
def Menu_Principal():
    #se cicla el menu hasta que la opcion sea igual a 0
    while True:
        #se limpia la pantalla
        LimpiarPantalla = lambda: os.system('cls')
        #se imprimen las funciones
        print("MENU CONTACTOS")
        print("[1] Agregar un contacto")
        print("[2] Buscar un contacto")
        print("[3] Eliminar un contacto")
        print("[4] Mostrar contactos")
        print("[5] Serializar datos")
        print("[0] Salir")
        _resp= input("Opcion: ")

        if _resp == "1":     #se llama a la funcion agregar a contacto
            Agregar_Contacto()
        elif _resp== "2":    #se llama a la funcion buscar contacto
            Buscar_Contacto()
        elif _resp== "3":    #se llama a la funcion eliminar contacto
            Eliminar_Contacto()
        elif _resp== "4":     #se llama a la funcion mostrar contacto
            Mostrar_Contactos()
        elif _resp == "5":    #se llama a la funcion seliarizar lista
            Serializar_Contacto()
        elif _resp == "0":
            print("programa finalizado")
            break    #se termina el ciclo con un break
        else:
            print("¡¡¡Opcion Invalida\tIntente de nuevo!!!")

def Validar():
    pass
def Agregar_Contacto():
    pass
def Buscar_Contacto():
    pass
def Eliminar_Contacto():
    pass
def Mostrar_Contactos():
    pass
def Serializar_Contacto():
    pass

#primero se cargaran los contactos del archivo csv
Cargar_Archivo()
#se muestra el menu principal
Menu_Principal()
