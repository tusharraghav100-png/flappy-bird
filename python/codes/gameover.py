import  pygame
import sys
import subprocess
import os

pygame.init()
WIDDTH,HEIGGTH = 1080 , 720
menu = pygame.display.set_mode((WIDDTH,HEIGGTH))
back = pygame.image.load('blur.png')
back = pygame.transform.scale(back,(1080 , 720))
backrect = back.get_frect(center = (WIDDTH//2,HEIGGTH//2))

resume = pygame.Surface((300 , 50))
resume.fill('green')
resumerect = resume.get_frect(center =(WIDDTH//2,HEIGGTH//2))

border = pygame.Surface((500 , 500))
border.fill('yellow')
borderect = border.get_frect(center =(WIDDTH//2,HEIGGTH//2))

font = pygame.font.Font(pygame.font.get_default_font(), 45)
label = font.render("RESTART", True, 'black')
laBEL2 = font.render("GAME OVER" , True , 'blue')
pygame.mixer.music.load("out.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
runnung = True
while runnung:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            runnung = False

    
    if events.type == pygame.MOUSEBUTTONDOWN:
        if resumerect.collidepoint(events.pos):
            subprocess.Popen([
                sys.executable,
                os.path.join(os.path.dirname(__file__), "python.py")
            ])
            runnung = False

    
    menu.blit(back , backrect)
    menu.blit(border , borderect)
    menu.blit(resume , resumerect)
    menu.blit(label,(450,340))
    menu.blit(laBEL2 , (380, 50))
    pygame.display.update()
pygame.quit()

        