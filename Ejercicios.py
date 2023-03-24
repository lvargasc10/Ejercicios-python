"Luisa Mabel Vargas Cardena - Correccion QUIZ MDIS"

"Punto 2"

#a) Suma de divisores de un numero entero.

def divisores(suma,num):
    if suma > num//2:
	    return num
    elif num % suma == 0:
	    return suma + divisores(suma+1,num)
    else:
	    return divisores(suma+1,num)
	
def suma_divisores(num):
	suma=1
	return divisores(suma,num)


#b) Organizar al final los impares y al inicio del arreglo los impares.
    
def pares_e_impares(lista):
    if lista == []:
        return []
    elif lista[0] % 2 == 0:
        return [lista[0]] + pares_e_impares(lista[1:])
    else:
        return pares_e_impares(lista[1:]) + [lista[0]]

#c) Determinar si la suma de los elementos de un arreglo da como resultado un numero perfecto.

def divisores(suma,lista):
    num = int(sum(lista))
    if suma > num//2:
        return 0
    elif num % suma == 0:
        return suma + divisores(suma+1,lista)
    else:
        return divisores(suma+1,lista)
	
def suma_divisores(lista):
	suma=1
	return divisores(suma,lista)


def suma_elementos(lista):  
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_elementos(lista[1:])

def perfecto(lista):
    if suma_elementos(lista) == suma_divisores(lista):
        return True
    else:
        return False

#d) Repetir un entero en un arreglo con su longitud, input: 5, output: [5,5,5,5,5,].

def repetir(n,k):
    if n==0:
        return []
    else:        
        return [k]+ repetir(n-1,k)

def rep(n):    
    return repetir(n,n)


"Punto 4"
#Ingresar un arreglo y un entero, devolver solo los extremos basandose en el entero, input: (2,[1,2,3,4,5,6]), output: [1,2,5,6].

def extremos(n,s):
    return s[:n]+s[-n:]







