Este código implementa un juego de fusión utilizando la biblioteca pygame. Comienza inicializando pygame, creando una ventana de 400x400 píxeles, y definiendo una cuadrícula de 4x4 para el juego. Se establece un sistema de colores y se inicializa un tablero vacío.

Las funciones clave incluyen:

draw_board(): Dibuja el tablero y muestra los números en las celdas.
add_random_tile(): Agrega un número (2 o 4) aleatorio en una celda vacía.
Clase Inventory: Maneja un inventario de artículos del jugador, permitiendo añadir, eliminar y mostrar artículos.
Funciones de movimiento (move_left(), move_right(), etc.): Mueven y fusionan las celdas según las teclas presionadas, actualizando el tablero en consecuencia.
game_turn(): Procesa cada turno del juego, añadiendo un nuevo número y verificando si el juego ha terminado.
check_game_over(): Comprueba si el juego ha llegado a su fin.
El ciclo principal del juego gestiona los eventos de teclado y actualiza la pantalla, permitiendo al jugador interactuar con el juego. Al final, pygame.quit() cierra la aplicación.
