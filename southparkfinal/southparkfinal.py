import pygame
pygame.init()  
pygame.display.set_caption("south park collect!")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop


#player variables
xpos = 100 #xpos of player
ypos = 765-232 #ypos of player
vx = 0 #x velocity of player
vy=0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

#game variables
timer = 0
score = 0
room = 1
LEFT=0
RIGHT=1
UP=2
DOWN=3

#images and fonts
butters = pygame.image.load('butters.png') #load your spritesheet
kenny=pygame.image.load('kenny.png')
stan=pygame.image.load('stan.png')
kyle= pygame.image.load('kyle.png')
cartman = pygame.image.load('cartman.png')
background = pygame.image.load('background.jpg')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('DIFFICULTY:EASY', True, (255, 195, 170))
text2 = font.render('CATCH KENNY!', True, (255, 94, 5))

#animation variables
frameWidth = 170
frameHeight = 175
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0


#game loop------------------------------------------------------------------------------
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
        
#changing the rooms based on the players position
        if xpos >= 1000 and room == 1:
            room = 2
            xpos = 10
        elif xpos < 0 and room == 2:
            room = 1
            xpos = 700
        elif xpos >= 1000 and room == 2:
            room = 3
            xpos = 10
        elif xpos < 0 and room == 3:
            room = 2
            xpos = 700
        elif xpos >= 1000 and room == 3:
            room = 4
            xpos = 10
        elif xpos < 0 and room == 4:
            room = 3
            xpos = 700       
        
        #dont go past screen proportions
        if xpos < 0 and room ==1:
            xpos = 10
            print("Out of bounds!")
        if ypos < 0:
            ypos = 0
            print("Out of bounds!")
        if ypos >800-175:
            ypos = 800-175
            print("Out of bounds!")
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
    ypos+=vy #update player ypos
        
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
    screen.blit(background,(0,0)) #add background
    screen.blit(butters, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    screen.blit(text, (20, 20)) #add first text
    screen.blit(text2, (750,20)) #add second text
    
    #rooms
    if room == 1: #kenny
        screen.blit(kenny, (500, 500))
        text = font.render('DIFFICULTY:EASY', True, (253, 245, 226))
        text2 = font.render('CATCH KENNY!', True, (255, 94, 5))

    if room == 2: #stan
        screen.blit(stan,(600,600))
        text = font.render('DIFFICULTY:MILD', True, (210, 161, 140))
        text2 = font.render('CATCH STAN!', True, (27, 3, 163))
    
    if room == 3: #kyle
        screen.blit(kyle,(400,400))
        text = font.render('DIFFICULTY:MEDIUM', True, (165, 126, 110))
        text2 = font.render('CATCH KYLE!', True, (0, 128, 0))

    if room == 4: #cartman
        screen.blit(cartman,(300,300))
        text = font.render('DIFFICULTY:HARD', True, (75, 57, 50))
        text2 = font.render('CATCH ERIC!', True, (255, 0, 0))

   


    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
