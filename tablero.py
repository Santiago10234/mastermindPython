from colored import fg,attr

class Tablero:
    COLORES = {
        "r":fg("red"),
        "g":fg("green"),
        "y":fg("yellow"),
        "b":fg("blue")
    }

    def __init__(self):
        self.turnos=[]
        self.color_adivinar=[]

    
    def definir_color(self,color):
        self.color_adivinar = color


    def comprobar_color(self,intento):
        retroalimentacion=[]

        copia_color_adivinar = self.color_adivinar.copy()
        for elemento in range(4):
            if intento[elemento] == copia_color_adivinar[elemento]:
                retroalimentacion.append("color_verde")
                copia_color_adivinar[elemento]=None
            elif intento[elemento] in copia_color_adivinar:
                retroalimentacion.append("color_amarillo")
                copia_color_adivinar.remove(intento[elemento])
            else:
                retroalimentacion.append("color_blanco")
        
        return retroalimentacion
    

    def mostrar_tabla(self):
        for intento,retroalimentacion in self.turnos:
            intento_jugado = " ".join([self.COLORES[color_jugado]+"o"+attr("reset") for color_jugado in intento])

            retroalimentacion_jugada = " ".join([
                fg(2) + "o" +attr("reset") if retro_adivina == "color_verde"

                else fg(3) + "o" + attr("reset") if retro_adivina == "color_amarillo"

                else "o"

                for retro_adivina in retroalimentacion
            ])

        print(f"{intento_jugado}|{retroalimentacion_jugada}")

    
    def actualizar_tablero(self,intento,retroalimentacion):
        self.turnos.append((intento,retroalimentacion))