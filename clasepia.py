import datetime
#import librearia para usar los datos tipo fechas
class CONTACTO:
     #se definio la clase de CONTACTOS
     #se crea el metodo constructor _init_ para construir objetos cuando se instacie el mismo
    def __init__(self,NickName,Nombre,Correo,Telefono,FechaNacimiento,Gasto,Registro=datetime.datetime.now()):
        CONTACTO.NickName = NickName      #tipo string                      #se crea un default de registro que se almacenara
        CONTACTO.Nombre= Nombre           #tipo string                      # un datetime de la hora cuando se instacie el objeto
        CONTACTO.Correo = Correo          #tipo sitrng
        CONTACTO.Telefono= Telefono       #tipo string
        CONTACTO.FechaNacimiento = FechaNacimiento   #tipo datetime
        CONTACTO.Gasto= Gasto                        #tipo float
        CONTACTO.Registro= Registro                  #tipo datetime

