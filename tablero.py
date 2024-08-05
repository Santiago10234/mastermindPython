from colored import fg,attr

class Tablero:
    COLORES = {
        "r": fg(1),
        "g": fg(1),
        "y": fg(1),
        "b": fg(1)
    }
    
    def __init__(self):
        self.color_secreto = []
        self.turnos = []
        
    def definir_color(self, color):
        self.color_secreto = color
        
    def validar_ganador(self, intento):
        retroalimentacion = []
        copia_color = self.color_secreto.copy
        for i in range(4):
            if intento[i] == copia_color[i]:
                retroalimentacion.append("color_verde")
                copia_color[i] = None
            elif intento[i] in copia_color:
                retroalimentacion.append("color_amarillo")
                copia_color.remove(intento[i])
            else: retroalimentacion.append("color_blanco")
        return retroalimentacion
    
    def mostrar(self):
        for intento, retroalimentacion in self.turnos:
            fila_color = " ".join([self.COLORES[color] + "⚪" + attr("reset") for color in intento])
            
        fila_retroalimentacion = " ".join([
            fg(2) + "⚪" + attr("reset") if adivina == "color_verde"
            
            else fg(3) + "⚪" + attr("reset") if adivina == "color_amarillo"
            
            else "⚪"
            
            for adivina in retroalimentacion
        ])
    
        print(f"{fila_color} {fila_retroalimentacion}")
    
    def actualiza(self,intento,retroalimentacion):
        self.turnos.append((intento, retroalimentacion))
