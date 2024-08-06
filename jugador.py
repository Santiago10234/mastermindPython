import random
from termcolor import colored

colores = ["Red", "Green", "Yellow", "Blue"]
code_length = 4
maximo_intentos = 10

code = random.choices(colores, k=code_length)
intentos = 0