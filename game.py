import pygame
import time
import random

pygame.init()

disp_w = 800
disp_h = 600
car_width = 140

red   = (255,0,0)
black = (0,0,0)
block_color = (63,115,255)

gd = pygame.display.set_mode((disp_w,disp_h))

pygame.display.set_caption("Racey")

clock = pygame.time.Clock()

carimg = pygame.image.load('car.png')

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged : "+str(count),True,black)
    gd.blit(text,(0,3));

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gd , color , [thingx,thingy,thingw,thingh])
    
def car(x,y):
    gd.blit(carimg,(x,y))    

def crash():
    message_display("You Crashed !!!")

def message_display(text):
    str1 =pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text,str1)
    TextRect.center = ((disp_w/2),(disp_h/2))
    gd.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()
    

def game_loop():
    x=(disp_w * 0.45)
    y=(disp_h * 0.8)
    x_chng = 0

    thing_startx = random.randrange(0,disp_w)
    thing_starty = -600
    thing_speed = 4
    thing_width = 80
    thing_height = 50

    gameExit=False

    dodged = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_chng=-5
                elif event.key == pygame.K_RIGHT:    
                    x_chng=5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_chng=0
                    
        x+=x_chng

        gd.fill(red)

        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty += thing_speed

        car(x,y)

        things_dodged(dodged)
        
        if x > disp_w - car_width or x<0:
            crash()

        if(thing_starty > disp_h):
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,disp_w)
            dodged += 1
            thing_speed += 1
            #thing_width += dodged*1.2

        if(y < thing_starty + thing_height):
            # print("Y CrossOver !")
            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width :
                crash()
    
        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()

quit()

            

            
