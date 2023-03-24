#Elaborado por Luisa Mabel Vargas Cárdenas - Buscaminas

print("¡Bienvenido a buscaminas! El juego consiste en despejar todas las casillas") 
print("de una pantalla que no oculten una mina. Algunas casillas tienen un número,")
print("este número indica las minas que suman todas las casillas circundantes.Si se")
print("descubre una casilla con una mina se pierde la partida. !Que comience el juego!")
      
import random

#-----
def matriz(longitud):
    
    tablero = []
    
    for i in range(0,longitud):
        
        mat = []
        for j in range(0,longitud):
            
            mat.append('?')
        tablero.append(mat)
        
    for f in range(0,longitud):
        
        print(tablero[f])
        
    return tablero

#-----

def crear_tablero(valor):
    
    tablero = []
    minas = valor
    longitud = valor    
    
    for i in range (0,longitud):
        
        mat = []
        for j in range(0,longitud):
            
            mat.append(0)

        tablero.append(mat)

    while minas != -1:
        
        b = random.randint(0,longitud-1)
        a = random.randint(0,longitud-1)       
        
        tablero[a][b]='*'
        
        minas = minas - 1

    for k in range (longitud):
        for h in range(longitud):
            
            num = acumulado(k,h,longitud,tablero)
            
            if tablero[k][h] != '*':
                tablero[k][h] = num
                
    return tablero

#-----

def acumulado(a,b,longitud,tablero):
    
    contador = 0
    
    for i in range (a-1,a+2):
        for j in range (b-1,b+2):
            
            if i <= longitud-1 and i >= 0 and j <= longitud-1 and j >= 0:
                if tablero[i][j] == '*':
                    
                    contador = contador + 1
    return contador

#-----

def buscaminas():
    
    longitud = int(input("\nIngrese el tamaño del tablero, debe ser un número ENTERO: "))
    print("El tamaño del tablero será de ",longitud,"x",longitud,"\n")
    tablero = crear_tablero(longitud)
    aviso = 0
    nueva_matriz = matriz(longitud)

    if longitud != int:
        buscaminas()
        
    while aviso != 1:
        
        posicion = input("\nIngrese una posición (0.1,1.5,5.1...etc.): ")
        p1 = int(posicion[0])
        p2 = int(posicion[2])
        
        if (tablero[p1][p2]=='*'):
            
            aviso = 1
        else:
            nueva_matriz[p1][p2] = tablero[p1][p2]
            
            for i in range (0,longitud):
                
                print(nueva_matriz[i])

    print("¡¡KABOOM!! Ha pisado una mina, perdió.")

buscaminas()
                
