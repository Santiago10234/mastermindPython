import random

class Jugador:
    COLORES = ["r", "g", "y", "b"]

    def __init__(self, es_el_jugador=True):
        self.es_el_jugador = es_el_jugador

    def validar_codigo(self, codigo):
        return len(codigo) == 4 and all(c in self.COLORES for c in codigo)

class Creador(Jugador):
    def crea_codigo(self):
        if self.es_el_jugador:
            while True:
                color_codigo = input("INGRESE EL CODIGO DE COLORES A CREAR (4 colores, separados por espacios): ").strip().split()
                if self.validar_codigo(color_codigo):
                    return color_codigo
                else:
                    print("Código inválido. Debe ingresar exactamente 4 colores válidos (r, g, y, b).")
        else:
            return random.choices(self.COLORES, k=4)

class Adivinador(Jugador):
    def adivinar_codigo(self):
        if self.es_el_jugador:
            while True:
                color_codigo = input("INGRESE EL CODIGO DE COLORES A ADIVINAR (4 colores, separados por espacios): ").strip().split()
                if self.validar_codigo(color_codigo):
                    return color_codigo
                else:
                    print("Código inválido. Debe ingresar exactamente 4 colores válidos (r, g, y, b).")
        else:
            return random.choices(self.COLORES, k=4)
