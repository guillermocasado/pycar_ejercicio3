#Módulo que pide 3 datos numericos introduciendolos en una lista. Calcular y mostrar la media, mediana y varianza para esta lista
import statistics

list = [] #se crea una lista vacia donde se van a ir poniendo los numeros
numero1 = float(input('Dime el primer número: '))
list.append(numero1)
numero2 = float(input('Dime el segundo número: '))
list.append(numero2)
numero3 = float(input('Dime el tercer número: '))

list.append(numero3)

media = statistics.mean(list)
mediana = statistics.median(list)
varianza = statistics.variance(list)

print('Numeros: \n', list)

print('Media: \n',media)

print('Mediana: \n',mediana)

print('Varianza: \n',varianza)





