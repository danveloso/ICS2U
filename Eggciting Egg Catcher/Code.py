import pygame
import math
import random
#Defining all boolean variables
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 500
pause = False
lose = False
startmenu = True
start = False
tutorial = False
controls = False
mouse_option = False
keyboard = True
caught_egg = False
caught_regg = False
music = True
booleans = [pause,startmenu,start,tutorial,controls,mouse_option,keyboard,caught_egg,caught_regg,music,lose]
left = False; right = False;
movement = [left,right]
level = 1
lives = 6
score = 0
combo_counter = 0
combo = 1
bonus = score * combo
level_cap = 10
egg_radius = 15
eggs_caught = 0
total_eggs_caught = 0
red = [255, 0, 0]
white = [255, 255, 255]
black = [0, 0, 0]
cyan = [0, 255, 255]
darkred = [190,0,0]
x_egg = random.randint(egg_radius,WINDOW_WIDTH - egg_radius)
x_regg = random.randint(egg_radius,WINDOW_WIDTH - egg_radius)
y_egg = 0
y_regg = 0
x_pos = 200
y_pos = 650
x_speed = 15
x_size = 100
y_size = 70
allscores = [level,level_cap, eggs_caught, total_eggs_caught,lives,score,combo,combo_counter]
basket = [[x_pos,y_pos],[x_size,y_size],x_speed]
egg = [[x_egg, y_egg],egg_radius]
rotten_egg = [[x_regg,y_regg],egg_radius]
play_button = [[150,300],[200,50]]
controls_button = [[150,400],[200,50]]
tutorial_button = [[150,500],[200,50]]
controls_keyboard_button = [[100,100],[300,250]]
controls_mouse_button = [[100,450],[300,250]]
little_quit_button = [[200,590],[100,35]]
pause_menu_reset_button = [[100,300],[300,100]]
pause_menu_quit_button = [[100,400],[300,100]]
loss_reset_button = [[100,300],[300,150]]
loss_quit_button = [[100,450], [300,150]]
#loading the images
pygame.mixer.init()
LossScreen = pygame.image.load('LossScreen.png')
background = pygame.image.load('background.png')
EggBasket = pygame.image.load('basket1.png')
EGG = pygame.image.load('Egg2.png')
Regg = pygame.image.load('Regg.png')
levelimg = pygame.image.load('level.png')
scoreimg = pygame.image.load('Score.png')
life = pygame.image.load('life.png')
baskettop = pygame.image.load('baskettop.png')
StartMenu = pygame.image.load('StartMenu.png')
PauseMenu = pygame.image.load('PauseMenu.png')
Tutorial = pygame.image.load('Tutorial.png')
menu = pygame.image.load('Menu.png')
comboimg = pygame.image.load('Combo.png')
Options = pygame.image.load('Options.png')
pygame.init()  #initializes the graphics module
myfont = pygame.font.SysFont("Arial Black",30,)
myfont2 = pygame.font.SysFont('Comic Sans',40,bold=True,)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # define window size
pygame.display.set_caption('Egg Catcher')  # title of program that
pygame.mixer.music.load('eggsong.mp3') # load an mp3 file
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.3)
  #Defining all my functions (literally all of my code lol)

def AfterLoss():
    window.blit(LossScreen, (0, 0))
    myfont3 = pygame.font.SysFont("Arial Black", 20, )
    total_catches = myfont3.render(str(allscores[3]), 1, white) #rendering my total eggs into a txt.
    level_text = myfont3.render(str(allscores[0]), 1, white)  # rendering my level into a txt.
    window.blit(total_catches, (200, 95))
    window.blit(level_text, (365, 95))
    pygame.mouse.set_visible(True)
    if ButtonCheck(loss_reset_button): # reseting the game (im reeaally proud of thiss!!)
        ScoreReset()
        booleans[10] = False
    if ButtonCheck(loss_quit_button): #quitting after loss
        pygame.quit()
def ButtonCheck(a_button):  #IM REALLY PROUD OF THIS!!!! OK SO ITS A GENERIC BUTTON PRESS CHECKER!!! SO SIMPLE BUT SO USEFUL!!!!
    if event.type == pygame.MOUSEBUTTONDOWN:
        if a_button[0][0] < mouse[0] < a_button[0][0] + a_button[1][0] \
        and a_button[0][1] < mouse[1] < a_button[0][1] + a_button[1][1]:
            return(True)
        return(False)
def ScoreReset():   # To reset all my scores, possibly usefull when you lose and want to reset without closing game.
    allscores[0] = 1; allscores[1] = 10; allscores[2] = 0; allscores[3] = 0; allscores[4] = 6; allscores[5] = 0
    allscores[6] = 1; allscores[7] = 0; egg[0][1] = -5; rotten_egg[0][1] = -5
def MenuThings():  # All things related to the menu, basically images and code before the game starts.
    if booleans[1]:  # If startmenu then draw it lol.
        window.blit(StartMenu,(0,0))
    if ButtonCheck(play_button) and booleans[1]: #These 3 lines check for any 3 buttons in the main menu being pressed!
        booleans[2] = True
        booleans[1] = False
    if ButtonCheck(controls_button) and booleans[1]:
        booleans[4] = True
    if ButtonCheck(tutorial_button) and booleans[1]:
        booleans[3] = True
    if ButtonCheck(little_quit_button) and booleans[1]:
        pygame.quit() #Using this quit button gives a video system error but I don't think that's a legitemate error
    if booleans[4]:  # Controlling the Controls menu, the irony.
        window.blit(Options,(0,0))
        booleans[1] = False
        if ButtonCheck(controls_keyboard_button): #checking if the keyboard option is chosen in the controls menu.
            pygame.mouse.set_pos(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2) #putting you back in the main menu after choosing the option.
            booleans[6] = True
            booleans[4] = False
            booleans[1] = True
        if ButtonCheck(controls_mouse_button): #checking if the mouse option is chosen in controls menu.
            pygame.mouse.set_pos(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2) #putting you back in main menu after choosing the option.
            booleans[6] = False
            booleans[4] = False
            booleans[1] = True
    if booleans[3]:
        window.blit(Tutorial,(0,0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mouse.set_pos(WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2)  # putting you back in main menu after choosing the option.
                booleans[3] = False
                booleans[1] = True
def DrawLives(): #Just drawing my lives on my screen, I'm pretty proud of this.
    x_life = 310
    for i in range(0,allscores[4]):
        window.blit(life,(x_life,10))
        x_life = x_life + 30

def Movement(): #Movement of the basket and keeping it in the screen (halfway)
    if booleans[6]:
        if movement[0]:
            basket[0][0] -= basket[2]
            movement[0] = False
        if movement[1]:
            basket[0][0] += basket[2]
            movement[1] = False
        if basket[0][0] < -basket[1][0] / 2:
            basket[0][0] = -basket[1][0] / 2
        if basket[0][0] + basket[1][0] > WINDOW_WIDTH + basket[1][0] / 2:
            basket[0][0] = WINDOW_WIDTH - basket[1][0] / 2
    if not booleans[6]: #Movement of basket if the mouse controls are chosen.
        if not booleans[0]:
            basket[0][0] = mouse[0] - 50
        pygame.mouse.set_visible(False)
def Level_Combo_Check(): #This function checks if the player can level up, and updates both level and combos.
    if allscores[2] == allscores[1]: #checking for the level up.
        allscores[0] += 1
        if allscores[1] >= 15:  #adding to required catches to level up
            allscores[1] += 5
        allscores[2] = 0
    if allscores[7] == 5 and allscores[6] < 5: #combo checking
        allscores[6] += 1
        allscores[7] = 1
def EggColisionCheck(): #This function checks if my two eggs are too close for the player to catch just one.
    if abs(egg[0][0] - rotten_egg[0][0]) <= 20 and rotten_egg[0][1] >= egg[0][1]: #checks if the difference of the eggs # is below 20 x pixels and if the rotten egg is above the egg.
        egg[0][0] = random.randint(egg[1],WINDOW_WIDTH - egg[1])
    if abs(egg[0][0] - rotten_egg[0][0]) <= 20 and rotten_egg[0][1] <= egg[0][1]: #same as above but for if the egg is above the rotten egg.
        rotten_egg[0][0] = random.randint(rotten_egg[1],WINDOW_WIDTH - rotten_egg[1])
def EggCatch(an_egg): #This function checks if my basket catches an egg, and says which egg has been caught to the next function.
    if basket[0][0] < an_egg[0][0] + an_egg[1] < basket[0][0] + basket[1][0] and an_egg[0][1] - 3 - allscores[0] < basket[0][1] < an_egg[0][1] + 3 + allscores[0]:
        if an_egg == egg: #If the egg caught is the good egg, the function Positions and score adds combo counter and score.
            booleans[7] = True
        else:
            booleans[8] = True #If the egg is bad, the Positions and score function substracts score and lives.
def PositionsAndScore(an_egg):  # This Function checks if an egg has been caught and adds or removes points depending on if it is a good or a bad egg.
    if booleans[7] == True:  #Checking for a caught (good) egg, adding to combo counter, adding score.
        egg[0][0] = random.randint(an_egg[1],WINDOW_WIDTH - an_egg[1])
        egg[0][1] = -5 #placing egg back at the top when it's been caught.
        allscores[5] += (allscores[0]*allscores[6]) # score is level * combo.
        allscores[2] += 1
        allscores[3] += 1
        allscores[7] += 1
        booleans[7] = False
    elif booleans[8]:  #Checking for a caught (bad)egg, reseting combos, substracting score, and decreasing lives.
        rotten_egg[0][0] = random.randint(rotten_egg[1],WINDOW_WIDTH - an_egg[1])
        rotten_egg[0][1] = -5  #placing the egg back at the top when it's been caught.
        allscores[5] -= (allscores[0]*allscores[6]) # you also lose the level * combo when you catch a rotten egg.
        allscores[6] = 1 #after losing that score, your combo resets to 1.
        allscores[7] = 0
        allscores[4] -= 1
        booleans[8] = False
    if an_egg[0][1] >= WINDOW_HEIGHT: #This portion sets the egg back at the top when they fall off of the screen.
        if an_egg == egg: #This if portion checks if the egg that fell off is a good egg, and substracts a life.
            allscores[4] -= 1
            allscores[6] = 1 #also resets the combo!!
        an_egg[0][0] = random.randint(an_egg[1], WINDOW_WIDTH - an_egg[1])
        an_egg[0][1] = -5 #Setting the y of the egg back to the top.
    if an_egg[0][1] < WINDOW_HEIGHT:
        an_egg[0][1] += 4 + allscores[0]
    if allscores[4] <= 0:
        booleans[10] = True
def DrawAll(): # This Function Draws everything in the pygame window.
    window.fill(black)
    window.blit(background, (0, 0))
    window.blit(baskettop, (basket[0][0], basket[0][1]))
    window.blit(EGG, (egg[0][0] - egg[1] - 5, egg[0][1] - egg[1] - 5))
    window.blit(Regg, (rotten_egg[0][0] - egg_radius - 5, rotten_egg[0][1] - rotten_egg[1] - 5))
    window.blit(menu,(0,0))
    window.blit(comboimg, (0,0))
    window.blit(EggBasket, (basket[0][0], basket[0][1]))
    scoretext = myfont.render(str(allscores[5]), 1, darkred) # rendering my score into a txt
    leveltext = myfont2.render(str(allscores[0]), 1, darkred) # rendering my level into a txt.
    combotext = myfont.render(str(allscores[6]), 1, black) #rendering my combo into a txt.
    window.blit(combotext, (140,55))
    window.blit(scoretext, (220, 3))
    window.blit(scoreimg, (140, 10))
    window.blit(levelimg, (15, 10))
    window.blit(leveltext, (103, 12))
    DrawLives()
clock = pygame.time.Clock() # used to track time within the game (FPS)
quit = False
pygame.key.set_repeat(1)
while not quit: # main program loop
    for event in pygame.event.get(): # check if there were any events
        if event.type == pygame.QUIT: # check if user clicked the upper
            quit = True # right quit button
        if event.type == pygame.KEYDOWN:  # Checking for clicking in the Right or Left key to move basket when keyboard option is active.
            if event.key == pygame.K_LEFT and not booleans[0]:
                movement[0] = True  # saying that movement to the left is happening for function to actually have it happen
            if event.key == pygame.K_RIGHT and not booleans[0]:
                movement[1] = True   # same as above but to the right
            if event.key == pygame.K_r: #Option to restart the game
                ScoreReset()
            if event.key == pygame.K_ESCAPE: #quitting the game through ESC key
                quit = True
            if event.key == pygame.K_p:  # Checking for the button p being pressed.
                pygame.key.set_repeat(0)  # this is here so that pygame only takes my input from "p" once and pause isn't constantly toggled as I press "p".
                if booleans[0]: # if pause is true, then turn pause to false.
                    if not booleans[6]:
                        pygame.mouse.set_pos(mouse)
                    pygame.mouse.set_visible(False)
                    booleans[0] = False
                    pygame.key.set_repeat(1)
                else: # if pause is false, turn pause to true.
                    pygame.mouse.set_visible(True)
                    booleans[0] = True
                    window.blit(PauseMenu,(0,0)) # Drawing the pause menu, I didn't have any interactions with it because its unecessary :V
                    pygame.key.set_repeat(1)
        if event.type == pygame.MOUSEMOTION and not booleans[0]:  # check if event was a mouse motion
            mouse = event.pos
    MenuThings()
    if booleans[2] and not booleans[10]: # If play and not loss
        if not booleans[0]: #if not paused
            DrawAll() #draw everything
            EggCatch(egg) #check for egg being caught
            EggCatch(rotten_egg) #check for rotten egg being caught
            PositionsAndScore(egg) #update score and positions
            PositionsAndScore(rotten_egg) #update score and positions
            Level_Combo_Check() #check for level up and combos
            EggColisionCheck() #check if egg is caught
            Movement() #move basket
    if booleans[10]: #if you have lost.
        AfterLoss() #options after losing
    pygame.display.update() # refresh your display
    clock.tick(60) # wait a certain amount of time that
# ensures a frame rate of 60 fps

pygame.quit() # shutdown module