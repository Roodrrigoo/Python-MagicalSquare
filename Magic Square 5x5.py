# Recuerda la suma de columnas filas y diagonales debe dar 65
contador=0 # En esta parte vamos a declarar un contador para que nos repita el proceso de imprimir

matriz =[[11, 0,7, 0,3],[ 0 , 12,25,8, 0],[17, 0,13, 0, 9],
    [ 0, 18, 0,14, 0],[23, 0,19, 0,0]]
#En esta parte vamos a declarar como queremos que este conformada nuestra matriz los ceros
# representan donde podemos elegir las coordenadas 

a1 =[[11, 0,7, 0,3],[ 0 , 12,25,8, 0],[17, 0,13, 0, 9],
    [ 0, 18, 0,14, 0],[23, 0,19, 0,0]]
#En esta parte declaramos otra matriz que no se va actualizar para recordar donde quedan los
#ceros
long=len(matriz)
#Medimos la longitud de la matriz
nombre=str(input('Ingrese su nombre: '))
#Pedimos el nombre del usuario
print('Hola',nombre)
print('vamos a resolver un cuadrado magico de 5x5')
print('Para resolverlo necesitas que las columnas filas y diagonales den un mismo numero')
print('En este caso 65')
print('Mucha suerte',nombre)

def cuadro_magico():
    for i in range(long): #En esta parte vamos a imprimir la matriz para que quede con forma
        print(matriz[i]) # de tablero
cuadro_magico()

while contador==0: # Esta es la funcion que nos hace loop hasta que se complete el cuadrado
    dato1=input('Ingrese las coordenadas: ')#El input de las coordenadas
    coordenadas= dato1.split()#Usamo la funcion split para dividirlo en 2
    if (len(coordenadas)!= 2)or(int(coordenadas[0])>5)or(int(coordenadas[1])>5):
# En esta parte vamos a verificar que escoja una coordenada correcta
       print('Ese no es un valor correcto')
    else:#Si es que es un valor correcto continuamos con el programa
        x=int(coordenadas[0])-1
        y=int(coordenadas[1])-1
        # Como sabemos python empieza desde cero por lo que a las coordenadas le restamos 1

        if(a1[x][y])==0:# En esta parte verificamos que la casilla elegida sea cero
            #Entonces se podra modificar
            valor=int(input('Ingrese el valor: '))
            matriz[x][y]=valor#En esta parte modificamos el valor en la matriz al ingresado por el
            #usuario
            diagonal=[]
            for i in range(long): # En esta parte vamos agregar a una lista todos los valores
                diagonal.append(int(matriz[i][i]))# de la diagonal
               
            horizontal=[] 
            for i in range(long):# En esta parte vamos a imprimir al lado de la matriz la suma
                horizontal.append(sum(matriz[i]))# de los elementos de sus filas
                print(matriz[i],sum(matriz[i]))
                #vamos a guardar en una lista las sumas para al final sumarlas
                
            columnas=[]
            for i in range(long):#En esta parte vamos a calcular la suma de las columnas
                columnas.append(sum([row[i] for row in matriz]))
            
            if (sum(columnas)==325)and(sum(horizontal)==325)and(sum(diagonal)==65):
                contador=1# Esta parte es donde verificamos si es que la suma de las columnas
                #filas y diagonales de 65
            
            lista4=[]
            for c in range(long):
                lista4.append(str(columnas[c]))  #En esta parte vamos a darle formato                                
            sr = ", ".join(lista4)# a como se imprimen las sumas de las columnas
            print(sr)
        else:
            print('La casilla ya esta ocupada favor de elegir otra')# Si la casilla
            # es diferente de cero desplegamos este mensaje

print('Felicidades',nombre,'completaste el cuadrado magico')



   
        