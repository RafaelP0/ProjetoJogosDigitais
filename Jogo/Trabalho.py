import sys, pygame, random, pygame
from pygame.locals import *
from random import *

pygame.init()

screen_width = 1200
screen_height = 750
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Papa Bolinhas")

imagem = pygame.image.load("img/imagem_fundo.png")
imagem = pygame.transform.scale(imagem, (size))

pacote = pygame.image.load("sprites/pacote.png")
	
pacote = pygame.transform.scale(pacote, (20, 20))

nave = pygame.image.load("sprites/nave.png")
nave = pygame.transform.scale(nave, (40, 40))

bus = pygame.image.load("sprites/bus.png")
bus = pygame.transform.scale(bus, (550, 170))

Pacotes=[]
Pacotes=["sprites/pacotes/pacote0.png","sprites/pacotes/pacote1.png", "sprites/pacotes/pacote2.png", "sprites/pacotes/pacote3.png","sprites/pacotes/pacote4.png", "sprites/pacotes/pacote5.png", "sprites/pacotes/pacote6.png", "sprites/pacotes/pacote7.png", "sprites/pacotes/pacote8.png", "sprites/pacotes/pacote9.png", "sprites/pacotes/pacote10.png", "sprites/pacotes/pacote11.png", "sprites/pacotes/pacote12.png", "sprites/pacotes/pacote13.png", "sprites/pacotes/pacote14.png", "sprites/pacotes/pacote15.png", "sprites/pacotes/pacote16.png", "sprites/pacotes/pacote17.png", "sprites/pacotes/pacote18.png",]

BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans',40)
placar = 0


def valoresConta():
    a = randint(0, 18)
    c = randint(0, 18)
    while a > c:
        c = randint(0, 18)
    b = c - a
    return [a,b,c]

def array(b):
    # Crie um array de 10 elementos
    array_de_valores =[]
    array_de_valores.append(b)
    
    n=0
    while n <9:
        a = randint(0, 18)
        # Adicione o valor de 'b' ao array
        while a in array_de_valores:
            a = randint(0, 18)
            
        while a == b:
            a = randint(0, 18)
        array_de_valores.append(a)
        n+=1
    # Imprima o array resultante
    print(array_de_valores)
    return array_de_valores

    
class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, raio, ponto, AA):
        super().__init__()
        self.valor = AA
        print(self.valor)
        if AA == b:
            self.ponto=1
        else:
            self.ponto= 0
        a=[]
        a=pygame.image.load(Pacotes[AA]).convert_alpha()
        a= pygame.transform.scale(a, (30, 30))
        self.image = a
        
        self.rect = self.image.get_rect(center=(x, y))


        self.velocity = [choice([-1, 1]), choice([-1, 1])]
        

    def update(self):
        self.rect.move_ip(self.velocity)
        
        if self.rect.left < 0 or self.rect.right > screen_width:
                self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
                self.velocity[1] *= -1

            




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = nave

        
        self.rect = self.image.get_rect(center=(400, 300))


    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
 
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
            
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        
        self.rect.clamp_ip(screen.get_rect())


def create_circle(values):
    for i in range(10):
        X_vermelho = randint(40, (screen_width - 50))
        Y_vermelho = randint(40, (screen_height - 50))
        raio = 20
        circle = Circle(X_vermelho, Y_vermelho, raio, 1, values[i] )
        if values[i] == b:
            circlelo.add(circle)
        else:
            circles.add(circle)  # Adicione o círculo diretamente ao grupo 'circles'


circles = pygame.sprite.Group()  # Crie o grupo 'circles'
circlelo = pygame.sprite.Group()  # Crie o grupo 'circles'
a,b,c = valoresConta()
create_circle(array(b))
        

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


clock = pygame.time.Clock()

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 
temporizador = 60

def killCircles():
    for c1 in circles:              
        c1.kill()
    for c2 in circlelo:              
        c2.kill()
        
        
def menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False
                elif event.key == pygame.K_2:
                    creditos()
                elif event.key == pygame.K_3:
                    opcoes()

        screen.blit(imagem, (0, 0))
        screen.blit(bus, ((screen_width / 2) - 90, 8))

        menu_text = font.render('Menu:', True, WHITE)
        screen.blit(menu_text, (screen_width / 2 - menu_text.get_width() / 2, 200))

        option1_text = font.render('1 - Iniciar Jogo', True, WHITE)
        screen.blit(option1_text, (screen_width / 2 - option1_text.get_width() / 2, 300))

        option2_text = font.render('2 - Créditos', True, WHITE)
        screen.blit(option2_text, (screen_width / 2 - option2_text.get_width() / 2, 350))

        option3_text = font.render('3 - Opções', True, WHITE)
        screen.blit(option3_text, (screen_width / 2 - option3_text.get_width() / 2, 400))

        pygame.display.flip()


def creditos():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)

        creditos_text = font.render('Créditos:', True, WHITE)
        screen.blit(creditos_text, (screen_width / 2 - creditos_text.get_width() / 2, 200))

        nome1_text = font.render('Nome: Gabriel Rezende Rangel Santana RA: 10331989', True, WHITE)
        screen.blit(nome1_text, (screen_width / 2 - nome1_text.get_width() / 2, 250))

        nome2_text = font.render('Nome: João Paulo Ladeia Santana RA: 10401026', True, WHITE)
        screen.blit(nome2_text, (screen_width / 2 - nome2_text.get_width() / 2, 300))

        nome3_text = font.render('Nome: Rafael Junqueira Pezeiro RA: 10374627', True, WHITE)
        screen.blit(nome3_text, (screen_width / 2 - nome3_text.get_width() / 2, 350))

        pygame.display.flip()

def opcoes():
    opcoes_running = True
    opcao_selecionada = 1

    while opcoes_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    opcoes_running = False
                elif event.key == pygame.K_UP:
                    opcao_selecionada -= 1
                    if opcao_selecionada < 1:
                        opcao_selecionada = 3
                elif event.key == pygame.K_DOWN:
                    opcao_selecionada += 1
                    if opcao_selecionada > 3:
                        opcao_selecionada = 1

        screen.fill(BLACK)

        opcoes_text = font.render('Opções:', True, WHITE)
        screen.blit(opcoes_text, (screen_width / 2 - opcoes_text.get_width() / 2, 200))

        opcao1_text = font.render('1 - Opção 1', True, WHITE)
        screen.blit(opcao1_text, (screen_width / 2 - opcao1_text.get_width() / 2, 300))
        opcao2_text = font.render('2 - Opção 2', True, WHITE)
        screen.blit(opcao2_text, (screen_width / 2 - opcao2_text.get_width() / 2, 350))
        opcao3_text = font.render('3 - Opção 3', True, WHITE)
        screen.blit(opcao3_text, (screen_width / 2 - opcao3_text.get_width() / 2, 400))

        if opcao_selecionada == 1:
            pygame.draw.rect(screen, WHITE, (screen_width / 2 - opcao1_text.get_width() / 2 - 10, 295,
                                              opcao1_text.get_width() + 20, opcao1_text.get_height()), 2)
        elif opcao_selecionada == 2:
            pygame.draw.rect(screen, WHITE, (screen_width / 2 - opcao2_text.get_width() / 2 - 10, 345,
                                              opcao2_text.get_width() + 20, opcao2_text.get_height()), 2)
        elif opcao_selecionada == 3:
            pygame.draw.rect(screen, WHITE, (screen_width / 2 - opcao3_text.get_width() / 2 - 10, 395,
                                              opcao3_text.get_width() + 20, opcao3_text.get_height()), 2)

        pygame.display.flip()


def main():
    menu()


if __name__ == "__main__":
    main()
    
#----------------PARTE 2-------------------------------------



while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == CLOCKTICK:
            temporizador = temporizador -1
        
    if temporizador == 0:
        break


    screen.blit(imagem, (0, 0))
    screen.blit(bus, ((screen_width/2) - 90, 8))

    player.update()
    all_sprites.update()
    
    #if len(circles) < 10:
        #create_circle()
        
    

            
    
    circles.update()
    circlelo.update()
    if pygame.sprite.spritecollide(player,circlelo, dokill=False):
        



        placar += 1
            
        killCircles()
            
            
        pygame.mixer.music.load('som/catch.mp3')
        pygame.mixer.music.play(0)

        a,b,c = valoresConta()
        create_circle(array(b))
        
    if pygame.sprite.spritecollide(player,circles, dokill=False):
        killCircles()
            
        pygame.mixer.music.load('som/catch.mp3')
        pygame.mixer.music.play(0)

        a,b,c = valoresConta()
        create_circle(array(b))
        
  
    score1 = font.render('Placar '+str(placar), True, (WHITE))
    screen.blit(score1, ((screen_width-200), 50))

    timer1 = font.render('Tempo ' + str(temporizador), True, (YELLOW))
    screen.blit(timer1, (50, 50))

    expressao = f"{a} + _ = {c}"

    AA = font.render(expressao, True, (YELLOW))
    screen.blit(AA, ((screen_width/2), 50))

    for circle1 in circles:
        #if circle1.type != 4:
            #circles.draw(screen)
        #else:
        screen.blit(circle1.image, circle1.rect)

    for circle1 in circlelo:
        #if circle1.type != 4:
            #circles.draw(screen)
        #else:
        screen.blit(circle1.image, circle1.rect)
    
    all_sprites.draw(screen)
    
    pygame.display.flip()

    clock.tick(60)


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (screen_width, screen_height)))


textofinal = font.render('Fim de Jogo - Placar final: ' + str(placar), True, (RED))
size = font.size(str(textofinal))
screen.blit(textofinal, (size[0]/2., size[1]/2.))


pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
