from operator import truediv
from matplotlib import image
import pygame
import random
import math

pygame.init() #Initialize the game

screen = pygame.display.set_mode((800,600))  # Creates the Screen

running = True

# The name and ICON
pygame.display.set_caption("Space Rangers")
# icon = pygame.image.load("logo.jpeg")
background = pygame.image.load("Resources/back.jpg")



#Player image
playerImg = pygame.image.load("Resources/spaceship.png")
playerX = 370
playerXdiff = 0
playerY = 480
playerYdiff = 0

bulletImg = pygame.image.load("Resources/bullet.png")
bulletX = 0
bulletXdiff = 0
bulletY = 480
bulletYdiff = 10
bulletState = "ready"

enmImg = []
enmX = []
enmY = []
enmXdiff = []
enmYdiff = []
numenm = 6
enmImg.append(pygame.image.load("Resources/enm1.png"))
enmImg.append(pygame.image.load("Resources/enm2.png"))
enmImg.append(pygame.image.load("Resources/enm1.png"))
enmImg.append(pygame.image.load("Resources/enm2.png"))
enmImg.append(pygame.image.load("Resources/enm1.png"))
enmImg.append(pygame.image.load("Resources/enm2.png"))

for i in range (numenm):
    
    enmX.append(random.randint(10 , 730))
    enmXdiff.append(0.5)
    enmY.append(random.randint(50 , 150))
    enmYdiff.append(40)

# enm2Img = pygame.image.load("Resources/enm2.png")
# enm2X =random.randint(10 , 730)
# enm2Xdiff = 0
# enm2Y =random.randint(50 , 150)
# enm2Ydiff = 0

def player(x , y):
    screen.blit(playerImg , (x, y) )

def enemy(x , y , i):
    screen.blit(enmImg[i], (x, y) )

score_val = 0
font = pygame.font.Font('freesansbold.ttf' , 32)
textX =10
textY =10
def score_show(x , y):
    score = font.render("Score : "+str(score_val ) , True , (255 ,255 ,255))
    screen.blit(score , (x, y))


overfont = pygame.font.Font('freesansbold.ttf' , 64)

def gameovertext():
    score = overfont.render(" Game Over " , True , (255 ,0 ,0))
    screen.blit(score , (200, 250))


# def enm2(x , y):
#     screen.blit(enm2Img , (x, y) )

def bullet(x , y):
    global bulletState 
    bulletState = "fire"
    screen.blit(bulletImg , (x, y+10) )

def isCollision(enmX , enmY ,bulletX , bulletY):
    dis = math.sqrt((math.pow(enmX - bulletX , 2)  ) + (math.pow(enmY - bulletY , 2)  )  )
    if dis <30:
        return True
    else:
        return False


# The Entire Game loop
while running:
    screen.fill((0 , 0 , 0))
    screen.blit(background , (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        dir =0

        if event.type == pygame.KEYDOWN:  # If that key is pressed
            if event.key == pygame.K_LEFT:
                playerXdiff = -3
                dir = -1
            if event.key == pygame.K_RIGHT:
                playerXdiff = 3
                dir = 1
            #  if event.key == pygame.K_RIGHT && event.key == pygame.K_LEFT:
            #     if (dir==1)
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                bullet(bulletX , bulletY)
        if event.type == pygame.KEYUP:  # If that key is relased
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXdiff = 0

    playerX = playerX +playerXdiff 

    if playerX < 10:
        playerX = 10
    if playerX > 730:
        playerX = 730 

    for i in range(numenm ):

        # Game Over
        if enmY[i] >= 440:
            for j in range(numenm):
                enmY[j] = 2000
            gameovertext()
            break


        enmX[i] = enmX[i] +enmXdiff[i] 
        if enmX[i] < 10:
            enmXdiff[i] = 1
            enmY[i] = enmY[i] + enmYdiff[i]
        if enmX[i] > 750:
            enmXdiff[i] = -1
            enmY[i] = enmY[i] + enmYdiff[i]
        
        collision = isCollision(enmX[i] , enmY[i] , bulletX , bulletY)
        if collision:
            bulletY=480
            bulletState="ready"
            score_val = score_val +1
            #print(score_val)
            enmX[i] = random.randint(20,710)
            enmY[i] = random.randint(50, 150)
        enemy(enmX[i] , enmY[i] , i)


        
    
   
    
    
    if bulletY <=0:
        bulletY = 480
        bulletState = "ready"
    
    if bulletState == "fire":
        bullet(bulletX , bulletY)
        bulletY = bulletY - bulletYdiff


    player(playerX  , playerY)
    score_show(textX , textY)
   
    
    pygame.display.update()
