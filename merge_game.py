import pygame
import random

# Inicialización de pygame y configuración de la pantalla
pygame.init()
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 100
GRID_SIZE = 4  # Tamaño de la cuadrícula 4x4
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Merge")

# Definición de colores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Inicializar el tablero vacío
board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_board():
    """Dibuja el tablero en la pantalla."""
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = board[row][col]
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 2)
            if value:
                font = pygame.font.Font(None, 55)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def add_random_tile():
    """Agrega un número aleatorio en una celda vacía."""
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])

class Inventory:
    """Clase para manejar el inventario del jugador."""
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = {"Poción": 3, "Espada": 1}  # Inicializa con algunos artículos

    def add_item(self, item, quantity=1):
        """Añade un artículo al inventario."""
        if len(self.items) < self.capacity or item in self.items:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
            print(f"Agregado {quantity} de {item} al inventario.")
        else:
            print("Inventario lleno, no se puede añadir más artículos.")

    def remove_item(self, item, quantity=1):
        """Elimina un artículo del inventario."""
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
                print(f"Removido {quantity} de {item} del inventario.")
            elif self.items[item] == quantity:
                del self.items[item]
                print(f"{item} eliminado del inventario.")
            else:
                print("Cantidad a remover excede lo disponible en el inventario.")
        else:
            print(f"{item} no está en el inventario.")

    def show_inventory(self):
        """Muestra los artículos en el inventario."""
        if not self.items:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

# Inicializar el inventario
inventory = Inventory()
inventory.show_inventory()
inventory.remove_item("Poción", 1)
inventory.show_inventory()

# Funciones de sonido
pygame.mixer.init()
merge_sound = pygame.mixer.Sound("") # Establecer el path del sonido de fusion 

def play_merge_sound():
    """Reproduce el sonido de fusión."""
    merge_sound.play()

# Funciones de gestión del juego
def initialize_board():
    """Inicializa el tablero con dos piezas."""
    global board
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_random_tile()
    add_random_tile()

def slide_left(row):
    """Desliza las celdas a la izquierda y fusiona si es necesario."""
    new_row = [i for i in row if i != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
            play_merge_sound()  # Reproducir sonido de fusión
    return [i for i in new_row if i != 0] + [0] * (GRID_SIZE - len(new_row))

def move_left():
    """Mueve las celdas a la izquierda."""
    for r in range(GRID_SIZE):
        board[r] = slide_left(board[r])

# Funciones para rotar y mover el tablero
def rotate_board_clockwise():
    """Rota el tablero en el sentido de las agujas del reloj."""
    global board
    board = [list(row) for row in zip(*board[::-1])]

def move_right():
    """Mueve las celdas a la derecha."""
    rotate_board_clockwise()
    rotate_board_clockwise()
    move_left()
    rotate_board_clockwise()
    rotate_board_clockwise()

def move_up():
    """Mueve las celdas hacia arriba."""
    rotate_board_clockwise()
    rotate_board_clockwise()
    rotate_board_clockwise()
    move_left()
    rotate_board_clockwise()

def move_down():
    """Mueve las celdas hacia abajo."""
    rotate_board_clockwise()
    move_left()
    rotate_board_clockwise()
    rotate_board_clockwise()
    rotate_board_clockwise()

# Funciones para el ciclo principal del juego
def game_turn():
    """Procesa cada turno del juego."""
    global game_over
    add_random_tile()
    if check_game_over():
        game_over = True
        print("¡Juego terminado! Puntaje final:", score)

def check_game_over():
    """Verifica si el juego ha terminado."""
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                return False
            if r < GRID_SIZE - 1 and board[r][c] == board[r + 1][c]:
                return False
            if c < GRID_SIZE - 1 and board[r][c] == board[r][c + 1]:
                return False
    return True

# Inicializar el tablero
initialize_board()
score = 0
game_over = False

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Capturar teclas para mover el tablero
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            game_turn()

    draw_board()
    pygame.display.flip()

# Cerrar pygame
pygame.quit()
