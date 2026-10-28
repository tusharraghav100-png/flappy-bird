import pygame
import sys
import subprocess
import os
import time

pygame.init()
width , hieght  = 1080 , 720

screen = pygame.display.set_mode((width , hieght))
clock = pygame.time.Clock()
gravity = 10
y = 50
pillarone = 1000
pillartwo = 1000

pillars = []
pillars2 = []








#background
background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background,(1080 , 720))
backgroundrect = background.get_frect(center =(width//2 , hieght//2) )

#bird
bird = pygame.image.load('bird.jpeg')
bird = pygame.transform.scale(bird,(50 , 50))
birdrect = bird.get_frect(topleft = (50,y))
running = True

#upword pillar
pillar = pygame.image.load('pillar.jpeg')
pillar = pygame.transform.scale(pillar,(100 , 300))
pillarrect = pillar.get_frect(center = (pillarone,650))

#downword pillar
pillar2 = pygame.image.load('pillar.jpeg')
pillar2 = pygame.transform.scale(pillar,(100 , 400))
pillarrect2 = pillar.get_frect(center = (pillartwo, -10))

for i in range(1000):
    x2 = 1000 + i *400
    rect2 = pillar2.get_frect(center = (x2 , 100))
    pillars2.append(rect2)

for i in range(1000):
   x =   1000 + i * 400
   rect = pillar.get_frect(topleft = (x , 500))   

   pillars.append(rect)
pygame.mixer.music.load("musicc.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000

    jump = pygame.key.get_pressed()
    if jump[pygame.K_SPACE]:
        y -= 30 




    

    

    y += gravity
    birdrect.y = y

    pillarone -= 10
    pillarrect.x = pillarone

    pillartwo -= 10
    pillarrect2.x = pillartwo

    for rect in pillars:
        rect.x -= 300*dt

    for rect2 in pillars2:
        rect2.x -= 300*dt


    for rect in pillars:
        if birdrect.colliderect(rect):
           
            
            time.sleep(1)

            subprocess.Popen([
                            sys.executable,
                            os.path.join(os.path.dirname(__file__), "gameover.py")
                        ])
            running = False

    for rect2 in pillars2:
            if birdrect.colliderect(rect2):
                subprocess.Popen([
                                sys.executable,
                                os.path.join(os.path.dirname(__file__), "gameover.py")
                            ])
                running = False
            
    
    
    
    screen.blit(background,backgroundrect)
    for rect in pillars:
            screen.blit(pillar,rect)

    for rect2 in pillars2:
        screen.blit(pillar2 , rect2)
    screen.blit(bird, birdrect)
    screen.blit(pillar, pillarrect)
    screen.blit(pillar2 , pillarrect2)
    pygame.display.update()


            


pygame.quit()