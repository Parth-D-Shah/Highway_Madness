#importing my modules
import pygame #This module allows me to use pygame in python
import time #This module allows me to use time-related functions
import sys, random #This module allows me to import random and system specific parameters
from pygame.locals import * #This module allows me to import all names in pygame.locals into your current namespace

pygame.init() #This initializes all imported pygame modules

Display_Width = 800 #Now I initialize all my global variables
Display_Height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
yellow = (255,255,0)
bright_yellow = (255,255,204)

Large_Font = pygame.font.Font('freesansbold.ttf',90)
Small_Font = pygame.font.Font('freesansbold.ttf',20)

Truck_Start_X = 174

Current_Car = 0

Game_Pause = False

Music_Pause = False

Game_Display = pygame.display.set_mode((Display_Width,Display_Height)) #This is where the game display is set
pygame.display.set_caption('Highway_Madness')

clock = pygame.time.Clock()

Highway = pygame.image.load('background.png') #Now I load in all my pictures into variables
Play_Button = pygame.image.load('button_play.png')
Play_Button_Pressed = pygame.image.load('button_play_pressed.png')
Quit_Button = pygame.image.load('button_quit.png')
Quit_Button_Pressed = pygame.image.load('button_quit_pressed.png')
Instruction_Button = pygame.image.load('button_instruction.png')
Instruction_Button_Pressed = pygame.image.load('button_instruction_pressed.png')
Back_Button = pygame.image.load('button_back.png')
Back_Button_Pressed = pygame.image.load('button_back_pressed.png')
Play_Again = pygame.image.load('button_play_again.png')
Play_Again_Pressed = pygame.image.load('button_play_again_pressed.png')
Main_Menu_Button = pygame.image.load('button_main_menu.png')
Main_Menu_Button_Pressed = pygame.image.load('button_main_menu_pressed.png')
Continue_Button = pygame.image.load('button_continue.png')
Continue_Button_Pressed = pygame.image.load('button_continue_pressed.png')
Game_Name = pygame.image.load('Game_Name.png')
You_Died = pygame.image.load('You_Died.png')
Paused_Text = pygame.image.load('Paused_Text.png')
Instruction_1 = pygame.image.load('Instruction_1.png')
Instruction_2 = pygame.image.load('Instruction_2.png')
Instruction_3 = pygame.image.load('Instruction_3.png')
Instruction_4 = pygame.image.load('Instruction_4.png')
Choose_Car= pygame.image.load('Choose_Car.png')
Tree_Img = pygame.image.load('tree.png')
Truck_Img = pygame.image.load('truck.png')

Car_Selected = 1
Car_Width = 72

Car_Img_1 = pygame.image.load('car1.png')
Car_Img_2 = pygame.image.load('car2.png')
Car_Img_3 = pygame.image.load('car3.png')
Car_Img_4 = pygame.image.load('car4.png')
Car_Img_5 = pygame.image.load('car5.png')
Car_Img_6 = pygame.image.load('car6.png')
Car_Img_1x = pygame.image.load('car1x.png')
Car_Img_2x = pygame.image.load('car2x.png')
Car_Img_3x = pygame.image.load('car3x.png')
Car_Img_4x = pygame.image.load('car4x.png')
Car_Img_5x = pygame.image.load('car5x.png')
Car_Img_6x = pygame.image.load('car6x.png')

Car_Crash_Sound = pygame.mixer.Sound("Jetpack_Crash.wav") #Now i load in my game music and sound effects
pygame.mixer.music.load('Game_Music.mp3')

background = Highway


class Cursor_Effects: #This class adds in the cursor effects feature
    def __init__(self,Radius,y,x,color,Size,Max_Force,force,life):
        self.y = y
        self.x = x
        self.Size = Size
        self.Max_Force = Max_Force
        self.force = force
        self.Radius = Radius
        self.color = color
        self.life = life
        pygame.draw.circle(Game_Display, self.color, (self.x, self.y), self.Radius)
 
    def fall(self):
        if self.y < Display_Height - self.Radius:
            self.y += self.force
            if self.force < self.Max_Force:
                self.force += 1
        elif self.y > Display_Height - self.Radius or self.y == Display_Height - self.Radius:
            self.y = Display_Height - self.Radius - 1
            self.force = self.force* - 1
            self.Max_Force = self.Max_Force / 2
        pygame.draw.circle(Game_Display, self.color, (self.x, self.y), self.Radius)
        self.life -= 1
        if self.life < 0:
            cursor_effects.remove(self)      
       
 
cursor_effects = []


def car(Car_X, Car_Y): #This subroutine adds the car selection feature
    global Car_Selected
    global Car_Width
    
    if Car_Selected == 1:
        Game_Display.blit(Car_Img_1, (Car_X, Car_Y))
        Car_Width = 72
    elif Car_Selected == 2:
        Game_Display.blit(Car_Img_2, (Car_X, Car_Y))
        Car_Width = 78
    elif Car_Selected == 3:
        Game_Display.blit(Car_Img_3, (Car_X, Car_Y))
        Car_Width = 78
    elif Car_Selected == 4:
        Game_Display.blit(Car_Img_4, (Car_X, Car_Y))
        Car_Width = 78
    elif Car_Selected == 5:
        Game_Display.blit(Car_Img_5, (Car_X, Car_Y))
        Car_Width = 78
    elif Car_Selected == 6:
        random_car(Car_X, Car_Y)


def random_car(x, y): #This subroutine adds the random car selection feature
    global Current_Car
    global Car_Width
    global carSelect

    if Current_Car == 1:
        carSelect = random.randrange(1, 6)

    if carSelect == 1:
        Game_Display.blit(Car_Img_1, (x, y))
        Car_Width = 72
    elif carSelect == 2:
        Game_Display.blit(Car_Img_2, (x, y))
        Car_Width = 78
    elif carSelect == 3:
        Game_Display.blit(Car_Img_3, (x, y))
        Car_Width = 78
    elif carSelect == 4:
        Game_Display.blit(Car_Img_4, (x, y))
        Car_Width = 78
    elif carSelect == 5:
        Game_Display.blit(Car_Img_5, (x, y))
        Car_Width = 78


def truck(truckX,truckY): #This subroutine blits the truck(obstacle) onto the game display
    Game_Display.blit(Truck_Img,(truckX,truckY))


def Truck_Spawn_Global(Car_X): #This subroutine spawns the truck in different positions
    global Truck_Spawn_Global
    global Truck_Start_X
    if 102 <= Car_X <= 247:
        Truck_Start_X = 174
    if 248 <= Car_X <= 397:
        Truck_Start_X = 322
    if 298 <= Car_X <= 547:
        Truck_Start_X = 472
    if 548 <= Car_X <= 693:
        Truck_Start_X = 618


def car_select_1(): #This subroutine displays the home screen after the user has selected the first car
    global Car_Selected
    Car_Selected = 1
    Home_Screen()

def car_select_2(): #This subroutine displays the home screen after the user has selected the second car
    global Car_Selected
    Car_Selected = 2
    Home_Screen()

def car_select_3(): #This subroutine displays the home screen after the user has selected the third car
    global Car_Selected
    Car_Selected = 3
    Home_Screen()

def car_select_4(): #This subroutine displays the home screen after the user has selected the fourth car
    global Car_Selected
    Car_Selected = 4
    Home_Screen()

def car_select_5(): ##This subroutine displays the home screen after the user has selected the fifth car
    global Car_Selected
    Car_Selected = 5
    Home_Screen()

def car_select_6(): ##This subroutine displays the home screen after the user has selected the random car
    global Car_Selected
    Car_Selected = 6
    Home_Screen()


def img_button(img,activeImg,x,y,w,h,action): #This subroutine displays the correct landing screen after pressing a image button
    Mouse_Location = pygame.mouse.get_pos()
    Mouse_Click = pygame.mouse.get_pressed()
    Game_Display.blit(img, (x, y))
    if x+w > Mouse_Location[0] > x and y+h > Mouse_Location[1] > y:
        Game_Display.blit(activeImg, (x-5,y-5))
        if Mouse_Click[0] == 1 and action != None:
            
            if action == "Play":
                Game_Loop()
            elif action == "Quit":
                pygame.quit()
                quit()
            elif action == "Main Menu":
                Home_Screen()
            elif action == "Settings":
                Settings()
            elif action == "Back":
                Home_Screen()
            elif action == "Unpause":
                Un_Pause()
            elif action == "Instructions":
                Instruction_Screen()


def Car_Button(img, x, y, w, h, action): #This subroutine displays the car buttons on the settings screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        Game_Display.blit(img, (x-4, y-4))
        if click[0] == 1:
            action()
            

##def Button_Settings(Button_X,Button_Y,Button_W,Button_H,Active_Colour,Inactive_Colour,Message,action=None):
##    Mouse_Location = pygame.mouse.get_pos()
##    Mouse_Click = pygame.mouse.get_pressed()
##    if Button_X+Button_W > Mouse_Location[0] > Button_X and Button_Y+Button_H > Mouse_Location[1] > Button_Y:
##        pygame.draw.rect(Game_Display, Active_Colour,(Button_X,Button_Y,Button_W,Button_H))
##        
##        if Mouse_Click[0] == 1 and action != None:
##            if action == "Cloudy_Sky":
##                background = Cloudy_Sky
##                pygame.display.update()
##            elif action == "Plain_Fields":
##                background = background2
##                pygame.display.update()
##         
##    else:
##        pygame.draw.rect(Game_Display,Inactive_Colour,(Button_X,Button_Y,Button_W,Button_H))
##
##    textSurf,textRect = Text_Command(Message,Small_Font)
##    textRect.center = ((Button_X+(Button_W/2)),(Button_Y+(Button_H/2)))
##    Game_Display.blit(textSurf,textRect)
    

##def Power_Ups(Power_Up_X, Power_Up_Y, Power_Up_Width, Power_Up_Height, color):
##        pygame.draw.rect(Game_Display, color, [Power_Up_X, Power_Up_Y, Power_Up_Width, Power_Up_Height])


def tree(treeX,treeY): #This subroutine displays the trees in the game
    Game_Display.blit(Tree_Img, (treeX, treeY))


def Scoreboard(count): #This subroutine displays the scoreboard
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(count),True,black)
    Game_Display.blit(text, (5, 5))


##def Obstacles(Obstacles_X, Obstacles_Y, Obstacles_Width, Obstacles_Height, color):
##    pygame.draw.rect(Game_Display, color, [Obstacles_X, Obstacles_Y, Obstacles_Width, Obstacles_Height])

     
def Text_Command(text, font): #This subroutine is vital for the text to render and is used in conjuction with other subroutines
    Text_Level = font.render(text, True, black)
    return Text_Level, Text_Level.get_rect()

def Message_Car_Crash(text): #This subroutine plays the correct sound effects and prepares for the transition phase from player death to next screen
    pygame.mixer.Sound.play(Car_Crash_Sound)
    pygame.mixer.music.stop()
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = Text_Command(text, largeText)
    TextRect.center = ((Display_Width/2),(Display_Height/2))
    Game_Display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    Death_Screen()
    
    
def Car_Crash(): #This subroutine displays the "Game Over" message when the player loses the game
    Message_Car_Crash('Game Over')


def Button(Button_X,Button_Y,Button_W,Button_H,Active_Colour,Inactive_Colour,Message,action=None): #This subroutine displays the settings screen after pressing the settings button
    Mouse_Location = pygame.mouse.get_pos()
    Mouse_Click = pygame.mouse.get_pressed()
    if Button_X+Button_W > Mouse_Location[0] > Button_X and Button_Y+Button_H > Mouse_Location[1] > Button_Y:
        pygame.draw.rect(Game_Display, Active_Colour,(Button_X,Button_Y,Button_W,Button_H))
        
        if Mouse_Click[0] == 1 and action != None:
            if action == "Settings":
                Settings()
                
    else:
        pygame.draw.rect(Game_Display,Inactive_Colour,(Button_X,Button_Y,Button_W,Button_H))

    textSurf,textRect = Text_Command(Message,Small_Font)
    textRect.center = ((Button_X+(Button_W/2)),(Button_Y+(Button_H/2)))
    Game_Display.blit(textSurf,textRect)


def Button_Pause(Button_X,Button_Y,Button_W,Button_H,Active_Colour,Inactive_Colour,Message,action=None): #This subroutine displays the pause menu after pressing the pause button

    Mouse_Location = pygame.mouse.get_pos()
    Mouse_Click = pygame.mouse.get_pressed()
    if Button_X+Button_W > Mouse_Location[0] > Button_X and Button_Y+Button_H > Mouse_Location[1] > Button_Y:
        pygame.draw.rect(Game_Display, Active_Colour,(Button_X,Button_Y,Button_W,Button_H))
        
        if Mouse_Click[0] == 1 and action != None:
            if action == "Unpause":
                Un_Pause()
            elif action == "Main_Menu":
                Home_Screen()
                      
    else:
        pygame.draw.rect(Game_Display,Inactive_Colour,(Button_X,Button_Y,Button_W,Button_H))

    textSurf,textRect = Text_Command(Message,Small_Font)
    textRect.center = ((Button_X+(Button_W/2)),(Button_Y+(Button_H/2)))
    Game_Display.blit(textSurf,textRect)    


def Background_Game_Loop(bgX, bgY): #This subroutine displays the background
    Game_Display.blit(background, (bgX, bgY))


def Speed_Counter(speed): #This subroutine displays the speed counter
    font = pygame.font.SysFont(None, 25)
    text = font.render('Speed: '+str(speed), True, black)
    Game_Display.blit(text, (5, 30))

    
def Instruction_Screen(): #This subroutine when called will display the instructions screen
    global Music_Pause
        
    Instruction_Screen = True
    while Instruction_Screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        Game_Display.fill(white)
        Game_Display.blit(background,(0,0))
        Mouse_Location = pygame.mouse.get_pos()
        img_button(Play_Button,Play_Button_Pressed,172,450,161,50,"Play")
        img_button(Back_Button,Back_Button_Pressed,463,450,161,50,"Back")
        Game_Display.blit(Instruction_1,(50,150))
        Game_Display.blit(Instruction_2,(150,200))
        Game_Display.blit(Instruction_3,(65,260))
        Game_Display.blit(Instruction_4,(65,325))
        
        z=1
        Pos_x,Pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
 
        if z == 1:
                cursor_effects.append(Cursor_Effects(4, Pos_y, Pos_x, (random.randint(1,255),random.randint(1,255),random.randint(1,255)),"L", 15, 1 ,100))
                z = 3
        elif z > 1:
                z-=1   
 
        for i in cursor_effects:
                i.fall()
        
        pygame.display.update()
        clock.tick(60)


def Death_Screen(): #This subroutine when called will display the death screen

    global Music_Pause
    
    if Music_Pause == False:
        pygame.mixer.music.play(-1)
    
    Death_Screen = True
    
    while Death_Screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Game_Display.fill(white)
        Game_Display.blit(background,(0,0))
        Mouse_Location = pygame.mouse.get_pos()
        img_button(Play_Again,Play_Again_Pressed,100,500,161,50,"Play")
        img_button(Quit_Button,Quit_Button_Pressed,533,500,161,50,"Quit") #525
        img_button(Main_Menu_Button,Main_Menu_Button_Pressed,318,500,200,50,"Main Menu") #300
        Game_Display.blit(You_Died,(200,250))
        
        
        z=1
        Pos_x,Pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
 
        if z == 1:
                cursor_effects.append(Cursor_Effects(4, Pos_y, Pos_x, (random.randint(1,255),random.randint(1,255),random.randint(1,255)),"L", 15, 1 ,100))
                z = 3
        elif z > 1:
                z-=1   
 
        for i in cursor_effects:
                i.fall()
        
        pygame.display.update()
        
        clock.tick(60)


def Home_Screen(): #This subroutine when called will display the home screen
    
    global Music_Pause
    
    if Music_Pause == False:
        pygame.mixer.music.play(-1)
    
    Home_Screen = True
    while Home_Screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    Game_Loop()
        
        Game_Display.fill(white)
        Game_Display.blit(background,(0,0))
        
        Mouse_Location = pygame.mouse.get_pos()
        img_button(Play_Button,Play_Button_Pressed,100,500,161,40,"Play")
        img_button(Quit_Button,Quit_Button_Pressed,534,500,161,50,"Quit")
        img_button(Instruction_Button,Instruction_Button_Pressed,310,100,200,50,"Instructions")
        Button(650,50,150,50,bright_yellow,yellow,"Settings","Settings")
        Game_Display.blit(Game_Name,(50,250))

        z=1
        Pos_x,Pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
 
        if z == 1:
                cursor_effects.append(Cursor_Effects(4, Pos_y, Pos_x, (random.randint(1,255),random.randint(1,255),random.randint(1,255)),"L", 15, 1 ,100))
                z = 3
        elif z > 1:
                z-=1   
 
        for i in cursor_effects:
                i.fall()
 
        pygame.display.update()
        clock.tick(60)


def Un_Pause(): #This subroutine will unpause the game
    global Game_Pause
    Game_Pause = False


def Pause(): #This subroutine will pause the game
##    global Music_Pause
##    
##    if Music_Pause == False:
##        pygame.mixer.music.play(-1)
        
    global Game_Pause
    Game_Pause = True
    while Game_Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Game_Display.fill(white)
        Game_Display.blit(background,(0,0))
        
        Mouse_Location = pygame.mouse.get_pos()
        img_button(Continue_Button,Continue_Button_Pressed,100,500,150,50,"Unpause")
        img_button(Quit_Button,Quit_Button_Pressed,533,500,161,50,"Quit")
        img_button(Main_Menu_Button,Main_Menu_Button_Pressed,318,500,200,50,"Main Menu")
        Game_Display.blit(Paused_Text,(250,250))

        z=1
        Pos_x,Pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                elif event.type == MOUSEBUTTONDOWN:
                        z = 1
                elif event.type == MOUSEBUTTONUP:
                        z = 0
                        
        if z == 1:
                cursor_effects.append(Cursor_Effects(4, Pos_y, Pos_x, (random.randint(0,255),random.randint(0,255),random.randint(0,255)),"L", 15, 1 ,100))
                z = 3
        elif z > 1:
                z-=1   
 
        for i in cursor_effects:
                i.fall()
        
        pygame.display.update()
        clock.tick(60)


def Settings(): #This subroutine when called will display the settings screen
##    global Music_Pause
##    
##    if Music_Pause == False:
##        pygame.mixer.music.play(-1)
        
    Setting = True
    while Setting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        Game_Display.fill(white)
        Game_Display.blit(background,(0,0))
##        TextSurf,TextRect = Text_Command("Choose your car here",Small_Font)
##        TextRect.center = ((Display_Width/2),(Display_Height/2))
##        Game_Display.blit(TextSurf,TextRect)
        
        Mouse_Location = pygame.mouse.get_pos()
        Game_Display.blit(Car_Img_1, (200, 150))
        Game_Display.blit(Car_Img_2, (361, 150))
        Game_Display.blit(Car_Img_3, (522, 150))
        Game_Display.blit(Car_Img_4, (200, 350))
        Game_Display.blit(Car_Img_5, (361, 350))
        Game_Display.blit(Car_Img_6, (522, 350))
        Car_Button(Car_Img_1x, 200, 150, 72, 113, car_select_1)
        Car_Button(Car_Img_2x, 361, 150, 78, 114, car_select_2)
        Car_Button(Car_Img_3x, 522, 150, 78, 112, car_select_3)
        Car_Button(Car_Img_4x, 200, 350, 78, 114, car_select_4)
        Car_Button(Car_Img_5x, 361, 350, 78, 114, car_select_5)
        Car_Button(Car_Img_6x, 522, 350, 78, 114, car_select_6)
        Game_Display.blit(Choose_Car,(220,280))

        z=1
        Pos_x,Pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                elif event.type == MOUSEBUTTONDOWN:
                        z = 1
                elif event.type == MOUSEBUTTONUP:
                        z = 0
 
        if z == 1:
                cursor_effects.append(Cursor_Effects(4, Pos_y, Pos_x, (random.randint(1,255),random.randint(1,255),random.randint(1,255)),"L", 15, 1 ,100))
                z = 3
        elif z > 1:
                z-=1   
 
        for i in cursor_effects:
                i.fall()
        
        pygame.display.update()
        clock.tick(60)


##def Truck_Spawn_Global(Car_X): #This subroutine spawns the truck in different positions
##    global Truck_Spawn_Global
##    global Truck_Start_X
##    if 102 <= Car_X <= 247:
##        Truck_Start_X = 174
##    if 248 <= Car_X <= 397:
##        Truck_Start_X = 322
##    if 298 <= Car_X <= 547:
##        Truck_Start_X = 472
##    if 548 <= Car_X <= 693:
##        Truck_Start_X = 618

 
def Game_Loop():
    # Calling all the global variables to use in the loop
    global pause
    global crashed
    global Current_Car
    global Truck_Start_X
    global Music_Pause

    # Defining the location where the car will start off 
    Car_X = (Display_Width / 2) - 36
    Car_Y = Display_Height - 114
    Car_X_Change = 0

    bgY = -100

    # Defining the location where the truck will start off
    Truck_Spawn_Global(Car_X)
    truck_startY = -600
    truck_speed = 5
    truck_width = 100
    truck_height = 190

    Tree_Start_X1 = random.randrange(0, 45)
    Tree_Start_X2 = random.randrange(Display_Width - 98, Display_Width - 49)
    Tree_Start_Area = random.randint(1,2)
    if Tree_Start_Area == 1:
        Tree_Start_X = Tree_Start_X1
    elif Tree_Start_Area == 2:
        Tree_Start_X = Tree_Start_X2
    Tree_Start_Y = -100

    Dodged = 0

    # Initiaitng loop variable
    Game_End = True

    # Main Game Loop
    while Game_End == True:
        
        # Checks for quit event to exit game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Checks if left and right arrow keys are pushed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Car_X_Change = -10
                if event.key == pygame.K_RIGHT:
                    Car_X_Change = 10
                if event.key == pygame.K_p:
                    pause = True
                    Pause()

            # Checks if left and right arrow keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    Car_X_Change = 0


        Car_X += Car_X_Change
        truck_startY += truck_speed
        Tree_Start_Y += (truck_speed * 2)
        bgY += (truck_speed * 2)
        Current_Car += 1

        # Draws objects on the screen
        
        Background_Game_Loop(0,bgY)
        truck(Truck_Start_X, truck_startY)
        car(Car_X, Car_Y)
        Scoreboard(Dodged)
        Speed_Counter(truck_speed)
        tree(Tree_Start_X, Tree_Start_Y)

        if Car_X > Display_Width - 172 or Car_X < 96:
            crashed = True
            Car_Crash()

        if truck_startY > Display_Height:
            truck_startY = 0 - truck_height
            Truck_Spawn_Global(Car_X)
            Dodged += 1
            truck_speed += 0.25

        if bgY > -1:
            bgY = -100

        if Tree_Start_Y > Display_Height:
            Tree_Start_X1 = random.randrange(0, 45)
            Tree_Start_X2 = random.randrange(Display_Width - 98, Display_Width - 49)
            Tree_Start_Area = random.randint(1,2)
            if Tree_Start_Area == 1:
                Tree_Start_X = Tree_Start_X1
            elif Tree_Start_Area == 2:
                Tree_Start_X = Tree_Start_X2
            Tree_Start_Y = -100

        if Car_Y < truck_startY + truck_height:
            if Car_X > Truck_Start_X and Car_X <Truck_Start_X + truck_width or Car_X + Car_Width > Truck_Start_X and Car_X + Car_Width < Truck_Start_X + truck_width:
                crashed = True
                file = open('leaderboard.txt','a') 
                file.write(str(Dodged))
                file.close()
                Car_Crash()
                
        pygame.display.update()# Updates the screen for each frame with the currently drawn objects
        clock.tick(60)# Setting frames per second(FPS)
        

Leaderboard_Name = input("Enter your name: ") #Asks for the player name and places it into a text file
file = open('leaderboard.txt','a') 
file.write(Leaderboard_Name)
file.close()
 
Home_Screen()
Game_Loop()
pygame.quit()
quit()




