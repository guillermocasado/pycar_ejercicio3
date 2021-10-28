#Crear una lista en la que cada elemento sea un diccionario de keywords en el que pida por teclado
#los datos de nombre y telefono. Se termina de introducir datos en la lista cuando el nombre es fin.

datos = [] #se crea una lita vacia llamada datod
while True:
    nombre = input('Dime tu nombre:')
    if nombre == 'fin':
        break
    apellidos = input('Dime tus apellidos:')
    telefono = input('Dime tu teléfono:')

    linea = {} #se crea el diccionario
    linea['Nombre'] = nombre
    linea['Apellidos'] = apellidos
    linea['Telefono'] = telefono

    datos.append(linea) #se añade el diccionario linea a la lista datos

print('Nombre, apellidos y telefono:\n', datos) #para que aparezcan los datos uno por uno