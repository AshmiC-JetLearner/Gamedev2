import pygame
screen=pygame.display.set_mode((800,600))
title=pygame.display.set_caption('My circle')
screen.fill(('white'))
pygame.display.update()
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

class my_circle:
    def __init__(self,color,pos,radius,width=0):
        self.circle_color=color
        self.circle_pos=pos
        self.circle_radius=radius
        self.circle_width=width
        self.circle_surface=screen

    def draw(self):
        self.draw.circle=pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_radius,
                                            self.circle_width,
                                            )
        
    def grow(self,r):
        self.circle_radius=self.circle_radius+r
        self.draw.circle=pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_radius,
                                            self.circle_width
                                            )
        
    
circle1=()



