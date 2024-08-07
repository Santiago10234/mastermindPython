Estructura del Proyecto.
Mi proyecto está dividido en tres archivos principales: jugador.py, tablero.py y main.py

jugador.py contine las clases que representan a los jugadore en el juego.
tablero.py define la clase que maneja el tablero del juego y la logica asociada a las jugadas.
main.py es el punto de entrada del juego donde ejecuta el flujo del juego.

(jugador.py)
En jugador.py tengo la clase Jugador que define comportamientos y validaciones comunes para los jugadores.
En los metodos ponemos el constructor el cual inicializa el jugador, indicando si es el jugador humano o la IA.
Luego tenemos una validacion donde verifica que el codigo de colores tenga exactamente 4 colores validos.
En class creador le damos la posibilidad al jugador de que pueda crear su codigo de colores para que la IA adivine el codigo.
En class adivinador el usuario tendra que adivinar el codigo de colores generado por la IA.

(tablero.py)
tablero.py se emcarga de define la clase que maneja el tablero del juego y la logica asociada a las jugadas.
Tenemos una clase llamada Tablero que se encarga de manejar el estado del juego, incluyendo la definicion del codigo secreto, la comporobación de identidad y la visualizacion de resultados.
El constructor inicializa el tablero con una lista de turnos y el codigo a adivinar.

(main.py)
main.py es el punto de entrada del juego.
Tenemos una clase Juear que maneja el flujo del juego, incluyendo la seleccion de roles, la gestion de turnos y la determinacion del resultado final.
El construcator inicializa el juego configurado el tablero y los roles de los jugadores.
elegir_rol(self): Permite al jugador seleccionar su rol y configura el tablero con el código secreto.
