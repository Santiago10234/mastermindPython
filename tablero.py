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
        retroalimentacion = []
        
        copia_colores_a_adivinar = self.colores_a_adivinar.copy()
        for i in range(4):
            if intento[i] == copia_colores_a_adivinar[i]:
                retroalimentacion.append("verde")
                copia_colores_a_adivinar[i] = None
            elif intento[i] in copia_colores_a_adivinar:
                retroalimentacion.append("amarillo")
                copia_colores_a_adivinar.remove(intento[i])
            else:
                retroalimentacion.append("blanco")
        return retroalimentacion
    
    
        
    