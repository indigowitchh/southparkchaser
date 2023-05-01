import pygame
pygame.init()  
pygame.display.set_caption("south park collect!")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

butters = pygame.image.load('butters.png') #load your spritesheet

#player variables
xpos = 500 #xpos of player
ypos = 765-232 #ypos of player
vx = 0 #x velocity of player
vy=0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

#game variables
timer = 0
score = 0
room = 1

#images and fonts
kenny=pygame.image.load('kenny.png')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('DIFFICULTY:EASY', True, (200, 200, 0))

LEFT=0
RIGHT=1
UP=2
DOWN=3

#animation variables variables
frameWidth = 170
frameHeight = 175
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

while not gameover:
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True

        elif event.type == pygame.KEYUP: #when keys are not being pressed
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
        
          
#physics-------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = 0
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
    #turn off velocity
    else:
        vx = 0
    #UP MOVEMENT
    if keys[DOWN]==True:
         vy=3
    #RIGHT MOVEMENT
    elif keys[UP]==True:
        vy=-3
    #turn off velocity
    else:
        vy=0

    #UPDATE POSITION BASED ON VELOCITY
        
    xpos+=vx #update player xpos
    ypos+=vy
        
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information
    
    if vx < 0: #left animation
        RowNum = 2
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>2: 
           frameNum = 0
    if vx > 0: #right animation
        RowNum = 3
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>2: 
           frameNum = 0

    if vy < 0: #down animation
        RowNum = 1
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>2: 
           frameNum = 0
    if vy > 0: #up animation
        RowNum = 0
        ticker+=1
        if ticker%10==0: 
          frameNum+=1
        if frameNum>2: 
           frameNum = 0
  
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
    screen.fill((255,255,255)) #wipe screen so it doesn't smear   
    screen.blit(text, (20, 20))
    screen.blit(kenny, (500, 500))
    screen.blit(butters, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))


    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
