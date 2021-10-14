# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300, 600] # Define size of windows
titulo = input('Dime el nombre del titulo:')
red = int(input('Dame la intensidad del rojo:'))
green = int(input('Dame la intensidad del verde:'))
blue = int(input('Dame la intensidad del azul:'))
colores = (red, green, blue) #variable con los tres colores
main2(size = size, titulo = titulo, colores = colores) #el = sirve para que no importe el orden en el que se introducen