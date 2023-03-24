#Elaborado por Luisa Mabel Vargas Cárdenas

'''Organizar los números enteros de un arreglo
dejando todos los números pares antes de todos los números impares.'''

def numeros_pares(contador,lista):
    c = []
    for i in range (0,len(lista)):
        k = 0
        contador = 0
        if int(lista[i])%2==0:
                contador = contador + 1
                c.append(lista[i])
    return c

def numeros_impares(contador,lista):
    d = []
    for i in range (0,len(lista)):
        k = 0
        contador = 0
        if int(lista[i])%2!=0:
                contador = contador + 1
                d.append(lista[i])
    return d

k = 0
contador = 0

lista = input("Ingrese el conjunto de números: ")

pares = numeros_pares(contador,lista)
impares = numeros_impares(contador,lista)

print("La lista final es: ",pares+impares) #Está sería la lista ya con los pares e impares organizados.

fin = input("Presione ENTER para terminar")
