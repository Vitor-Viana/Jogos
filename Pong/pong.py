import pygame

def gameOver():
    while True:
        global s, bola_x, bola_y, placar, placarTotal
        event = pygame.event.poll()
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                s = placar = placarTotal = 0
                bola_x, bola_y = 560, 310
                break


def colisao(x, y):
    logic = False
    if ((bola_x + 70 > x) and (bola_x < x + 20)
    and (bola_y + 70 > y) and (bola_y < y + 90)):
        logic = True
    return logic

WHITE = (255, 255, 255)
bola_x, bola_y = 560, 310
velocidade_x = velocidade_y = 10
Raquete1_x, Raquete1_y = 20, 300
Raquete2_x, Raquete2_y = 1150, 300
s = placar = placarTotal = 0
pygame.init()

ImagemFundo = pygame.image.load("imagens/grama.jpg")
bola = pygame.image.load("imagens/bola.png")

font1 = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 50)
text1 = font1.render("Game Over", True, WHITE)
text2 = font2.render("pressione espaço para continuar a jogar", True, WHITE)
screen = pygame.display.set_mode((1190, 690))
pygame.display.set_caption("Pong")
audio = pygame.mixer.Sound("música/colisão.ogg")
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_UP) and (Raquete1_y > 0):
            Raquete2_y = Raquete1_y = Raquete1_y - 30
        if (event.key == pygame.K_DOWN) and (Raquete1_y + 90 < 690):
            Raquete2_y = Raquete1_y = Raquete1_y + 30

    # Movimento da bola
    bola_x += velocidade_x
    bola_y += velocidade_y

    # Colisão da bola com a raquete
    if (colisao(Raquete1_x, Raquete1_y)
    or colisao(Raquete2_x, Raquete2_y)):
        velocidade_x = -velocidade_x
        placarTotal += 1
        placar += 1
        audio.play()
    
    # Colisão da bola com as bordas horizontais
    if (bola_y + 70 > 690) or (bola_y < 0):
        velocidade_y = -velocidade_y
        audio.play()

    # Colisão da bola com as bordas verticais
    if (bola_x + 70 > 1190) or (bola_x < 0):
        s += 1
        if s == 3:
            screen.blit(text1, [400, 300])
            screen.blit(text2, [250, 400])
            pygame.display.flip()
            gameOver()
        else:
            bola_x, bola_y = 560, 310
            placar = 0
    
    screen.blit(ImagemFundo, (0, 0))
    
    pygame.draw.line(screen, WHITE, [595, 0], [595, 690], 8)
    pygame.draw.rect(screen, WHITE, [Raquete1_x, Raquete1_y, 20, 90])
    pygame.draw.rect(screen, WHITE, [Raquete2_x, Raquete2_y, 20, 90])

    screen.blit(bola, [bola_x, bola_y])
    
    text3 = font2.render(str(placar) + "  Acertos", True, WHITE)
    screen.blit(text3, [300, 20])
    text4 = font2.render("Total de acertos " + str(placarTotal), True, WHITE)
    screen.blit(text4, [680, 20])

    pygame.display.flip()
