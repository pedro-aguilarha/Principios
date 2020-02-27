#desarollar un programa con eln uso de format
def main():  # se define una funcion main(principal)
    print("*AREA DE RECTANGULO*")
    _base= input("inserta la base: ")
    _altura= input("isnserta la altura: ")
    base= int(_base)   # se convierten de carater string a caracter int para
    altura= int(_altura) # poder manipular los datos en tipo  int
    area= base*altura
    txt="AREA:{} ({}*{})" # los corchetes se ultilizan como una llamada a una variable
    print(txt.format(area,base,altura)) # se llama la variable con el .format y se
main()  # se llama a la funcion main    # agregan en el orden deseado
