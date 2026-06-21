import pygame
screen=pygame.display.set_mode([800,600])
title=pygame.display.set_caption('My circle')


blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
screen.fill(('white'))
class my_circle:
    def __init__(self,color,pos,radius,width=0):
        self.circle_color=color
        self.circle_pos=pos
        self.circle_radius=radius
        self.circle_width=width
        self.circle_surface=screen

    def draw(self):
        pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_radius,
                                            self.circle_width,
                                            )
        
    def grow(self,r):
        self.circle_radius=self.circle_radius+r
        pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_radius,
                                            self.circle_width
                                            )
        
#creating objects for the class  
circle1=my_circle(blue,(400,400),20)
circle2=my_circle(red,(100,450),15)
circle3=my_circle(green,(200,100),30)

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            circle2.draw()
            circle1.draw()
            circle3.draw()
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            circle1.grow(4)
            circle2.grow(3)
            circle3.grow(2)
            pygame.display.update()
        
        elif event.type == pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            r_circle=my_circle(red,pos,5)
            r_circle.draw()
            pygame.display.update()

        
