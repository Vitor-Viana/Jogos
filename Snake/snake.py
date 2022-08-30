from time import sleep
from random import randint
import pygame

def Apple():
    x = randint(0, 590)
    y = randint(0, 590)
    x = (x // 10) * 10
    y = (y // 10) * 10
    return (x, y)

apple = Apple()
BLACK, ORANGE, BLUE, WHITE = (0, 0, 0), (255, 185, 155), (0, 0, 255), (255, 255, 255)
UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
cobra = [(300, 300), (310, 300), (320, 300), (330, 300)]
direction = LEFT
logic = False

pygame.init()
audio1 = pygame.mixer.Sound("música/comer.ogg")
audio2 = pygame.mixer.Sound("música/colisão.ogg")
font = pygame.font.SysFont(None, 60)
text = font.render("Game Over", True, WHITE)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Cobra Assassina")
clock = pygame.time.Clock()

while True:
    clock.tick(10)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and direction != DOWN:
            direction = UP
        if event.key == pygame.K_DOWN and direction != UP:
            direction = DOWN
        if event.key == pygame.K_RIGHT and direction != LEFT:
            direction = RIGHT
        if event.key == pygame.K_LEFT and direction != RIGHT:
            direction = LEFT
    # Colisão da cobra com a cobra
    for i in range(1, len(cobra)):
        if cobra[0] == cobra[i]: logic = True
    # Colisão da cobra com a apple
    if cobra[0][0] == apple[0] and cobra[0][1] == apple[1]:
        audio1.play()
        apple = Apple()
        cobra.append((0, 0))
    # Mover a cobra  
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = cobra[i-1]
    # Colisão com as bordas
    if (cobra[0][0] < 0 or cobra[0][0]+10 > 600 or
    cobra[0][1] < 0 or cobra[0][1]+10 > 600): logic = True
    # Game Over
    if logic == True:
        audio2.play()
        screen.blit(text, [190, 200])
        pygame.display.flip()
        sleep(5)
        break
    # mover a cabeça da cobra
    if direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    elif direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    elif direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    else:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    screen.fill(BLACK)
    pygame.draw.rect(screen, ORANGE, [apple[0], apple[1], 10, 10])
    for xy in cobra:
        pygame.draw.rect(screen, BLUE, [xy[0], xy[1], 10, 10])
    pygame.display.flip()
