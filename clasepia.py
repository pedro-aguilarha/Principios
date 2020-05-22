import datetime
#import librearia para usar los datos tipo fechas
class CONTACTO:
     #se definio la clase
    def __init__(self,NickName,Nombre,Correo,Telefono,FechaNacimiento,Gasto,Registro=datetime.datetime.now()):
        CONTACTO.NickName = NickName
        CONTACTO.Nombre= Nombre
        CONTACTO.Correo = Correo
        CONTACTO.Telefono= Telefono
        CONTACTO.FechaNacimiento = FechaNacimiento
        CONTACTO.Gasto= Gasto
        CONTACTO.Registro= Registro

