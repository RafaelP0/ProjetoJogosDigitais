import sys, pygame, random, pygame
from pygame.locals import *
from random import *
from pygame import mixer
import io

pygame.init()

screen_width = 1200
screen_height = 750
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Entrega Especial (Math edition)")


pacote = pygame.image.load("sprites/pacote.png")
	
pacote = pygame.transform.scale(pacote, (20, 20))

redX = pygame.image.load("img/X.png")
redX = pygame.transform.scale(redX, (180, 70))

bus = pygame.image.load("sprites/bus.png")


Pacotes=[]
Pacotes=["sprites/pacotes/pacote0.png","sprites/pacotes/pacote1.png", "sprites/pacotes/pacote2.png", "sprites/pacotes/pacote3.png","sprites/pacotes/pacote4.png", "sprites/pacotes/pacote5.png", "sprites/pacotes/pacote6.png", "sprites/pacotes/pacote7.png", "sprites/pacotes/pacote8.png", "sprites/pacotes/pacote9.png", "sprites/pacotes/pacote10.png", "sprites/pacotes/pacote11.png", "sprites/pacotes/pacote12.png", "sprites/pacotes/pacote13.png", "sprites/pacotes/pacote14.png", "sprites/pacotes/pacote15.png", "sprites/pacotes/pacote16.png", "sprites/pacotes/pacote17.png", "sprites/pacotes/pacote18.png",]

bgImg=[]
bgImg=["img/imagem_fundo1.png","img/imagem_fundo2.png","img/imagem_fundo3.png","img/imagem_fundo4.jpg"]


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

wrong=mixer.Sound("Audio/Sound/wrong.wav")
wrong.set_volume(0.5)



lvlMusic=[]
lvlMusic=["Audio/Music/SF-Tit.mp3","Audio/Music/SF-eb.mp3","Audio/Music/RR.mp3", "Audio/Music/Fanfare.mp3"]

    
BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RANKCOLOR= (229,215,27)
PURPLE=(102,0,102)
BROWN=(51,25,0)

fontG = pygame.font.SysFont('sans',60)
font = pygame.font.SysFont('sans',40)
fontP = pygame.font.SysFont('sans',35)

placar = 200
coletado = 0

nivel = 1
numColetar = 3

def defBG():
    imagem = pygame.image.load(bgImg[nivel-1])
    imagem = pygame.transform.scale(imagem, (size))
    return imagem



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

        if X_vermelho >= screen_width/2 - 150 and X_vermelho <= screen_width/2 + 150:
            while Y_vermelho >= screen_height*0.9 - 150 and Y_vermelho <= screen_height*0.9 + 150:
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

clock = pygame.time.Clock()

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 

def killCircles():
    circles.empty()
    circlelo.empty()

def expressions(h, e):
    if nivel == 1:
        return (f"{a} + {b} = {h}")
    elif nivel == 2:
        return (f"{a} + {h} = {c}")
    elif nivel == 3:
        return (f"{h} + {e} = {c}")
    
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

def writeCuts(array,i):
    aa=i
    z=array[aa]
    aa+=1
    x=array[aa]
    aa+=1
    c=array[aa]
    texto1 = font.render(z, True, (WHITE))
    screen.blit(texto1, (30, (screen_height - 180)))
    texto2 = font.render(x, True, (WHITE))
    screen.blit(texto2, (30, (screen_height - 130)))
    texto3 = font.render(c, True, (WHITE))
    screen.blit(texto3, (30, (screen_height - 80)))


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
    file1 = io.open(files[nivel-1],'r', encoding="utf8")
    file1.seek(0)
    arr=[None]*100
    i=0
    tamanho=[]
    tamanho=[16,9,12,27]
    for valorr in file1:
        arr[i] = valorr
        arr[i]=arr[i][:-1]

        i+=1
    imagem = defBG()
    mixer.music.load("Audio/Music/SF-Title.mp3")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
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
            music()


            break;

nave1 = pygame.image.load(naves[0])
nave1 = pygame.transform.scale(nave1, ((screen_width//3),(screen_height//3)))
nave2 = pygame.image.load(naves[1])
nave2 = pygame.transform.scale(nave2, (((screen_width//3)),(screen_height//3)))
nave3 = pygame.image.load(naves[2])
nave3 = pygame.transform.scale(nave3, (((screen_width//3)),(screen_height//3)))
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
        
        imagem = pygame.image.load('img/hangar.png')
        imagem = pygame.transform.scale(imagem, (size))
        screen.blit(imagem, (0, 0))

        legenda = font.render('ESCOLHA SUA NAVE:', True, WHITE)
        screen.blit(legenda, (screen_width / 2 - legenda.get_width() / 2, 200))
        option1_text = font.render('1 - ', True, WHITE)

        screen.blit(option1_text, (50, 300))
        screen.blit(nave1, ((option1_text.get_width()/2) - 50, 300))

        option2_text = font.render('2 - ', True, WHITE)
        screen.blit(option2_text, (nave1.get_width()+ option1_text.get_width()/2, 300))
        screen.blit(nave2, ((nave1.get_width()+ option1_text.get_width()/2 + option2_text.get_width()/2) - 50, 300))


        option3_text = font.render('3 - ', True, WHITE)
        screen.blit(option3_text, ((nave2.get_width() + nave1.get_width()+ option1_text.get_width()/2 + option2_text.get_width()/2), 300))
        screen.blit(nave3, ((nave2.get_width() + nave1.get_width()+ option1_text.get_width()/2 + option2_text.get_width()/2 + option2_text.get_width()/2) - 50, 300))

        pygame.display.flip()

def music():
    msk=lvlMusic[nivel-1]
    mixer.music.load(msk)
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    
def chooseLvl():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3

        bg1 = pygame.image.load(bgImg[0])
        bg1 = pygame.transform.scale(bg1, (size))
        bg2 = pygame.image.load(bgImg[1])
        bg2 = pygame.transform.scale(bg2, (size))
        bg3 = pygame.image.load(bgImg[2])
        bg3 = pygame.transform.scale(bg3, (size))
        screen.blit(bg1, (0, 0))
        screen.blit(bg2, (screen_width//3, 0))
        screen.blit(bg3, ((screen_width//3)*2, 0))

        legenda = font.render('SELCIONE O NIVEL:', True, WHITE)
        
        screen.blit(legenda, (screen_width / 2 - legenda.get_width() / 2, 50))
        
        option1_text = font.render('1 ', True, WHITE)
        screen.blit(option1_text, (screen_width//6, 300))
        expressao1 = fontG.render('7 + 3 = _', True, WHITE)
        screen.blit(expressao1, ((screen_width//6 - expressao1.get_width()/2, 450)))

        option2_text = font.render('2 ', True, WHITE)
        screen.blit(option2_text, (screen_width//2, 300))
        expressao2 = fontG.render('7 + _ = 10', True, WHITE)
        screen.blit(expressao2, ((screen_width//2 - expressao2.get_width()/2, 450)))


        option3_text = font.render('3 ', True, WHITE)
        screen.blit(option3_text, ((screen_width//6)*5, 300))
        expressao3 = fontG.render('_ + _ = 10', True, WHITE)
        screen.blit(expressao3, (((screen_width//6)*5 - expressao3.get_width()/2, 450)))

        pygame.display.flip()
        
def rankdps():
    one = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            file1 = open('rankings/ranking.txt','r+')
            file1.seek(0)
            arr=[0]*11
            i=0
            for valorr in file1:
                arr[i] = valorr
                i+=1
                        
            imagem = pygame.image.load('img/rankBg.jpg')
            imagem = pygame.transform.scale(imagem, (size))
            screen.blit(imagem, (0, 0))

            rank_p = fontG.render('sua pontuação: %d' %placar, True, WHITE)
            screen.blit(rank_p, (screen_width / 2 - rank_p.get_width() / 2, screen_height*0.3 - 100))
            pygame.draw.rect(screen, (0, 0, 0), (0, (screen_height - 200), screen_width, screen_height*0.3))


            
            rank_1 = font.render('1 - %s' %arr[0], True, WHITE)
            screen.blit(rank_1, (rank_1.get_width() / 2, screen_height - 200 + 20))

            rank_2 = font.render('2 - %s' %arr[1], True, WHITE)
            screen.blit(rank_2, (rank_1.get_width() + rank_2.get_width() / 2, screen_height - 200 + 70))

            rank_3 = font.render('3 - %s' %arr[2], True, WHITE)
            screen.blit(rank_3, (rank_1.get_width() + rank_2.get_width() + rank_3.get_width() / 2, screen_height - 200  +130))

            
            
            
    
            pygame.display.flip()

            if one == 1:
                file1.seek(0)
                arr2=[0]*11
                i=0
                for valorr in file1:
                    arr2[i] = int(valorr)
                    i+=1
                arr2[i]=int(placar)
                aa=len(arr2)
                arr2 = sorted(arr2, reverse=True)
                arr2.pop(aa-1)
                file1.seek(0)
                i=0
                while i<=9:
                    bb=str("%s \n" %arr2[i])
                    
                    file1.write(bb)
                    i+=1
                one -=1

def menu():
    running = True
    mixer.music.load("Audio/Music/SF-Corn.mp3")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game()
                elif event.key == pygame.K_2:
                    creditos()
                elif event.key == pygame.K_3:
                    opcoes()
                elif event.key == pygame.K_4:
                    rank()
                elif event.key == pygame.K_5:
                    pygame.quit()
                    sys.exit()
        
        imagem = pygame.image.load('img/title.png')
        imagem = pygame.transform.scale(imagem, (size))
        screen.blit(imagem, (0, 0))

        option1_text = font.render('1 - Iniciar Jogo', True, BLACK)
        pygame.draw.rect(screen, (WHITE), (screen_width / 2 - option1_text.get_width() / 2 - 5, 345, option1_text.get_width() +15, option1_text.get_height() + 15))
        screen.blit(option1_text, (screen_width / 2 - option1_text.get_width() / 2, 350))

        option2_text = font.render('2 - Créditos', True, BLACK)

        pygame.draw.rect(screen, (WHITE), (screen_width / 2 - option2_text.get_width() / 2 - 5, 415, option2_text.get_width() +15, option2_text.get_height() + 15))
        screen.blit(option2_text, (screen_width / 2 - option2_text.get_width() / 2, 420))

        option3_text = font.render('3 - Opções', True, BLACK)
        pygame.draw.rect(screen, (WHITE), (screen_width / 2 - option3_text.get_width() / 2 - 5, 485, option3_text.get_width() +15, option3_text.get_height() + 15))

        screen.blit(option3_text, (screen_width / 2 - option3_text.get_width() / 2, 490))

        option4_text = font.render('4 - Ranking', True, BLACK)
        pygame.draw.rect(screen, (WHITE), (screen_width / 2 - option4_text.get_width() / 2 - 5, 555, option4_text.get_width() +15, option4_text.get_height() + 15))

        screen.blit(option4_text, (screen_width / 2 - option4_text.get_width() / 2, 560))

        option5_text = font.render('5 - Sair', True, BLACK)
        pygame.draw.rect(screen, (WHITE), (screen_width / 2 - option5_text.get_width() / 2 - 5, 625, option5_text.get_width() +15, option5_text.get_height() + 15))

        screen.blit(option5_text, (screen_width / 2 - option5_text.get_width() / 2, 630))
        
        pygame.display.flip()

def rank():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            file1 = open('rankings/ranking.txt','r+')
            file1.seek(0)
            arr=[0]*11
            i=0
            for valorr in file1:
                arr[i] = valorr
                arr[i]=arr[i][:-1]
                i+=1

            imagem = pygame.image.load('img/rankBg.jpg')
            imagem = pygame.transform.scale(imagem, (size))
            screen.blit(imagem, (0, 0))
            rank_1 = fontG.render('1 - %s' %arr[0], True, RANKCOLOR)
            screen.blit(rank_1, (screen_width//2-rank_1.get_width(), 200))
            pygame.draw.rect(screen, (BLUE), (0, (200 + rank_1.get_height()),rank_1.get_width() / 2+ screen_width//2-80,15))
            pygame.draw.rect(screen, (0, 0, 0), (0, (200 + rank_1.get_height()),rank_1.get_width() / 2+ screen_width//2-50,10))

            rank_2 = fontG.render('2 - %s' %arr[1], True, RANKCOLOR)
            screen.blit(rank_2, ( screen_width//2- rank_2.get_width() -20, 300))
            
            pygame.draw.rect(screen, (BLUE), (0, (300 + rank_2.get_height()),rank_2.get_width() / 2 + screen_width//2-130,15))
            pygame.draw.rect(screen, (0, 0, 0), (0, (300 + rank_2.get_height()),rank_2.get_width() / 2 + screen_width//2-100,10))

            rank_3 = fontG.render('3 - %s' %arr[2], True, RANKCOLOR)
            screen.blit(rank_3, (screen_width//2- rank_3.get_width() -40, 400))
            pygame.draw.rect(screen, (BLUE), (0, (400 + rank_3.get_height()),rank_3.get_width() / 2 + screen_width//2-180,15))
            pygame.draw.rect(screen, (0, 0, 0), (0, (400 + rank_3.get_height()),rank_3.get_width() / 2 + screen_width//2-150,10))



        

            rank_4 = fontP.render('4 - %s' %arr[3], True, RANKCOLOR)
            screen.blit(rank_4, ((screen_width - rank_4.get_width() )-10, 100))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_4.get_width()/2 )+130, (100 + rank_4.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_4.get_width()/2 )+90, (100 + rank_4.get_height()), screen_width//2-200,10))

            rank_5 = fontP.render('5 - %s' %arr[4], True, RANKCOLOR)
            screen.blit(rank_5, ((screen_width- rank_5.get_width() )-10, 175))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_5.get_width()/2 )+150, (175 + rank_5.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_5.get_width()/2 )+110, (175 + rank_5.get_height()), screen_width//2-200,10))
            
            rank_6 = fontP.render('6 - %s' %arr[5], True, RANKCOLOR)
            screen.blit(rank_6, ((screen_width- rank_6.get_width() )-10, 250))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_6.get_width()/2 )+170, (250 + rank_6.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_6.get_width()/2 )+130, (250 + rank_6.get_height()), screen_width//2-200,10))

            rank_7 = fontP.render('7 - %s' %arr[6], True, RANKCOLOR)
            screen.blit(rank_7, ((screen_width - rank_7.get_width() )-10, 325))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_7.get_width()/2 )+190, (325 + rank_7.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_7.get_width()/2 )+150, (325 + rank_7.get_height()), screen_width//2-200,10))
            
            rank_8 = fontP.render('8 - %s' %arr[7], True, RANKCOLOR)
            screen.blit(rank_8, ((screen_width - rank_8.get_width() )-10, 400))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_8.get_width()/2 )+210, (400 + rank_8.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_8.get_width()/2 )+170, (400 + rank_8.get_height()), screen_width//2-200,10))
            
            rank_9 = fontP.render('9 - %s' %arr[8], True, RANKCOLOR)
            screen.blit(rank_9, ((screen_width - rank_9.get_width() )-10, 475))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_9.get_width()/2 )+230, (475 + rank_9.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_9.get_width()/2 )+190, (475 + rank_9.get_height()), screen_width//2-200,10))
            
            rank_10 = fontP.render('10 - %s' %arr[9], True, RANKCOLOR)
            screen.blit(rank_10, ((screen_width - rank_10.get_width() )-10, 550))
            pygame.draw.rect(screen, (BROWN), ((screen_width / (4/3)- rank_10.get_width()/2 )+250, (550 + rank_10.get_height()), screen_width//2-200,15))
            pygame.draw.rect(screen, (0, 0, 0), ((screen_width / (4/3)- rank_10.get_width()/2 )+210, (550 + rank_10.get_height()), screen_width//2-200,10))
            
            pygame.display.flip()

def creditos():
    running = True
    mixer.music.load("Audio/Music/OoT-ToT.mp3")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill(BLACK)
        imagem = pygame.image.load('img/mack1.jpg')
        imagem = pygame.transform.scale(imagem, (size))
        screen.blit(imagem, (0, 0))
        imagem2 = pygame.image.load('img/mack3.png')
        imagem2 = pygame.transform.scale(imagem2, (500, 150))
        
        
        screen.blit(imagem2, ((screen_width/2 - imagem2.get_width()/2),10))

        creditos_text = font.render('Créditos:', True, BLACK)
        screen.blit(creditos_text, (screen_width / 2 - creditos_text.get_width() / 2, 200))

        nome1_text = font.render('Nome: Gabriel Rezende Rangel Santana RA: 10331989', True, BLACK)
        screen.blit(nome1_text, (screen_width / 2 - nome1_text.get_width() / 2, 250))

        nome2_text = font.render('Nome: João Paulo Ladeia Santana RA: 10401026', True, BLACK)
        screen.blit(nome2_text, (screen_width / 2 - nome2_text.get_width() / 2, 300))

        nome3_text = font.render('Nome: Rafael Junqueira Pezeiro RA: 10374627', True, BLACK)
        screen.blit(nome3_text, (screen_width / 2 - nome3_text.get_width() / 2, 350))

        pygame.display.flip()

def opcoes():
    
    def ajustar_volume(volume):
       
        pygame.mixer.music.set_volume(volume / 100)  
    
    opcoes_running = True
    opcao_selecionada = 1
    show_volume_slider = False  
    volume_slider_width = 200 
    volume_slider_height = 10  
    volume_slider_x = screen_width / 2 - volume_slider_width / 2 
    volume_slider_y = 450  
    volume_slider_pos = 0
    volume = 50 

    
    volume_slider_rect = pygame.Rect(volume_slider_x, volume_slider_y, volume_slider_width, volume_slider_height)

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
                elif event.key == pygame.K_RETURN:  
                    if opcao_selecionada == 1:  
                        show_volume_slider = not show_volume_slider
                        

            elif event.type == pygame.MOUSEMOTION:
                
                if volume_slider_rect.collidepoint(event.pos) and show_volume_slider:
                    volume_slider_pos = event.pos[0] - volume_slider_rect.left
                    volume = int((volume_slider_pos / volume_slider_width) * 100)
                    ajustar_volume(volume)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and volume_slider_rect.collidepoint(event.pos):
                    volume_slider_pos = event.pos[0] - volume_slider_rect.left
                    volume = int((volume_slider_pos / volume_slider_width) * 100)
                    ajustar_volume(volume)

        screen.fill(BLACK)
        imagem = pygame.image.load('img/optBg.jpg')
        imagem = pygame.transform.scale(imagem, (size))
        screen.blit(imagem, (0, 0))

        opcoes_text = font.render('Configurações:', True, WHITE)
        screen.blit(opcoes_text, (screen_width / 2 - opcoes_text.get_width() / 2, 200))

        opcao1_text = font.render('1 - Som', True, WHITE)
        screen.blit(opcao1_text, (screen_width / 2 - opcao1_text.get_width() / 2, 300))
       

        if opcao_selecionada == 1:
            pygame.draw.rect(screen, WHITE, (screen_width / 2 - opcao1_text.get_width() / 2 - 10, 295,
                                              opcao1_text.get_width() + 20, opcao1_text.get_height()), 2)
            if show_volume_slider:  
                pygame.draw.rect(screen, WHITE, volume_slider_rect)
                pygame.draw.circle(screen, WHITE, (volume_slider_rect.left + volume_slider_pos, volume_slider_rect.centery), 10)
                volume_text = font.render('Volume: {}'.format(volume), True, WHITE)
                screen.blit(volume_text, (volume_slider_rect.right + 20, volume_slider_rect.top))

        pygame.display.flip() 
    



        
    
def game():
    global nivel
    nivel = chooseLvl()
    global placar
    placar = 200
    global coletado
    coletado = 0
    
    numColetar = 2
    ship=naves[choose()]
    temporizador = 12

    global nave
    nave = pygame.image.load(ship)
    nave = pygame.transform.scale(nave, (80, 80))
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    

    global a,b,c
    a,b,c = valoresConta()
    praCriar() 
    global expressao
    expressao = expressions("_","_")

    cutscene = True
    game_running=True
    while game_running:
        

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
            temporizador += 7
            placar += 10
            coletado +=1
            

            if nivel !=3:
                if coletado == numColetar:   
                    nivel +=1
                    
                    coletado = 0
                    cutscene = True


                all_sprites.empty()
                killCircles()
                player = Player()
                all_sprites.add(player)
                
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
                    

                elif coletado % 2 ==0:
                    killCircles()
                    all_sprites.empty()
                    player = Player()
                    all_sprites.add(player)
                    
                    a,b,c = valoresConta()
                    praCriar()

            
                
            

        elif pygame.sprite.spritecollide(player,circles, dokill=False):
            if nivel ==3:
                if coletado % 2 ==1:
                    coletado -=1
            all_sprites.empty()
            killCircles()   
            player = Player()
            all_sprites.add(player)
                    
                    
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
            
        #timer1 = font.render('Tempo ' + str(temporizador), True, (YELLOW))
        #screen.blit(timer1, (50, 50))

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
    rankdps()
menu()



frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (screen_width, screen_height)))


textofinal = font.render('Obrigado por Jogar! :D ' + str(placar), True, (RED))
size = font.size(str(textofinal))
screen.blit(textofinal, (size[0]/2., size[1]/2.))


pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
