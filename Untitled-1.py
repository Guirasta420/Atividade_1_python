# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
BLUE = ('blue')
X = 600
Y = 350
CIRCLE_x = 20
CIRCLE_y = 20
radius = 30
TAMANHO = 50
WHITE = ('white')

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    tela.fill(WHITE)

    teclas = pygame.key.get_pressed()
    if teclas [pygame.K_RIGHT]:
        X += 2
    elif teclas[pygame.K_LEFT]:
        X -= 2
    elif teclas[pygame.K_UP]:
        Y -= 2
    elif teclas[pygame.K_DOWN]:
        Y += 2        

    teclas = pygame.key.get_pressed()
    if teclas [pygame.K_d]:
        CIRCLE_x += 2
    elif teclas[pygame.K_a]:
        CIRCLE_x -= 2
    elif teclas[pygame.K_w]:
        CIRCLE_y -= 2
    elif teclas[pygame.K_s]:
        CIRCLE_y += 2  

    pygame.draw.rect(tela, BLUE, (X,Y,TAMANHO, TAMANHO))
    pygame.draw.circle(tela, BLUE, (CIRCLE_x,CIRCLE_y), TAMANHO)

    
    pygame.display.flip()

    pygame.time.Clock().tick(30)  

pygame.quit()