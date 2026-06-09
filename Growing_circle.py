import pygame
screen=pygame.display.set_mode((600,600))
screen.fill(('yellow'))
blue=((0,0,255))
red=((255,0,0))
pygame.display.update()

class circle:
    def __init__(self,color,radius,pos,width):
        self.circle_color=color
        self.circle_radius=radius
        self.circle_pos=pos
        self.circle_width=width
        self.circle_surface=screen

    def draw(self):
        self.draw_circle=pygame.draw.circle(self.circle_surface,
                                            self.circle_color,
                                            self.circle_pos,
                                            self.circle_radius,
                                            self.circle_width
                                            )
    
#creating objects
circle1=circle('blue',30,(300,300),20)
circle2=circle('red',70,(100,450),0)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill('yellow')
            circle1.draw()
            circle2.draw()
            pygame.display.update()
