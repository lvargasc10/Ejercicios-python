
#Actividad 1

#Programa misterioso.

print("Think of a number between 1 and 100,but don't tell me what you choose.")

min_n = 1
max_n = 100
right_answer = False

while not right_answer:
    mid_n = (max_n + min_n + 1)//2
    answer = input("Is it " + str(mid_n)+"? ")
    if answer[0] == "y":
        right_answer = True
    elif answer.startswith("higher"):
        min_n = mid_n + 1
    elif answer.startswith("lower"):
        max_n = mid_n - 1
    else:
        print ("Sorry,I don't understand your answer.")

print ("Woohoo! I got it!")

#Fin programa

#Preguntas

#1) Si "answer" es "si" o sea "y" entonces esta es True.
#2) Solo una vez si la respuesta es "y".
#3) Para saber si el numero es correcto o para seguir buscando con "lower" o "higher".
#4) Espera "lower","higher" o "y", para ver si el numero es mayor,menor o es el que se propuso.
#5) Si la respues es "higher" el programa empieza a buscar el numero en los mayores al dado.
#6) Para establecer los posibles valores del numero pensado.
#7) EL algoritmo de busqueda binaria.

#Actividad 2

def numeros(lista):
    c = []    
    for i in range (0,len(lista)):        
        while len(c) < len(lista)-1:
            valor = int(lista[i])*int(lista[i+1])        
            i = i+ 1
            print (valor)
            c.append(valor)
    return c

i = 0
cantidad = int(input("Ingrese la cantidad de números de la lista: "))
lista=[]

while cantidad != i:        
        numero=input("Ingrese el numero: ")
        lista.append(numero)
        i = i + 1         
    
print("La lista final es: ",numeros(lista))


#Actividad 3

def entero(lista):         
    for i in range (0,len(lista)-1):        
        valor = int(lista[i])+ int(lista[i+1])
        i = i+ 1                   
    return valor
    valorf = valor / cantidad
    return valorf

def mayor(lista):    
    mayor=lista[0]
    for valor in lista:
        if valor > mayor:
            mayor = valor            
    return mayor

def menor(lista):    
    menor=lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor            
    return menor

i = 0
cantidad = int(input("Ingrese la cantidad de números de la lista: "))
lista=[]

while cantidad != i:        
        numero=input("Ingrese el numero: ")
        lista.append(numero)
        i = i + 1         
intervalo = []
intervalo.append(menor(lista))
intervalo.append(mayor(lista))
print("El conjunto de valores se encuentra en el intervalo: ",intervalo)
print("El valor promedio es: ",entero(lista))





