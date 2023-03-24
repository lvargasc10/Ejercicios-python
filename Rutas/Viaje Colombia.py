print(" BIENVENIDO A: Viaje por Colombia")
print(" ")
print("RUTAS:")
print(" ")
print("ORIGEN","  ","DESTINO")

rutas_ciudades = {}#Diccionario vacio.

def agregar_rutas(origen,destino,peajes):
    "Esta funcion se encarga de crear el diccionario"
    if origen not in rutas_ciudades:
        rutas_ciudades[origen]={}
        rutas_ciudades[destino]={}
        rutas_ciudades[origen][destino]=peajes
    else:
        rutas_ciudades[origen].update({destino:peajes})#Se concatenan con el .uptade()

archivo=open('rutas.txt','r')#Abro el archivo con las rutas.
linea=archivo.readline().strip(" ").split(" ")#Se lee la primera linea del archivo.
for linea in archivo:    
    linea = linea.strip()
    origen, destino, peajes = linea.split()#Se dividen las lineas del archivo en este caso en origen,destino y peso.
    agregar_rutas(origen,destino,int(peajes))#Se llama a la funcion "agregar_rutas" y se crea el diccionario. 
    
    print(origen,"--",destino)#Se muestran las rutas y su destino.
    
print(" ")
c_origen=str(input("Ingrese la ciudad de origen: "))#Se solicita al usuario que ingrese la ciudad de origen.
c_destino=str(input("Ingrese la ciudad destino: "))#Se solicita al usuario que ingrese la ciudad destino.

def dijkstra(rutas_ciudades,origen,destino,visitado=[],distancias={},antecesores={}):
    "Calcula la menor ruta(en este caso la ruta con menos peajes)"
       
    if origen == destino:         
        #Construimos el camino más corto y lo mostramos.
        camino=[]
        antecesor=destino
        while antecesor!= None:
            camino.append(antecesor)
            antecesor=antecesores.get(antecesor)             
        print('La ruta menos costosa es : '+ str([i for i in camino[::-1]])+ " y cuenta con : "+ str(distancias[destino]),"peajes.") 
    else :     
        # Se inicializa el costo si es la primera ejecucion
        if not visitado: 
            distancias[origen]=0
        #Pasa por los vertices adyacentes
        for adyacente in rutas_ciudades[origen] :
            if adyacente not in visitado:
                nueva_distancia = distancias[origen] + rutas_ciudades[origen][adyacente]                
                if nueva_distancia < distancias.get(adyacente,999):
                    distancias[adyacente] = nueva_distancia
                    antecesores[adyacente] = origen
        #Se establece si el vertice fue o no visitado
        visitado.append(origen)
        # Una vez se ha pasado por todos los vertices pasamos a la recursion 
        No_visitado={}
        for i in rutas_ciudades:
            if i not in visitado:
                No_visitado[i] = distancias.get(i,999)                
        origen2= min(No_visitado, key=No_visitado.get) # origen2 es el vertice no visitado con la distancia mas corta 
        dijkstra(rutas_ciudades,origen2,destino,visitado,distancias)# Se reemplaza el origen por origen2, y se ejecuta la funcion de manera recurrente


def principal():
# Se verifica que las ciudades origen y destino se encuentren en las rutas. Tambien si ya se encuentra en esa ciudad.
    if c_origen not in rutas_ciudades:
        print('La ciudad de origen no existe.')        
    if c_destino not in rutas_ciudades:
        print('La ciudad destino no existe.')
    elif c_origen==c_destino:
        print("¡Ya se encuentra en esa ciudad!")
    else:
        print(dijkstra(rutas_ciudades,c_origen,c_destino))
        
principal()
    
    
    














    
