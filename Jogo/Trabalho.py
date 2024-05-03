import sys, pygame, random, pygame
from pygame.locals import *
from random import *
from pygame import mixer
pygame.init()

screen_width = 1200
screen_height = 750
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Matematica espacial")

#imagem = pygame.image.load("img/imagem_fundo.png")
#imagem = pygame.transform.scale(imagem, (size))

pacote = pygame.image.load("sprites/pacote.png")
	
pacote = pygame.transform.scale(pacote, (20, 20))

redX = pygame.image.load("img/X.png")
redX = pygame.transform.scale(redX, (180, 70))

bus = pygame.image.load("sprites/bus.png")
#bus = pygame.transform.scale(bus, (550, 170))

Pacotes=[]
Pacotes=["sprites/pacotes/pacote0.png","sprites/pacotes/pacote1.png", "sprites/pacotes/pacote2.png", "sprites/pacotes/pacote3.png","sprites/pacotes/pacote4.png", "sprites/pacotes/pacote5.png", "sprites/pacotes/pacote6.png", "sprites/pacotes/pacote7.png", "sprites/pacotes/pacote8.png", "sprites/pacotes/pacote9.png", "sprites/pacotes/pacote10.png", "sprites/pacotes/pacote11.png", "sprites/pacotes/pacote12.png", "sprites/pacotes/pacote13.png", "sprites/pacotes/pacote14.png", "sprites/pacotes/pacote15.png", "sprites/pacotes/pacote16.png", "sprites/pacotes/pacote17.png", "sprites/pacotes/pacote18.png",]

bgImg=[]
bgImg=["img/imagem_fundo1.jpg","img/imagem_fundo2.jpg","img/imagem_fundo3.jpg"]


naves=[]
naves=["sprites/naves/nave1.png", "sprites/naves/nave2.png", "sprites/naves/nave3.png"]

playerRight=pygame.image.load("sprites/npc/playerR.png")
playerRight = pygame.transform.scale(playerRight, (300, 700))
playerLeft=pygame.image.load("sprites/npc/playerL.png")
playerLeft = pygame.transform.scale(playerLeft, (300, 700))

bossRight=pygame.image.load("sprites/npc/bossR.png")
bossRight = pygame.transform.scale(bossRight, (400, 300))
bossLeft=pygame.image.load("sprites/npc/bossL.png")
bossLeft = pygame.transform.scale(bossLeft, (400, 300))

correct=mixer.Sound("Audio/Sound/correct.wav")
#correct.set_volume(0.2)

wrong=mixer.Sound("Audio/Sound/wrong.wav")
wrong.set_volume(0.5)

# background music
mixer.music.load("Audio/Music/Wii.mp3")
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont('sans',40)
placar = 200
#men = 0
coletado = 0

#for testing
#Nivel que começa
nivel = 1
#Numero de caixa a coletar
numColetar = 2

def defBG():
    imagem = pygame.image.load(bgImg[nivel-1])
    imagem = pygame.transform.scale(imagem, (size))
    return imagem

def expressions(h, e):
    if nivel == 1:
        return (f"{a} + {b} = {h}")
    elif nivel == 2:
        return (f"{a} + {h} = {c}")
    elif nivel == 3:
        return (f"{h} + {e} = {c}")

def praCriar():
    if nivel == 1:
        return create_circle(array(c))
    elif nivel == 2:
        return create_circle(array(b))
    elif nivel == 3:
        return create_circle(arrays(a,b))
    

def valoresConta():
    a = randint(0, 18)
    c = randint(0, 18)
    while a > c:
        c = randint(0, 18)
    b = c - a
    return [a,b,c]

def array(num):
    array_de_valores =[]
    array_de_valores.append(num)
    
    n=0
    while n <9:
        m = randint(0, 18)
        while m in array_de_valores:
            m = randint(0, 18)
            
        while m == num:
            m = randint(0, 18)
        array_de_valores.append(m)
        n+=1

    return array_de_valores

def arrays(num1,num2):
    array_de_valores =[]
    array_de_valores.append(num1)
    array_de_valores.append(num2)
    n=0
    while n <5:
        m = randint(0, 18)
        while m in array_de_valores:
            m = randint(0, 18)
            
        while (m == num1) or (m ==num2):
            m = randint(0, 18)

        for teste in array_de_valores:
            if m + teste == c:
                m = randint(0, 18)
        array_de_valores.append(m)
        n+=1

    return array_de_valores


    
    
class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, raio, AA):
        super().__init__()
        self.valor = AA
        a=[]
        a=pygame.image.load(Pacotes[AA]).convert_alpha()
        a= pygame.transform.scale(a, (40, 40))
        self.image = a
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [choice([-1, 1]), choice([-1, 1])]
        
        

    def update(self):
        self.rect.move_ip(self.velocity)
        
        if self.rect.left < 0 or self.rect.right > screen_width:
                self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
                self.velocity[1] *= -1

            


def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = nave
        self.image = nave
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height*0.9))


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                self.image = rotate_image(self.img, 45)
                self.rect.move_ip(-5, -5)
                
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                self.image = rotate_image(self.img, 135)
                self.rect.move_ip(-5, 5)

        

        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                self.image = rotate_image(self.img, -45)
                self.rect.move_ip(5, -5)
                
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                self.image = rotate_image(self.img, -135)
                self.rect.move_ip(5, 5)
                
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.image = rotate_image(self.img, 90)

        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.image = rotate_image(self.img, -90)
            
        elif keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
            self.image = self.img
            
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
            self.image = rotate_image(self.img, 180)

        self.rect.clamp_ip(screen.get_rect())
        


def create_circle(values):
    for i in range(len(values)):
        X_vermelho = randint(40, (screen_width - 50))
        
        Y_vermelho = randint(40, (screen_height - 50))

        if X_vermelho >= screen_width/2 - 100 and X_vermelho <= screen_width/2 + 100:
            while Y_vermelho >= screen_height*0.9/2 - 100 and Y_vermelho <= screen_height*0.9/2 + 100:
                Y_vermelho = randint(40, (screen_height - 50))
                
        raio = 20
        circle = Circle(X_vermelho, Y_vermelho, raio, values[i] )
        if nivel == 1:
            if values[i] == c:
                circlelo.add(circle)
            else:
                circles.add(circle)  
            
        elif nivel == 2:
            if values[i] == b:
                circlelo.add(circle)
            else:
                circles.add(circle) 
            
        elif nivel == 3:
            if values[i] == a:
                circlelo.add(circle)
            if values[i] == b:
                circlelo.add(circle)
            else:
                circles.add(circle)  


circles = pygame.sprite.Group()  
circlelo = pygame.sprite.Group()  
a,b,c = valoresConta()
praCriar()       




clock = pygame.time.Clock()

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 
temporizador = 12

def killCircles():
    circles.empty()
    circlelo.empty()


def mostra():
    tempp=1
    if nivel == 1:
        expressao = expressions(c, "_")
    elif nivel == 2:
        expressao = expressions(b, "_")
    elif nivel == 3:
        for c1 in circlelo:
            if c1.valor == a:
                expressao = expressions("_", b)
            elif c1.valor == b:
                expressao = expressions(a, "_")
        if coletado % 2 ==0:
            expressao = expressions(a, b)
                
    Formula = font.render(expressao, True, (GREEN))
    screen.blit(Formula, ((screen_width/2)- 120, 50))
    pygame.display.flip()
    while tempp >=0:
        for event in pygame.event.get():
            if event.type == CLOCKTICK:
                tempp-=1

def mostraWrong():
    tempp=1

                
    Formula = font.render(expressao, True, (BLACK))
    screen.blit(Formula, ((screen_width/2)- 120, 50))
    screen.blit(redX, ((screen_width/2) - 130, 40))
    pygame.display.flip()
    while tempp >=0:
        for event in pygame.event.get():
            if event.type == CLOCKTICK:
                tempp-=1

imagem = defBG()
def writeCuts(array,i):
    aa=i
    z=array[aa]
    aa+=1
    x=array[aa]
    aa+=1
    c=array[aa]
    texto1 = font.render(z, True, (WHITE))
    screen.blit(texto1, (50, (screen_height - 150)))
    texto2 = font.render(x, True, (WHITE))
    screen.blit(texto2, (50, (screen_height - 100)))
    texto3 = font.render(c, True, (WHITE))
    screen.blit(texto3, (50, (screen_height - 50)))


def loadChars():
    if nivel == 1:
        screen.blit(bossLeft, (50, screen_height*0.5))
        screen.blit(playerRight, ((screen_width-500), (screen_height*0.2)))
    else:
        screen.blit(playerLeft, (50, screen_height*0.2))
        screen.blit(bossRight, ((screen_width-500), (screen_height*0.5)))
        
def cuts():
    files=[]
    files=['Cutscene/cutscene1.txt','Cutscene/cutscene2.txt','Cutscene/cutscene3.txt','Cutscene/cutscene4.txt' ]
    file1 = open(files[nivel-1],'r')
    file1.seek(0)
    arr=[None]*100
    i=0
    tamanho=[]
    tamanho=[16,6,12,23]
    for valorr in file1:
        arr[i] = valorr
        i+=1
    
    j=0
    while j <=tamanho[nivel-1]:
        screen.blit(imagem, (0, 0))
        loadChars()
        pygame.draw.rect(screen, (0, 0, 0), (0, (screen_height - 200), screen_width, screen_height*0.3))
        writeCuts(arr,j)
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                j+=3
        pygame.display.flip()
        if j >= tamanho[nivel-1]:
            break;
        
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
nave1 = pygame.image.load(naves[0])
nave1 = pygame.transform.scale(nave1, (((screen_width/3)),(screen_height/3)))
nave2 = pygame.image.load(naves[1])
nave2 = pygame.transform.scale(nave2, (((screen_width/3)),(screen_height/3)))
nave3 = pygame.image.load(naves[2])
nave3 = pygame.transform.scale(nave3, (((screen_width/3)),(screen_height/3)))
def choose():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 0
                elif event.key == pygame.K_2:
                    return 1
                elif event.key == pygame.K_3:
                    return 2
        
        screen.blit(imagem, (0, 0))

        legenda = font.render('ESCOLHA SUA NAVE:', True, WHITE)
        screen.blit(legenda, (screen_width / 2 - legenda.get_width() / 2, 200))

        option1_text = font.render('1 - ', True, WHITE)
        #screen.blit(option1_text, (screen_width / 2 - option1_text.get_width() / 2, 300))
        #screen.blit(nave1, ((screen_width / 2 - option1_text.get_width()/2 + 50), 300))
        screen.blit(option1_text, (50, 300))
        screen.blit(nave1, ((option1_text.get_width()/2) - 50, 300))

        option2_text = font.render('2 - ', True, WHITE)
        #screen.blit(option2_text, (screen_width / 2 - option2_text.get_width() / 2, 350))
        #screen.blit(nave2, ((screen_width/2 - option2_text.get_width()/2 ) + 50, 350))
        screen.blit(option2_text, (nave1.get_width()+ option1_text.get_width()/2, 300))
        screen.blit(nave2, ((nave1.get_width()+ option1_text.get_width()/2 + option2_text.get_width()/2) - 50, 300))


        option3_text = font.render('3 - ', True, WHITE)
        #screen.blit(option3_text, (screen_width / 2 - option3_text.get_width() / 2, 400))
        #screen.blit(nave3, ((screen_width/2- option3_text.get_width() / 2 ) + 00, 400))
        screen.blit(option3_text, ((nave2.get_width() + nave1.get_width()+ option1_text.get_width()/2 + option2_text.get_width()/2), 300))
        screen.blit(nave3, ((nave2.get_width() + nave1.get_width()+ option1_text.get_width()/2 + option2_text.get_width()/2 + option2_text.get_width()/2) - 50, 300))

        pygame.display.flip()

ship=naves[choose()]
nave = pygame.image.load(ship)
nave = pygame.transform.scale(nave, (80, 80))
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
expressao = expressions("_","_")

cutscene = True
while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == CLOCKTICK:
            if temporizador != 0:
                temporizador = temporizador -1
            else:
                if placar > 0:
                    placar -=5
        
        
    imagem = defBG()

    screen.blit(imagem, (0, 0))
    
    if cutscene == True:
        cuts()
        cutscene = False
    screen.blit(bus, ((screen_width/2) - 150, 8))
    

    all_sprites.update()
        
    

    circles.update()
    circlelo.update()
    

    if pygame.sprite.spritecollide(player,circlelo, dokill=True):
        temporizador += 5
        placar += 10
        coletado +=1
        

        if nivel !=3:
            if coletado == numColetar:   
                nivel +=1
                coletado = 0
                cutscene = True
            killCircles()
            correct.play()
            mostra()
            a,b,c = valoresConta()
            praCriar()
        else:
            correct.play()
            mostra()
            if coletado == (numColetar*2):   
                nivel +=1
                coletado = 0
                cutscene = True

            if coletado % 2 ==0:
                killCircles()
                
                a,b,c = valoresConta()
                praCriar()

        
            
        

    elif pygame.sprite.spritecollide(player,circles, dokill=False):
        if nivel ==3:
            if coletado % 2 ==1:
                coletado -=1
                
        killCircles()           
        wrong.play()
        mostraWrong()

        a,b,c = valoresConta()
        praCriar()

    if nivel == 4:
        break
    
        
  
    score1 = font.render('Placar '+str(placar), True, (WHITE))
    screen.blit(score1, ((screen_width-200), 50))
    
    lvlDisplay = font.render('Nivel '+str(nivel), True, (WHITE))
    screen.blit(lvlDisplay, ((screen_width-198), 100))
        
    timer1 = font.render('Tempo ' + str(temporizador), True, (YELLOW))
    screen.blit(timer1, (50, 50))

    expressao = expressions("_","_")
    
    Formula = font.render(expressao, True, (BLACK))
    screen.blit(Formula, ((screen_width/2)- 120, 50))

    for circle1 in circles:
        screen.blit(circle1.image, circle1.rect)

    for circle1 in circlelo:
        screen.blit(circle1.image, circle1.rect)
    
    all_sprites.draw(screen)
    
    pygame.display.flip()

    clock.tick(60)

if cutscene == True:
        cuts()
        cutscene = False

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
