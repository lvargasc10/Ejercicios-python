#Elaborado por Luisa Mabel Vargas Cárdenas

'''Un programa que dadas dos listas A y B de tamaño n,
entregue una tercera lista C con los elementos de A
que están en la posición dada por los elementos de B.'''

def elementos_en_b(a,b,contador):
    
    c =[]
    
    for i in range (0,len(a)):
        
        k = 0
        contador = 0
        
        for k in range (0,len(b)):
            
            if a[i]==b[i]:
                contador = contador + 1
                c.append(a[i])
    return c


k = 0
contador = 0

a = input("Ingrese el conjunto A: ")
b = input("Ingrese el conjunto B: ")

lista = elementos_en_b(a,b,contador)

print("C = : ",lista)

fin = input("Presione ENTER para terminar")
