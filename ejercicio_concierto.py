#un evento de cardidad donde el minimo de aportacion es 500, la comision del artista si la aportacion es
# menor a 1000 se lleva el 20%, si es mayor a 1000 se lleva una comision fija de $300
#programa que calcule  la aportacion realizada y cuanto le tocara a la asociacion
import re
minimo= float(500.00)
valorfijo= float(300.00)
Aportaciones=[]
Comisiones=[]
# se crea la funcion ingresos con los parametros minimo y Aportaciones para ingresar las
#aportaciones y se validan si es un dato float y si es mayor a 500
def ingresos(minimo,Aportaciones):
    while True:
        # se calcula la longitud de la lista
        lon= len(Aportaciones)
        #se pregunta la cantidad a ingresar con su perspectivo folio
        _Aportacion= input("inserte la aportacion[{}]:".format(lon+1))
        #se valida que sea un dato float
        if re.search("^\d+(\.\d+)?$",_Aportacion):
            Aportacion= float(_Aportacion)
            if Aportacion< minimo:
                print("apotacion minima de 500.00")
            else:   # si aprieba las validaciones se retorna Aportacion y se termina el ciclo
                return Aportacion
                break
        else:
            print("dato invalido, ingrese una cantidad")
def ImprimirResultados(Apor,com):
    # se suman todas las aportaciones guardadas en la lista
    Total=0
    for x in Apor:
        Total += x
    # se suman todas las comisiones guardadas en la lista
    Total_Comsiones=0
    for x in com:
        Total_Comsiones +=x
    # se imprimen los resultados
    print("El ingreso total fue de:{}\nLa comision total del artista fue:{}".format(Total,Total_Comsiones))
    print("La asociacion reacudó:{}".format(Total-Total_Comsiones))
# se define una funcion que agrega las comsiones a la lista comsiones dependiendo si es<1000 agrega el .20
#y si es mayor agrega una cantidad de $300
def calcular_comision(cantidad,Aportaciones,Comisiones,valor):
    Aportaciones.append(cantidad)
    if cantidad<1000:
        porcentaje_comision= cantidad*.20
        Comisiones.append(porcentaje_comision)
    else:
        Comisiones.append(valor)
#bucle principal
while True:
    cantidad= ingresos(minimo,Aportaciones)
    calcular_comision(cantidad,Aportaciones,Comisiones,valorfijo)
    # preguntar si desea continuar
    Preguntar= input("deseas ingresar otra aportacion[si/no]: ")
    if Preguntar=="no":
        ImprimirResultados(Aportaciones,Comisiones)
        break
    else:
        print("")
        

