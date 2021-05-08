import random # for generating random no.
import sys #we will use sys.exit to exit the program or game
import pygame
from pygame.locals import * # basic pygame import


#Global variables for the game
FPS = 32
SCREENWIDTH = 285
SCREENHEIGHT = 500
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'flappy bird/sprites/bird.png'
BACKGROUND = 'flappy bird/sprites/background.png'
PIPE = 'flappy bird/sprites/pipe.png'

def WelcomeScreen():
    '''
    shows welcome image on the screen
    '''
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENHEIGHT - GAME_SPRITES['message'].get_height())/5)
    messagey = int(SCREENHEIGHT* 0.13)
    basex = 0
    while True:
        for event in pygame.event.get():#controls events which we press from mouse and keyboard
            #if user clicks on cross button close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #if the user press space or up key, start the game them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit((GAME_SPRITES)['background'],(0,0))
                SCREEN.blit((GAME_SPRITES)['player'],(playerx,playery))
                SCREEN.blit((GAME_SPRITES)['message'],(messagex,messagey))
                SCREEN.blit((GAME_SPRITES)['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    #create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

   #my list of upper pipes
    upperPipes = [{'x': SCREENWIDTH+200,'y':newPipe1[0]['y']},
                  {'x': SCREENWIDTH+200+(SCREENWIDTH/2),'y':newPipe2[0]['y']}]

    #my list of lower pipes
    lowerPipes = [{'x': SCREENWIDTH+200,'y':newPipe1[1]['y']},
                  {'x': SCREENWIDTH+200+(SCREENWIDTH/2),'y':newPipe2[1]['y']}]


    pipeVelX = -4 #to move pipe in reverse direction 

    playerVelY = -9 #to put player down in -9 velocity
    playerMaxVelY = -10 # not to fly bird more than the -10 velocity
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 #velocity while flapping
    playerFlapped = False #it is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()
                    
                    
    crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)#this function will return true if the player is crashed
    if crashTest:
        return

        #check for score
        playerMidPos = playerx = GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x']+ GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipMidPos +4:
                score+=1
                print(f'Your score is {score}')
                GAME_SOUNDS['piont'].play()


        if playerVelY <playermaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)


       #move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x']+= pipeVelX
            lowerPipe['x']+= pipeVelX

    #Add a new pipe when the first is about to cross the leftmost part of the screen     
        if upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])
            
     #if the pipe is out of the screen, romove it
        if upperPipes[0]['x']<- GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

#lets blit our sprites now
    SCREEN.blit(GAME_SPRITES['backgroung'],(0,0))
    for upperPipe, lowerPipe in zip (upperPipes, lowerPipes):
         SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'], upperPipe['y']))
         SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'], lowerPipe['y']))
         

    SCREEN.blit(GAME_SPRITES['base'],(basex, GROUNDY))
    SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
    myDigits = [int(x)for x in list (str(score))]
    width = 0
    for digit in myDigits:      
        width += GAME_SPRITES['numbers']['digit'].get_width()
        Xoffset = (SCREENWIDTH - width)/2

    for digit in myDigits:
         SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset, SCREENHEIGHT*0.12))
         Xoffset += GAME_SPRITES['numbers'][digit].get_width()
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery>GROUNDY -25 or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_height()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height()>pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_height()):
            GAME_SOUNDS['hit'].play()
            return True


    return False

         
def getRandomPipe():
    '''
    generate position of the pipes (one bottom
    straight and one top rotated) for blitting on the screen
    '''
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0,int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2*offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [{'x': pipeX,'y': -y1},#upper pipe
            {'x': pipeX,'y': y2}]#lower pipe

    return pipe
            
                
                


if __name__ == '__main__':
    pygame.init()#intialize all pygame module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('FLAPPYBIRDBYPRASHANT')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('flappy bird/sprites/0.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/1.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/2.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/3.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/4.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/5.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/6.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/7.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/8.png').convert_alpha(),
        pygame.image.load('flappy bird/sprites/9.png').convert_alpha(),)

    GAME_SPRITES['message'] = pygame.image.load('flappy bird/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('flappy bird/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
                            pygame.image.load(PIPE).convert_alpha())

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()                            

    #GAME SOUNDS
    GAME_SOUNDS['die'] = pygame.mixer.Sound('flappy bird/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('flappy bird/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('flappy bird/audio/point.wav')
    GAME_SOUNDS['swooch'] = pygame.mixer.Sound('flappy bird/audio/swooch.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('flappy bird/audio/wing.wav')

while True:
    WelcomeScreen()#shows welcome screen to the user until he press a button
    mainGame()#this is the main game fun
        




