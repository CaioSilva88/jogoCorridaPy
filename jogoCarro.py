import pygame
from random import randint
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

x = 400 #580,220
y = 100
pos_x = 230
pos_x_a = 380
pos_y = randint(800,1000)
pos_y_a = randint(1300,2000)  # carro meio
pos_y_b = randint(2300,3000)
e=0
e2 = -600

timer = 0
tempo_seg = 0



velocidade = 15
velocidade_outros = 20

fundo = pygame.image.load('rua.png')
fundo2 = pygame.image.load('rua.png')
carro = pygame.image.load('carroBranco.png')
policia = pygame.image.load('policia.png')
taxi =  pygame.image.load('taxi.png')
picape =  pygame.image.load('picape.png')
carro2 =  pygame.image.load('carroPreto.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo:",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

preto = (0,0,0)

janela = pygame.display.set_mode((800,600)) # tamando da tela
pygame.display.set_caption("Criando jogo com Python") # o que vai estar escrito na em cima da tela

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():    #evento: qualquer acao
        if event.type == pygame.QUIT: # caso feche a janela
            janela_aberta = False

    comandos = pygame.key.get_pressed()  # quando for pressionado uma tecla

    if comandos[pygame.K_d] and x<=580:
        x += velocidade
    if comandos[pygame.K_a] and x>=220:
        x -= velocidade
        # detecta colisao
    if comandos[pygame.K_SPACE]:
        x = 400
        y = 100

    # colisao
     #carro preto
    if((x + 134 > pos_x + 370 and y +180 > pos_y_b )):

        y = 1200
    # policia
    if((x < pos_x + 60 and y + 175 > pos_y)):
        y = 1200
    #picape
    if((x + 50 > pos_x + 130 and y + 180 > pos_y_a) and ( x < pos_x +200 and y + 180 > pos_y_a)):
        y = 1200

    # quando os carros passarem da tela

    if (pos_y <-60):
        pos_y = randint(1000,2000)
    if(pos_y_a<-60):  #picape
        pos_y_a = randint(3000,4000)
    if(pos_y_b<-60):
        pos_y_b = randint(6000,7000)
    if (timer <20):
        timer += 1
    else:
        tempo_seg += 1
        texto = font.render("Tempo: "+str(tempo_seg), True, (255, 255, 255), (0, 0, 0)) #cor, posicao
        timer = 0


    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_b -= velocidade_outros +10

    janela.blit(fundo, (0,0) ) #aparecer na tela
    janela.blit(carro,(x,y))
    janela.blit(policia,(pos_x,pos_y ))
    janela.blit(picape,(pos_x + 150,pos_y_a ))
    janela.blit(carro2,(pos_x + 300,pos_y_b))
    janela.blit(texto,pos_texto)
    pygame.display.update()

 #   pygame.draw.circle(janela, (0,255,0),(x,y),50)   #cor,onde vai aparecer na tela, raio em pixels


pygame.quit()