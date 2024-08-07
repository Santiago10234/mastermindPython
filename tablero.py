from colored import fg,attr

class Tablero_juego:
    COLORES={
        "R":fg("red"),
        "G":fg("green"),
        "Y":fg("yellow"),
        "B":fg("blue")
    }
    
    def __init__(self):
        self.intentos = []
        self.colores_a_adivinar = []
    
    
    def establecer_colores(self, colores):
        self.colores_a_adivinar = colores
    
    def evaluar_intento(self, intento):
        retoalimentacion = []
        
    