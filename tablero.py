from colored import fg, attr

class Tablero:
    COLORES = {
        "r": fg("red"),
        "g": fg("green"),
        "y": fg("yellow"),
        "b": fg("blue")
    }

    def __init__(self):
        self.turnos = []
        self.color_adivinar = []

    def definir_color(self, color):
        if len(color) == 4 and all(c in self.COLORES for c in color):
            self.color_adivinar = color
        else:
            raise ValueError("El color a adivinar debe tener exactamente 4 colores válidos.")

    def comprobar_color(self, intento):
        if len(intento) != 4:
            raise ValueError("El intento debe tener exactamente 4 colores.")

        retroalimentacion = []
        copia_color_adivinar = self.color_adivinar.copy()

        for i in range(4):
            if intento[i] == copia_color_adivinar[i]:
                retroalimentacion.append("color_verde")
            elif intento[i] in copia_color_adivinar:
                retroalimentacion.append("color_amarillo")
            else:
                retroalimentacion.append("color_blanco")

        return retroalimentacion

    def mostrar_tabla(self):
        for intento, retroalimentacion in self.turnos:
            intento_jugado = " ".join([self.COLORES[color_jugado] + "𖦹" + attr("reset") for color_jugado in intento])
            retroalimentacion_jugada = " ".join([
                fg(2) + "𖦹" + attr("reset") if retro_adivina == "color_verde"
                else fg(3) + "𖦹" + attr("reset") if retro_adivina == "color_amarillo"
                else "𖦹"
                for retro_adivina in retroalimentacion
            ])
            print(f"{intento_jugado} | {retroalimentacion_jugada}")

    def actualizar_tablero(self, intento, retroalimentacion):
        self.turnos.append((intento, retroalimentacion))
