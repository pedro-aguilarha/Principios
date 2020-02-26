import datetime  # se importa un modulo de datatime que se usara en la linea 8
txt= str(input("inserta una cadena: "))  # a continuacion se piden los datos con los que trabaremos
entero= int(input("inserta un entero: "))
dfloat= float(input("inserta un numero decimal: "))
dtime=(input("ingresa una fecha yyyy/mm/dd: "))
# se define una funcion para calcular los tipos de datos
def calcular(txt,entero,dfloat,dtime):
    año = dtime[0:4]
    mes =dtime[5:7]
    dia= dtime[-2:]
    fecha= datetime.datetime(int(año),int(mes),int(mes))
    resultado= {txt:type(txt),entero:type(entero),dfloat:type(dfloat),fecha: type(fecha)}
    return resultado
    # en la linea anterior se guardan el dato intreducido con su perspectivo tipo de dato en un diccionario
def imprimir(): # se  define una funcion para imprimir
    resultado= calcular(txt,entero,dfloat,dtime)  # se llama a la funcion calcular
    for x in resultado.items():  # se recorre el dicc resultado y se imprime
        print(x)
imprimir()
