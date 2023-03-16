import pygame, sys, random
from pygame.locals import *


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption('CHRISTMAS MINI GAMES')

black = (0,0,0)
burgundy = (128, 0, 32)
green = (71, 148, 58)
yellow = (255,223,0)
red = (255,0,0)
brown = (150, 75, 0)
blue = (0,0,255)
white = (255,255,255)
cream = (255, 253, 208)
grey = (128, 128, 128)
dark_grey = (54,55,55)
brown = (189,154,122)
darker_brown = (169,134,102)
dark_brown = (92,64,51)
dark_red = (178,34,34)

game1_button = pygame.Rect(100, 300, 100, 190)

font = pygame.font.Font(None, 25)
title_font = pygame.font.Font(None,75)

global bow
bow = pygame.image.load('bow.png')
bow = pygame.transform.scale(bow,(40,40))

def main_menu():
    click = False
    while True:
        
        mx, my = pygame.mouse.get_pos()
        if game1_button.collidepoint((mx, my)) and click:
            game1menu()

        screen.fill(burgundy)
        pygame.draw.ellipse(screen, red, (75,475,600,25))
        pygame.draw.ellipse(screen, black, (75,475,600,25),3)
        pygame.draw.polygon(screen, green,((375,70),(300,180),(450,180)))
        pygame.draw.polygon(screen,yellow,((375,40),(383,55),(398,55),(386,69),(394,86),(375,74),(356,86),(366,69),(351,55),(367,55)))
        pygame.draw.polygon(screen, green,((375,130),(275,250),(475,250)))
        pygame.draw.polygon(screen, green,((375,175),(255,325),(495,325)))
        pygame.draw.polygon(screen, green,((375,225),(230,400),(520,400)))
        pygame.draw.rect(screen,brown,(350,400,50,90))
        pygame.draw.circle(screen,red,(320,300),15)
        pygame.draw.circle(screen,red,(380,350),15)
        pygame.draw.circle(screen,red,(357,242),15)
        pygame.draw.circle(screen,red,(412,290),15)
        pygame.draw.circle(screen,red,(376,175),15)

        pygame.draw.rect(screen,red,game1_button)

        screen.blit(bow,(130,290))

        screen.blit(font.render("Game 1", True, black), (115, 380))
        screen.blit(title_font.render("Christmas         Mini Games",True, white), (50,50))
       
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if game1_button.collidepoint((mx, my)):
                    click = True
        pygame.display.update()


def game1menu():

    play_button = pygame.Rect(450, 250, 100, 100)
    back_button = pygame.Rect(175, 250, 100, 100)

    while True:

        mx, my = pygame.mouse.get_pos()

        screen.fill(black)
        screen.blit(title_font.render("MISSION:", True, white), (50, 100))
        screen.blit(font.render("Match the correct present sizes to the gifts", True, white), (50, 175))
        screen.blit(font.render("BACK", True, white), (200, 350))
        screen.blit(font.render("PLAY", True, white), (475, 350))
        pygame.draw.polygon(screen, white,((450, 250), (450, 350), (550, 300)))
        pygame.draw.polygon(screen, white,((275, 250), (275, 350), (175, 300)))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if play_button.collidepoint((mx, my)):
                    game_1()
                if back_button.collidepoint((mx, my)):
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
        pygame.display.update()


def game_1():
    
    bike = pygame.image.load('bike.png')
    bike = pygame.transform.scale(bike,(240,151.375))
    bike = pygame.transform.rotate(bike, 1)
    bat = pygame.image.load('bat.png')
    bat = pygame.transform.scale(bat,(100,80.875))
    bat = pygame.transform.rotate(bat,52)
    ball = pygame.image.load('ball.png')
    ball = pygame.transform.scale(ball,(85,85))
    flute = pygame.image.load('flute.png')
    flute = pygame.transform.scale(flute,(84,84))
    flute = pygame.transform.rotate(flute,8)
    ring = pygame.image.load('ring.png')
    ring = pygame.transform.scale(ring,(25,25))
    mug = pygame.image.load('mug.png')
    mug = pygame.transform.scale(mug,(47.5,52.5))
    mixer = pygame.image.load('mixer.png')
    mixer = pygame.transform.scale(mixer,(200,200))
    mixer = pygame.transform.rotate(mixer,-.5)

    x_list = [-250,-500,-750,-1000,-1250,-1500,-1750]
    random.shuffle(x_list)

    present_list = [475,40,260,150]
    present2_list = [395,45,35,145]
    present3_list = [270,51,85,85]
    present4_list = [270,170,85,20]
    present5_list = [200,51,25,25]
    present6_list = [189,130,48,60]
    present7_list = [45,50,115,140]
    
    present_clicked = False
    present2_clicked = False
    present3_clicked = False
    present4_clicked = False
    present5_clicked = False
    present6_clicked = False
    present7_clicked = False

    bike_wrapped = False
    bat_wrapped = False
    ball_wrapped = False
    flute_wrapped = False
    ring_wrapped = False
    mug_wrapped = False
    mixer_wrapped = False

    while True:

        x_list[0] += 0.25
        if bike_wrapped == True:
            present_list[0] += 0.25
        x_list[1] += 0.25
        if bat_wrapped == True:
            present2_list[0] += 0.25
        x_list[2] += 0.25
        if ball_wrapped == True:
            present3_list[0] += 0.25
        x_list[3] += 0.25
        if flute_wrapped == True:
            present4_list[0] += 0.25
        x_list[4] += 0.25
        if ring_wrapped == True:
            present5_list[0] += 0.25
        x_list[5] += 0.25
        if mug_wrapped == True:
            present6_list[0] += 0.25
        x_list[6] += 0.25
        if mixer_wrapped == True:
            present7_list[0] += 0.25
    
        bike_button = pygame.Rect(x_list[0],300,240,151.375)
        bat_button = pygame.Rect(x_list[1],327,100,80.875)
        ball_button = pygame.Rect(x_list[2],369,85,85)
        flute_button = pygame.Rect(x_list[3],403,84,84)
        ring_button = pygame.Rect(x_list[4],426,25,25)
        mug_button = pygame.Rect(x_list[5],399,47.5,52.5)
        mixer_button = pygame.Rect(x_list[6],284,200,200)

        present = pygame.Rect(present_list[0],present_list[1],present_list[2],present_list[3])
        present2 = pygame.Rect(present2_list[0],present2_list[1],present2_list[2],present2_list[3])
        present3 = pygame.Rect(present3_list[0],present3_list[1],present3_list[2],present3_list[3])
        present4 = pygame.Rect(present4_list[0],present4_list[1],present4_list[2],present4_list[3])
        present5 = pygame.Rect(present5_list[0],present5_list[1],present5_list[2],present5_list[3])
        present6 = pygame.Rect(present6_list[0],present6_list[1],present6_list[2],present6_list[3])
        present7 = pygame.Rect(present7_list[0],present7_list[1],present7_list[2],present7_list[3])

        mx, my = pygame.mouse.get_pos()
        if present_clicked:
                present_list[0] = mx - present_list[2]/2
                present_list[1] = my - present_list[3]/2
        if present2_clicked:
                present2_list[0] = mx - present2_list[2]/2
                present2_list[1] = my - present2_list[3]/2
        if present3_clicked:
                present3_list[0] = mx - present3_list[2]/2
                present3_list[1] = my - present3_list[3]/2
        if present4_clicked:
                present4_list[0] = mx - present4_list[2]/2
                present4_list[1] = my - present4_list[3]/2
        if present5_clicked:
                present5_list[0] = mx - present5_list[2]/2
                present5_list[1] = my - present5_list[3]/2
        if present6_clicked:
                present6_list[0] = mx - present6_list[2]/2
                present6_list[1] = my - present6_list[3]/2
        if present7_clicked:
                present7_list[0] = mx - present7_list[2]/2
                present7_list[1] = my - present7_list[3]/2

        if x_list[0] > 750 and bike_wrapped == False:
            game1outcome("FAILED","You failed to wrap the bicycle")
        if x_list[1] > 750 and bat_wrapped == False:
            game1outcome("FAILED","You failed to wrap the baseball bat")
        if x_list[2] > 750 and ball_wrapped == False:
            game1outcome("FAILED","You failed to wrap the basketball")
        if x_list[3] > 750 and flute_wrapped == False:
            game1outcome("FAILED","You failed to wrap the flute")
        if x_list[4] > 750 and ring_wrapped == False:
            game1outcome("FAILED","You failed to wrap the diamond ring")
        if x_list[5] > 750 and mug_wrapped == False:
            game1outcome("FAILED","You failed to wrap the mug")
        if x_list[6] > 750 and mixer_wrapped == False:
            game1outcome("FAILED","You failed to wrap the kitchen mixer")

        if x_list[0] > 750 and x_list[1] > 750 and x_list[2] > 750 and x_list[3] > 750 and x_list[4] > 750 and x_list[5] > 750 and x_list[6] > 750:
            game1outcome("COMPLETED","You successfully wrapped all the gifts")

        screen.fill(cream)
       
        pygame.draw.rect(screen,grey,(0,250,100,275))
        pygame.draw.rect(screen,dark_grey,(50,275,50,225))
        for x_offset in range(50,800,50):
            pygame.draw.circle(screen,black,(x_offset,462.5),12.5)
        pygame.draw.line(screen,black,(50,452),(750,452),5)
        pygame.draw.line(screen,black,(50,472),(750,472),5)
        pygame.draw.rect(screen,grey,(50,475,50,25))
        for x_offset in range(145,750,150):
            pygame.draw.rect(screen,black,(x_offset,475,10,25))
            pygame.draw.polygon(screen,black,((x_offset,490),(x_offset-20,500),(x_offset+30,500),(x_offset+10,490)))
        pygame.draw.rect(screen,dark_brown,(25,0,750,200))
        pygame.draw.rect(screen,brown,(25,0,750,200),10)
        pygame.draw.rect(screen,darker_brown,(100,200,650,20))
        pygame.draw.polygon(screen,darker_brown,((25,200),(100,200),(100,220)))
        pygame.draw.line(screen,brown,(450,0),(450,199),10)
        pygame.draw.line(screen,brown,(375,0),(375,199),10)
        pygame.draw.line(screen,brown,(250,0),(250,199),10)
        pygame.draw.line(screen,brown,(250,140),(375,140),10)
        pygame.draw.line(screen,brown,(175,0),(175,199),10)
        pygame.draw.line(screen,brown,(175,80),(250,80),10)


        screen.blit(bike,(x_list[0],300))
        screen.blit(bat,(x_list[1],327))
        screen.blit(ball,(x_list[2],369))
        screen.blit(flute,(x_list[3],403))
        screen.blit(ring,(x_list[4],426))
        screen.blit(mug,(x_list[5],399))
        screen.blit(mixer,(x_list[6],284))

        draw_presents(present_list[0],present_list[1],present_list[2],present_list[3],red,60)
        draw_presents(present2_list[0],present2_list[1],present2_list[2],present2_list[3],green,40)
        draw_presents(present3_list[0],present3_list[1],present3_list[2],present3_list[3],yellow,40)
        draw_presents(present4_list[0],present4_list[1],present4_list[2],present4_list[3],blue,20)
        draw_presents(present5_list[0],present5_list[1],present5_list[2],present5_list[3],green,20)
        draw_presents(present6_list[0],present6_list[1],present6_list[2],present6_list[3],red,20)
        draw_presents(present7_list[0],present7_list[1],present7_list[2],present7_list[3],blue,40)

        pygame.draw.rect(screen,grey,(0,250,50,275))
    

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if bike_wrapped == False:
                    if present.collidepoint((mx, my)):
                        if present_clicked == True:
                            present_clicked = False
                            if bike_button.collidepoint((mx,my)):
                                present_list[0] = x_list[0]
                                present_list[1] = 301
                                bike_wrapped = True
                            elif bat_button.collidepoint((mx,my)) or ball_button.collidepoint((mx,my)) or flute_button.collidepoint((mx,my)) or ring_button.collidepoint((mx,my)) or mug_button.collidepoint((mx,my)) or mixer_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else:
                                present_list = [475,40,260,150]
                        else:
                            present_clicked = True
                if bat_wrapped == False:
                    if present2.collidepoint((mx, my)):
                        if present2_clicked == True:
                            present2_clicked = False
                            if bat_button.collidepoint((mx,my)):
                                present2_list[0] = x_list[1] + 45
                                present2_list[1] = 305
                                bat_wrapped = True
                            elif bike_button.collidepoint((mx,my)) or ball_button.collidepoint((mx,my)) or flute_button.collidepoint((mx,my)) or ring_button.collidepoint((mx,my)) or mug_button.collidepoint((mx,my)) or mixer_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else:
                                present2_list = [395,45,35,145]
                        else:
                            present2_clicked = True
                if ball_wrapped == False:
                    if present3.collidepoint((mx, my)):
                        if present3_clicked == True:
                            present3_clicked = False
                            if ball_button.collidepoint((mx,my)):
                                present3_list[0] = x_list[2]
                                present3_list[1] = 365
                                ball_wrapped = True
                            elif bike_button.collidepoint((mx,my)) or bat_button.collidepoint((mx,my)) or flute_button.collidepoint((mx,my)) or ring_button.collidepoint((mx,my)) or mug_button.collidepoint((mx,my)) or mixer_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else: 
                                present3_list = [270,51,85,85]
                        else:
                            present3_clicked = True
                if flute_wrapped == False:
                    if present4.collidepoint((mx, my)):
                        if present4_clicked == True:
                            present4_clicked = False
                            if flute_button.collidepoint((mx,my)):
                                present4_list[0] = x_list[3] + 5
                                present4_list[1] = 430
                                flute_wrapped = True
                            elif bike_button.collidepoint((mx,my)) or bat_button.collidepoint((mx,my)) or ball_button.collidepoint((mx,my)) or ring_button.collidepoint((mx,my)) or mug_button.collidepoint((mx,my)) or mixer_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else:
                                present4_list = [270,170,85,20]
                        else:
                            present4_clicked = True
                if ring_wrapped == False:
                    if present5.collidepoint((mx, my)):
                        if present5_clicked == True:
                            present5_clicked = False
                            if ring_button.collidepoint((mx,my)):
                                present5_list[0] = x_list[4]
                                present5_list[1] = 425
                                ring_wrapped = True
                            elif bike_button.collidepoint((mx,my)) or bat_button.collidepoint((mx,my)) or ball_button.collidepoint((mx,my)) or flute_button.collidepoint((mx,my)) or mug_button.collidepoint((mx,my)) or mixer_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else:
                                present5_list = [200,51,25,25]
                        else:
                            present5_clicked = True
                if mug_wrapped == False:
                    if present6.collidepoint((mx, my)):
                        if present6_clicked == True:
                            present6_clicked = False
                            if mug_button.collidepoint((mx,my)):
                                present6_list[0] = x_list[5]
                                present6_list[1] = 390
                                mug_wrapped = True
                            elif bike_button.collidepoint((mx,my)) or bat_button.collidepoint((mx,my)) or ball_button.collidepoint((mx,my)) or flute_button.collidepoint((mx,my)) or ring_button.collidepoint((mx,my)) or mixer_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else:
                                present6_list = [189,130,48,60]
                        else:
                            present6_clicked = True
                if mixer_wrapped == False:
                    if present7.collidepoint((mx, my)):
                        if present7_clicked == True:
                            present7_clicked = False
                            if mixer_button.collidepoint((mx,my)):
                                present7_list[0] = x_list[6] + 44
                                present7_list[1] = 311
                                mixer_wrapped = True
                            elif bike_button.collidepoint((mx,my)) or bat_button.collidepoint((mx,my)) or ball_button.collidepoint((mx,my)) or flute_button.collidepoint((mx,my)) or ring_button.collidepoint((mx,my)) or mug_button.collidepoint((mx,my)):
                                game1outcome("FAILED","The present you chose does not match the gift")
                            else:
                                present7_list = [45,50,115,140]
                        else:
                            present7_clicked = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
        pygame.display.update()

def draw_presents(present_x,present_y,width,length,colour,bow_dimension):
    global bow
    pygame.draw.rect(screen,colour,(present_x,present_y,width,length))
    pygame.draw.rect(screen,dark_red,(present_x + width/2-width/24,present_y,width/8,length))
    pygame.draw.rect(screen,dark_red,(present_x,present_y + length/2-width/24,width,width/8))
    bow = pygame.transform.scale(bow,(bow_dimension,bow_dimension))
    screen.blit(bow,(present_x + width/2 - bow_dimension/2,present_y - bow_dimension/2 + bow_dimension/4))


def game1outcome(outcome,why):
    play_button = pygame.Rect(450, 250, 100, 100)
    back_button = pygame.Rect(175, 250, 100, 100)
    while True:
        mx, my = pygame.mouse.get_pos()
        if outcome == "COMPLETED":
            screen.fill(green)
        else:
            screen.fill(red)
        screen.blit(title_font.render(f"MISSION {outcome}!", True, white), (50, 100))
        screen.blit(font.render(why, True, white), (50, 175))
        screen.blit(font.render("MENU", True, white), (200, 350))
        screen.blit(font.render("REPLAY", True, white), (475, 350))
        pygame.draw.polygon(screen, white,((450, 250), (450, 350), (550, 300)))
        pygame.draw.polygon(screen, white,((275, 250), (275, 350), (175, 300)))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if play_button.collidepoint((mx, my)):
                    game_1()
                if back_button.collidepoint((mx, my)):
                    main_menu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
