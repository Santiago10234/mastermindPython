import random 

class Jugador:
    colores = ["red", "green", "yellow", "blue"]
    
    def __init__(self, el_jugador = True):
        self.el_jugador = el_jugador
        
class Creador(Jugador):
    def hace_codigo(self):
        if self.el_jugador:
            color_codigo = input("Ingrese el codigo de colores: ").strip().split()
        else:
            color_codigo = random.choices(self.colores, k=4)
        return color_codigo
    
    
class Adivinar(Jugador):
    def adivina_codigo(self):
        if self.el_jugador:
            color_codigo = input("Ingrese el codigo de colores a adivinar: ").strip().split()
        else:
            color_codigo = random.choices(self.colores, k=4)
        return color_codigo