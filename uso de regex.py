import re # se importa un modulo para expresiones regulares
def main():
    while True:  # se hace un bucle infinito hasta que la condicion sea verdadera
        RFC= input("inserta tu RFC: ")
        coincide= re.search("^[A-Z]{4}-[0-9]{6}-[A-Z]{6}-[A-Z0-9]{2}$",RFC)
        #se usa el modulo re.Donde define la condicion que buscara la funcion search
        if(coincide):
            print("RFC CORRECTO") # si search devuelve un match verdadera se finaliza el bucle
            break
        else:
            print("RFC INCORRECTO,INTENTE DE NUEVO") # si el match es un none se vuelve a repetir el ciclo
main() # se llama la funcion
