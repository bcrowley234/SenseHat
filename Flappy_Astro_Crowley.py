
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
Yellow = (255, 255, 0)

x = 0
y = 0

matrix = [[BLUE for column in range(8)] for row in range(8)]

def flatten(matrix):
	flattened = [pixel for row in matrix for pixel in row]
	return flattened

def gen_pipes(matrix):
      row[-1] = RED
    gap = randint( 1, 6 )
    matrix[gap][-1] = BLUE
    matrix[gap + 1][-1] = BLUE
    matrix[gap - 1][-1] = BLUE
    return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + i]
        row[-1] = BLUE
    return matrix
def draw_astronaut(event):
    global x
    global y
    sense.set_pixel(x, y, Blue)
    if event.action == "pressed":
        if event.direction == "up":
            y -= 1
        elif event.direction == "down":
            y += 1
        elif event.direction == "right":
            x += 1
        elif event.direction == "left":
            x -= 1
    sense.set_pixel(x, y, YELLOW)
    
def check_collision(matrix):
    if matrix[y][x] == RED:
        return True
    else:
        return False

sense.stick.direction_any = draw_astronaut

while True:
    matrix = gen_pipes(matrix)
    if check_collision(matrix):
        break
    for i in range(3):
        matrix = move_pipes(matrix)
        sense.set_pixels(flatten(matrix))
        sense.set_pixel(x, y, YELLOW)   
        if check_collision(matrix):
            break
        sleep(1)