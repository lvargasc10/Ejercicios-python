#Elaborado por Luisa Mabel Vargas Cárdenas.

def funcionpal(cadena):
    
    pal = True
    k = len (cadena) - 1
    i = 0    
    
    while (i < k and pal):
        while (cadena[i]== " "):
            i = i + 1
            
        while (cadena[k]== " " ):
            k = k - 1
            
        if (cadena[i] == cadena [k]):
            i = i + 1
            k = k + 1
        else:
            pal = False
            
        return pal

cadena = input (" Digíte la palabra o frase de la cual desea saber si es palíndrome: ")

resp = funcionpal (cadena)

if (resp == False):
    print ( cadena, ": No es palíndrome")
else:
    print (cadena, ": Es palíndrome")
    
fin = input("Presione ENTER para terminar")

