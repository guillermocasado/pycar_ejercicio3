#Crear dos matrices pidiendo sus elementos y despues sumarlas
def suma_matrices(m1, m2):
    matrizsuma = []
    for i in range(n):
        fila = []
        for j in range(n):
            elem = m1[i][j] + m2[i][j] #esto porque se pone asi, y se puede poner [i, j]
            fila.append(elem)
        matrizsuma.append(fila)
    print('Suma de matrices:\n', matrizsuma)
    return matrizsuma

n = int(input('Dime la dimsension de la matriz: ')) #va a ser una matriz cuadrada
m1 = [] #crea una lista vacia
print('elementos de la primera matriz') #se puede poner mas abajo
for i in range(n): #hay que poner siempre los dos puntos
    fila = []
    for j in range(n):
        print('elemnto', i,' ', ' ', j) #esto es si queremos que lo vaya sacando por pantalla pero no es necesario, te van saliendo las posiciones de la matriz
        #va a ir rellenando por filas, fila 1, fila 2, etc
        elem = float(input('Dime los elementos de la matriz: ')) #float es para pedir numeros que pueden ser decimales
        fila.append(elem) #append sirve para añadir. Va a ir añadiendo cada elemento a la fila
    m1.append(fila)
print('Primera matriz leida:\n', m1) #n sirve para que aparezca impreso por pantalla debajo en vez de al lado

m2 = []
print('elementos de la segunda matriz') #se puede poner mas abajo
for i in range(n):
    fila = []
    for j in range(n):
        print('elemnto', i,' ', ' ', j) #esto es si queremos que lo vaya sacando por pantalla pero no es necesario, te van saliendo las posiciones de la matriz
        #va a ir rellenando por filas, fila 1, fila 2, etc
        elem = float(input('Dime los elementos de la matriz: ')) #float es para pedir numeros que pueden ser decimales
        fila.append(elem) #append sirve para añadir. Va a ir añadiendo cada elemento a la fila
    m2.append(fila)
print('Segunda matriz leida:\n', m1) #n sirve para que aparezca impreso por pantalla debajo en vez de al lado

matrizsuma = suma_matrices(m1, m2) #llama a la funcion suma_matrices


