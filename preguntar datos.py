import datetime  # se importa un modulo de datatime que se usara en la linea 8
txt= str(input("inserta una cadena: "))  # a continuacion se piden los datos con los que trabaremos
entero= int(input("inserta un entero: "))
dfloat= float(input("inserta un numero decimal: "))
dtime=str(input("ingresa una fecha yyyy/mm/dd: "))
# se define una funcion para calcular los tipos de datos
def calcular(txt,entero,dfloat,dtime):
    fecha= datetime.datetime(int(dtime[0:4]),int(dtime[5:7]),int(dtime[-2:])) # se ultiliza el modulo
    resultado= {txt:type(txt),entero:type(entero),dfloat:type(dfloat),"fecha=":fecha}
    return resultado
    # en la linea anterior se guardan el dato intreducido con su perspectivo tipo de dato en un diccionario
def imprimir(): # se  define una funcion para imprimir
    resultado= calcular(txt,entero,dfloat,dtime)  # se llama a la funcion calcular
    for x in resultado.items():  # se recorre el dicc resultado y se imprime
        print(x)
imprimir()
