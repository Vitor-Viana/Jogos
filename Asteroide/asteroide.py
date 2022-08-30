from random import randint
import pygame

def TelaInicio():
    global pontuacao
    while True:
        clock.tick(60)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ganhando():
                    # Inicialização do jogo
                    pontuacao = 0
                    AsteroideInit()
                elif gameOver():
                    # Inicialização do jogo
                    pontuacao = 0
                    AsteroideInit()
                else:
                    break
        if ganhando():
            screen.blit(telaGanhou, (0, 0))
        elif gameOver():
            screen.blit(telaGameOver, (0, 0))
        else:
            screen.blit(telaInit, (0, 0))
        pygame.display.flip()
    
def ganhando():
    logic  = False
    if pontuacao == 100:
        logic = True
    return logic

def gameOver():
    logic = logicColisao = False
    # Colisão horizontal do asteroide
    for i in range(len(asteroide)):
        if asteroide[i][1] + 60 > 750:
            logicColisao = True

    if colisaoAsteroide(Nave_x, 600, 120, 120) or logicColisao:
        logic = True
    return logic    

def colisaoAsteroide(x, y, largura, altura):
    global pontuacao
    logic = False
    for i in range(len(asteroide)):
        if asteroide[i] != [0, 0]:
            if (x + largura > asteroide[i][0] and x < asteroide[i][0] + 60
            and y + altura > asteroide[i][1] and y < asteroide[i][1] + 60):
                if largura == 20:
                    asteroide[i] = [0, 0]
                    pontuacao += 1
                logic = True
    return logic
    
def  movimentoAsteroie():
    for i in range(len(asteroide)):
        if asteroide[i] != [0, 0]:
            asteroide[i][1] += 1
            screen.blit(Asteroide, [asteroide[i][0], asteroide[i][1]])

def AsteroideInit():
    global asteroide
    asteroide = []
    for i in range(100):
        asteroide.append([randint(1, 1140), randint(-2500, 0)])    

municao = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
pontuacao = 0
Nave_x = 540
asteroide = []

AsteroideInit()

pygame.init()
font           = pygame.font.SysFont("comicsansms", 30)
telaGanhou     = pygame.image.load("imagem/telaGanhou1200X750p.png")
telaInit       = pygame.image.load("imagem/telaInicio1200X750p.png")
telaGameOver   = pygame.image.load("imagem/gameover1200X750p.png")
Asteroide      = pygame.image.load("imagem/Asteroide60X60p.png")
audioTiro      = pygame.mixer.Sound("música/Tiro.ogg")
AudioGameOver  = pygame.mixer.Sound("música/GameOver.ogg")
Cenario        = pygame.image.load("imagem/Fundo1200X750p.png")
Nave           = pygame.image.load("imagem/Nave120X120p.png")
Bala           = pygame.image.load("imagem/Bala20X40p.png")
screen         = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("Asteroide")
clock          = pygame.time.Clock()

TelaInicio()

while True:
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    
    tecla = pygame.key.get_pressed()                                                          
    
    # Player
    # Movimentação Nave
    if tecla[pygame.K_RIGHT] == 1 and Nave_x + 120 < 1200:
        Nave_x += 10
    if tecla[pygame.K_LEFT] == 1 and Nave_x > 0:
        Nave_x -= 10
    
    # Tiro Nave
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT:
            for i in range(len(municao)):
                if municao[i] == [0, 0]:
                   municao[i] = [Nave_x + 50, 600]
                   audioTiro.play()      
                   break
                
    # ============ COLISÕES ============
    # Colisão do tiro com o asteroide
    for i in range(len(municao)):
        if municao[i] != [0, 0]:
            if colisaoAsteroide(municao[i][0], municao[i][1], 20, 40):
                municao[i] = [0, 0]
    # ==================================
    # colisão do tiro com a borda horizontal
    for i in range(len(municao)):
         if municao[i] != [0, 0]:
            if municao[i][1] < 0:
                municao[i] = [0, 0]
    # ========== FIM COLISÕES ==========
    
    # Cenário
    screen.blit(Cenario, (0, 0))
 
    # Asteroides
    movimentoAsteroie()

    # Movimento da bala 
    for i in range(len(municao)):
         if municao[i] != [0, 0]:
            screen.blit(Bala, [municao[i][0], municao[i][1]])
            municao[i][1] -= 10
               
    screen.blit(Nave, [Nave_x, 600])
    
    text = font.render("PONTUAÇÃO: " + str(pontuacao) + "%", True, (255, 255, 255))
    screen.blit(text, (40, 40))

    pygame.display.flip()

    # Fim de jogo
    if ganhando():
        TelaInicio()
    elif gameOver():
        AudioGameOver.play()
        TelaInicio()
