import pygame,time
pygame.init()
WIDTH=800
HEIGHT=600
output_screen=pygame.display.set_mode()
title=pygame.display.set_caption('Birthday card')

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

    img=pygame.image.load('birthday_card/images/Backgroundone.jpg')
    image=pygame.transform.scale(img,(WIDTH,HEIGHT))
    font=pygame.font.SysFont('Pacific',70)
    text=font.render('HAPPY',True,(100,155,0),'blue')
    text2=font.render('BIRTHDAY!!',True,(100,0,155))

    output_screen.fill((255,255,255))
    output_screen.blit(image,(0,0))
    output_screen.blit(text,(300,150))
    output_screen.blit(text2,(250,300))
    pygame.display.update()
    time.sleep(2)

   # position

    img=pygame.image.load('birthday_card/images/cake.jpg')
    image=pygame.transform.scale(img,(WIDTH,HEIGHT))
    font=pygame.font.SysFont('Lobster',70)
    text=font.render('Happy',True,(0,0,0),'pink')
    text2=font.render('Birthday!!',True,(0,0,0),'pink')

    output_screen.fill((255,255,255))
    output_screen.blit(image,(0,0))
    output_screen.blit(text,(300,300))
    output_screen.blit(text2,(250,400))
    pygame.display.update()
    time.sleep(2)

    #gift
    img=pygame.image.load('birthday_card/images/gift.jpg')
    image=pygame.transform.scale(img,(WIDTH,HEIGHT))
    font=pygame.font.SysFont('Pacific',120)
    text=font.render('HAPPY',True,(75,75,105))
    text2=font.render('BIRTHDAY',True,(75,75,105))

    output_screen.fill((255,255,255))
    output_screen.blit(image,(0,0))
    output_screen.blit(text,(150,150))
    output_screen.blit(text2,(100,300))
    pygame.display.update()
    time.sleep(2)
