import pygame
from pygame import *
import random
from pygame import mixer
mixer.init()
# color code (RGB)
white = (255,255,255)
snakeC = (34,139,34)
apple = (255,0,0)
black = (0,0,0)


## global variables ##

SCREENHEIGHT = 1010
SCREENWIDTH =  660
game_sprites = {}
game_audio = {}
snkvalInit = 4
FPS = 60
clock = pygame.time.Clock()



# setting game window size and caption
gameWindow = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))
pygame.display.update()
pygame.display.set_caption("Snake")

# Loading Gmame Sprites
game_sprites['message'] = pygame.image.load('gallary/images/message.png')
game_sprites['gameover'] = (
    pygame.image.load('gallary/images/gameover1.png').convert_alpha(),
    pygame.image.load('gallary/images/gameover2.png').convert_alpha(),
    pygame.image.load('gallary/images/gameover3.png').convert_alpha()
)
game_sprites['background'] = pygame.image.load('gallary/images/background.png')
game_sprites['score'] = (
    pygame.image.load('gallary/images/0.png'),
    pygame.image.load('gallary/images/1.png'),
    pygame.image.load('gallary/images/2.png'),
    pygame.image.load('gallary/images/3.png'),
    pygame.image.load('gallary/images/4.png'),
    pygame.image.load('gallary/images/5.png'),
    pygame.image.load('gallary/images/6.png'),
    pygame.image.load('gallary/images/7.png'),
    pygame.image.load('gallary/images/8.png'),
    pygame.image.load('gallary/images/9.png'),
)
game_sprites['apple'] = pygame.image.load('gallary/images/apple.png').convert_alpha()
game_sprites['decorations'] = pygame.image.load('gallary/images/decoration.png').convert_alpha()
game_sprites['food'] = pygame.image.load('gallary/images/food.png').convert_alpha()
# audio
# musics
game_audio['intro'] ='gallary/audio/intro.mp3'
game_audio['bgm'] = 'gallary/audio/bgm.mp3'
game_audio['gameOver'] = 'gallary/audio/gameover.mp3'
# sound effects
game_audio['snkeat'] = pygame.mixer.Sound('gallary/audio/eatsound.wav')

def welcomeScreen():
    mixer.music.load(game_audio['intro'])
    mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
            elif event.type == KEYDOWN and (event.key == K_LEFT or K_RIGHT or K_UP or K_DOWN):
                mixer.music.stop()
                return
            else:
                gameWindow.blit(game_sprites['message'],(0,0))
                pygame.display.update()    
                clock.tick(FPS)      

def snake_length(gameWindow,color,snake_list, snkSize):
    for xaxis, yaxis in snake_list:
        pygame.draw.rect(gameWindow, color,(xaxis, yaxis, snkSize,snkSize))

    
def mainGame():
    # maingame variables 
    snkX = 40
    snkY =  600

    foodX = random.randint(20,SCREENWIDTH/2)
    foodY = random.randint(20, SCREENHEIGHT/2)
    

    snkSize = 20
    snkvalX = 0
    snkvalY = 0
    snakeList = []
    numbers = []
    snkLength = 1
    
    score = 0
    
    game_quit = False
    game_over = False
    
    # playing game background music
    mixer.music.load(game_audio['bgm'])
    mixer.music.set_volume(0.2)
    mixer.music.play()
    while not game_quit:
        
        if game_over == True:
            mixer.music.load(game_audio['gameOver'])
            mixer.music.play(-1)
            game_quit = True
            return
                    
                
        else:
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    game_quit = True
                # adding key binding for snake movement
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        snkvalX =  + snkvalInit
                        snkvalY = 0

                    if event.key == K_LEFT:
                        snkvalX =  - snkvalInit
                        snkvalY = 0

                    if event.key == K_DOWN:
                        snkvalX = 0
                        snkvalY =  + snkvalInit

                    if event.key == K_UP:
                        snkvalX = 0
                        snkvalY =  - snkvalInit
        # setting game over whenever snake hits any of walls
        if snkX<0 or snkX> SCREENHEIGHT or snkY< 0 or snkY > SCREENWIDTH:
            game_over = True
            mixer.music.stop()
        
        # initiliazing game score system
        if abs(snkX - foodX) < 25 and abs(snkY - foodY) < 25:
            game_audio['snkeat'].play()
            score += 1
            foodX = random.randint(20,950)
            foodY = random.randint(20, 600)
            snkLength += 20
           
    
        head = []
        head.append(snkX)
        head.append(snkY)
        snakeList.append(head)

        #incrising snake length after eating food
        if len(snakeList) > snkLength:
            del snakeList[0]
        
        # fetching degits in score as list
        numbers = [int(i) for i in list(str(score))]
        width = 0
        

        # Finding the width of numbers
        for number in numbers:
            width += game_sprites['score'][number].get_width()
            
        Xoffset = (SCREENWIDTH - width)/9

        # bliting number images on windows
        
        snkX = snkvalX + snkX
        snkY = snkvalY + snkY
        
        #gameWindow.fill(black)
        # bliting game background
        gameWindow.blit(game_sprites['background'],(0,0))
        
        for number in numbers:
            gameWindow.blit(game_sprites['score'][number],
            (Xoffset, SCREENHEIGHT * 0.009))
            
            Xoffset += game_sprites['score'][number].get_width()
        
        
        # game over when snake hits it's own body
        if head in snakeList[:-1]:
            game_over = True

        
        # drawing snake
        snake_length(gameWindow, snakeC, snakeList, snkSize)
        # drawing food
        #pygame.draw.rect(gameWindow, apple,(foodX, foodY, snkSize, snkSize))
        gameWindow.blit(game_sprites['food'], (foodX, foodY))
        gameWindow.blit(game_sprites['apple'],(10,4))
        gameWindow.blit(game_sprites['decorations'],(0,0))
        
        
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    exit()

def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN and(event.key == K_RETURN):
                mixer.music.stop()
                mainGame()

        c = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        gameWindow.fill(c)
        gameWindow.blit(game_sprites['gameover'][random.randint(0,2)],(0,0))
        clock.tick(1)
        pygame.display.update()


if __name__ == '__main__':
    welcomeScreen()
    mainGame()
    game_over()
   
