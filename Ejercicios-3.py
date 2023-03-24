#Luisa Mabel Vargas Cardenas
'''
1. Elabore una función recurrente que entregue la posición del menor valor en un arreglo de
longitud n.
'''
def minimo(a):
    return minitu(0,a,0)

def minitu(i,a,r):
    r+=1
    if not a:
        ans=-1
    elif len(a)==1:
        ans=i
    else:
        if a[0]<=a[1]:
            ans=minitu(i,[a[0]]+a[2:],r)
        else:
            ans=minitu(r,a[1:],r)
    return ans
       
'''
2)Elabore dos funciones que calculen factorial de un número n, una de ellas de manera iterativa
y la otra de manera recurrente.
'''

def factorial_recursiva(numero): 
    if numero == 0:        
        return 1
    else:
        factorial = numero * factorial_recursiva(numero-1) 
        return factorial

#-----------------------------------------------------------

def factorial_iterativo(numero):
    factorial = 1
    for i in range(2,numero+1):
        factorial = factorial*i
    return factorial


'''
3)Elabore una función recurrente que convierta una cadena de dígitos en el número entero
que representa. Por ejemplo la cadena “5623” representa el número entero 5.623.
'''

def cadena_a_entero(cadena):
  if cadena:
     entero = (ord(cadena[-1]) - ord('0')) + 10 * cadena_a_entero(cadena[:-1])
     return entero
  else:
    return 0

'''
4) Implemente una función recurrente con la siguiente estrategia para sumar los elementos de
una lista de números. A es una lista de n enteros, donde n es una potencia de 2. Se crea una
nueva lista B del tamaño de la mitad de A y se asigna a cada B[i] = A[2i] + A[2i+1], para i = 0,1,
. . . , (n/2)−1. Si B tiene tamaño 1, se retorna B[0]. En cualquier otro caso se reemplaza A con
B, y se repite el proceso.
'''

def suma(lista):
    if len(lista)== 1:
        ans = lista[0]
    else:
        b = []
        for i in range (0,len(lista)//2):
            b.append(lista[2*i]+lista[2*i+1])
        ans = suma(b)
    return ans

'''
5) Escriba una función recurrente que dados dos conjuntos A y B, entregue A ∩ B.
'''
def AnB(a,b,contador):
    c = []
    for i in range (0,len(a)):
        k = 0
        contador = 0
        for k in range (0,len(b)):
            if a[i] == b[k]:
                contador = contador + 1
        if contador > 0:
            c.append(a[i])
    return c

k = 0
contador = 0
