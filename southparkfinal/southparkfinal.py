
import pygame
import random
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
keys = [False, False, False, False, False, False] #this list holds whether each key has been pressed

#game variables
timer = 0
score = 0
gainscore = False
room = 0

LEFT=0
RIGHT=1
UP=2
DOWN=3
SPACE=4

states = ["B","M","E"]
states = "B"

#images and fonts
butters = pygame.image.load('butters.png') #load your spritesheet
kenny=pygame.image.load('kenny.png')
stan=pygame.image.load('stan.png')
kyle= pygame.image.load('kyle.png')
cartman = pygame.image.load('cartman.png')

background = pygame.image.load('background.jpg')
font = pygame.font.Font('freesansbold.ttf', 32)
ending = pygame.image.load('ending.jpg')
text = font.render('DIFFICULTY:EASY', True, (255, 195, 170))
text1 = font.render('SCORE:', True, (0,0,0))
textuh = font.render(str(score), True, (0,0,0))
text2 = font.render('CATCH KENNY!', True, (255, 94, 5))
text3 = font.render('WELCOME TO SOUTH PARK CHASER', True,(0,139,139))
text4 = font.render('Press space to start!', True,(102,205,170))
text5= font.render('Use keyboard arrows to move!', True,(95,158,160))
text6 = font.render('OH, HAMBURGERS! YOU DID IT!!!', True,(95,158,160))

#sound---------------------------------------------------------------------
caught = pygame.mixer.Sound('prettygood.mp3')
soundtrack = pygame.mixer.music.load('elevator.mp3')
pygame.mixer.music.play(-1)

#animation variables
frameWidth = 170
frameHeight = 175
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0


#class for characters------------------------------------------------------------------
class Chase:
    def __init__(self,xpos,ypos,direction,pic,velx,vely,isCaught):
        self.xpos = xpos
        self.ypos = ypos
        self.position = direction
        self.Caught = isCaught
        self.pic = pic
        self.vx = velx
        self.vy = vely
        

    def Chasing(self):

        if timer % 30== 0: #only change direction every 50 game loops
            self.position = random.randrange(0, 4) #set random direction
        if self.position == LEFT:
            self.xpos-=self.vx #move left
        elif self.position == RIGHT :
            self.xpos += self.vx #move right
        elif self.position == UP : 
            self.ypos +=self.vy #move up
        elif self.position == DOWN :
            self.ypos -=self.vy #move down

       
        if self.xpos +100 >1000:
            self.position = LEFT
        elif self.xpos <0:
            self.position = RIGHT
        elif self.ypos+100 > 800:
            self.position = DOWN
        elif self.ypos < 0:
            self.position = UP
            
        return self.xpos and  self.ypos

    def Collide(self, PlayerX, PlayerY):
        if self.Caught == False:
          if PlayerX+170 > self.xpos:
           if PlayerX < self.xpos+50:
               if PlayerY+175 >self.ypos:
                   if PlayerY < self.ypos+50:
                       self.Caught = True
                       pygame.mixer.Sound.play(caught)
                       return True
                        
    def Draw(self,pic):
        if self.Caught == False:
            screen.blit(self.pic, (self.xpos, self.ypos))
        
ken = Chase(200,400,RIGHT,kenny,50,20, False)
marsh = Chase(700,450,LEFT,stan,18,18, False)
jersey = Chase(250,200,DOWN,kyle,50,15, False)
eric = Chase(650,300,UP,cartman,15,15, False)

#game loop------------------------------------------------------------------------------
while not gameover:
    clock.tick(60) #FPS
    timer+=1
    
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
            elif event.key == pygame.K_SPACE:
                keys[SPACE]= True

        elif event.type == pygame.KEYUP: #when keys are not being pressed
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False
#changing the rooms based on the players position
        if score ==4 and room == 4:
            states = "E"
        if keys[SPACE] == True and room == 0:
            room = 1
            states = "M"
        elif xpos >= 1000 and room == 1:
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
        if xpos < 0 and room ==0:
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
        vx=-2
        direction = 0
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 2
    #turn off velocity
    else:
        vx = 0
    #UP MOVEMENT
    if keys[DOWN]==True:
         vy=2
    #RIGHT MOVEMENT
    elif keys[UP]==True:
        vy=-2
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
    screen.blit(butters, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))


    if states == "B":
        screen.blit(text3,(200,200)) #add third text
        screen.blit(text4,(350,400)) #add fourth text
        screen.blit(text5,(300,600))
        text3 = font.render('WELCOME TO SOUTH PARK CHASER', True,(0,139,139))
        text4 = font.render('Press space to start!', True,(102,205,170))
        text5= font.render('Use keyboard arrows to move!', True,(95,158,160))


    if states == "M":
        screen.blit(background,(0,0)) #add background
        screen.blit(butters, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
        screen.blit(text, (20, 20)) #add first text
        screen.blit(text2, (750,20)) #add second text
        screen.blit(text1,(400,40))
        screen.blit(textuh,(545,40))


    if states == "E":

        xpos = 400
        ypos = 600
        screen.blit(text6,(200,600))
        screen.blit(ending,(0,0))

    if gainscore == True:
        score += 1
        gainscore = False

    #rooms
    if room == 0: #intro
        states = "B"

    if room == 1: #kenny
        ken.Draw(kenny)
        ken.Chasing()
        gainscore = ken.Collide(xpos,ypos)
        text = font.render('DIFFICULTY:EASY', True, (253, 245, 226))
        text2 = font.render('CATCH KENNY!', True, (255, 94, 5))
        text1 = font.render('SCORE:', True, (0,0,0))
        textuh = font.render(str(score), True, (0,0,0))


    if room == 2: #stan
        marsh.Draw(stan)
        marsh.Chasing()
        gainscore = marsh.Collide(xpos,ypos) 
        text = font.render('DIFFICULTY:MILD', True, (210, 161, 140))
        text2 = font.render('CATCH STAN!', True, (27, 3, 163))
        text1 = font.render('SCORE:', True, (0,0,0))
        textuh = font.render(str(score), True, (0,0,0))


    if room == 3: #kyle
        jersey.Draw(kyle)
        jersey.Chasing()
        gainscore = jersey.Collide(xpos,ypos)
        text = font.render('DIFFICULTY:MEDIUM', True, (165, 126, 110))
        text2 = font.render('CATCH KYLE!', True, (0, 128, 0))
        text1 = font.render('SCORE:', True, (0,0,0))
        textuh = font.render(str(score), True, (0,0,0))


    if room == 4: #cartman
        eric.Draw(cartman)
        eric.Chasing()
        gainscore = eric.Collide(xpos,ypos)
        text = font.render('DIFFICULTY:HARD', True, (75, 57, 50))
        text2 = font.render('CATCH ERIC!', True, (255, 0, 0))
        text1 = font.render('SCORE:', True, (0,0,0))
        textuh = font.render(str(score), True, (0,0,0))

    #if room == 5: #outro
       #states = "E"


    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
