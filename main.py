import pygame
import os

#
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("pardon")
# 





#
class Settings:
    def __init__(self, width, height, x, y, name_image):
        self.WIDTH = width
        self.HEIGHT = height 
        self.X=x
        self.Y=y
        self.NAME_IMAGE=name_image
        self.IMAGE = None
    
    def load_image(self):
        path= os.path.abspath(__file__ + "/..")
        path= os.path.join(path, self.NAME_IMAGE)
        self.IMAGE = pygame.image.load(path)
        self.IMAGE= pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
        self.IMAGE= pygame.transform.flip(self.IMAGE, True, True)




game = True 
while game == True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          game = False
          pygame.quit()
    screen.fill((255,100,0))
    screen.blit(image,(150,150))          
      
 
    pygame.display.flip()

# class Player:
#     def __init__(self, hair):
#        self.HAIR = hair

# vania = Player("short hair")
# sasha= Player("long hair")

# print(vania.HAIR)
# print(sasha.HAIR)





