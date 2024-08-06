import random
from termcolor import colored

colores = ["Red", "Green", "Yellow", "Blue"]
code_length = 4
maximo_intentos = 10

code = random.choices(colores, k=code_length)
intentos = 0

def mostrar_colores(paleta):
    colores_disponibles = {
        "Red": "🔴",
        "Green": "🟢",
        "Yellow": "🟡",
        "Blue": "🔵"
    }
    return " ".join(colores_disponibles[color] for color in paleta)