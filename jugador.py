import random

class Jugador:
    COLORES = ["r","g","y","b"]

    def __init__(self,es_el_jugador=True):
        self.es_el_jugador = es_el_jugador


class Creador(Jugador):
    def crea_codigo(self):
        if self.es_el_jugador:
            color_codigo = input("INGRESE EL CODIGO DE COLORES A CREAR: ").strip().split()
        else:
            color_codigo = random.choices(self.COLORES,k=4)

        return color_codigo

    
class Adivinador(Jugador):
    def adivinar_codigo(self):
        if self.es_el_jugador:
            color_codigo = input("INGRESE EL CODIGO DE COLORES A ADIVINAR: ").strip().split()
        else:
            color_codigo = random.choices(self.COLORES,k=4)

        return color_codigo