import pygame
WIDTH=650
HEIGHT=600
title=pygame.display.set_caption("Bulb simulater")
screen=pygame.display.set_mode()
screen.fill('white')
pygame.display.update()

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            img=pygame.image.load("bulb_simulater/BulbOff.jpg")
            resize_img=pygame.transform.scale(img,(400,600))
            screen.blit(resize_img,(600,100))
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            img2=pygame.image.load("bulb_simulater/BulbOn.jpg")
            resize_img2=pygame.transform.scale(img2,(400,600))
            screen.blit(resize_img2,(600,100))
            pygame.display.update()





