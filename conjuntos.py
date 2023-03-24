#Elaborado por Luisa Mabel Vargas Cárdenas

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

def A_B(a,b,contador):
    c=[]
    for i in range (0,len(a)):
        k = 0
        contador = 0
        for k in range (0,len(b)):
            if a[i] == b[k]:
                contador = contador + 1
        if contador == 0:
            c.append(a[i])
    return c

k = 0
contador = 0

a = input("Ingrese el conjunto A: ")
b = input("Ingrese el conjunto B: ")

AnB = AnB(a,b,contador)
A_B = A_B(a,b,contador)

print("Los elementos que se encuentran en las dos listas: ",AnB)
print("Los elementos que se encuentran en A y no en B: ",A_B)

fin = input("Presione ENTER para terminar")



