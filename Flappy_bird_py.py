
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
    upperPipes = [{'x': SCREENWITH+200,'y':newPipe1[0]['y']},
                  {'x': SCREENWITH+200+(SCREENWIDTH/2),'y':newPipe2[1]['y']}]

    #my list of lower pipes
    lowerPipes = [{'x': SCREENWITH+200,'y':newPipe1[0]['y']},
                  {'x': SCREENWITH+200+(SCREENWIDTH/2),'y':newPipe2[1]['y']}]


    pipeVelX = -4

    playerVelY = 9
    playerMaxVelY = -10
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
                    GAME_SOUNDS['Wing'],play()


def getRandomPipe():
    '''
    generate position of the pipes (one bottom
    straight and one top rotated) for blitting on the screen
    '''
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0,int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2*offset))
    pipeX = SCREENWWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe - [{'x': pipeX,'y': y1}#upper pipe
            {'x': pipeX,'y': y2}]#lower pipe
    return pipe
            
                
                


if __name__ == '__main__':
    #this will be the main point from where game will start
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
        




