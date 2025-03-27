import pygame
import os

#
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("pardon")
# 

path= os.path.abspath(__file__ + "/..")
path= os.path.join(path,"image.png")

image = pygame.image.load(path)
image= pygame.transform.scale(image,(200,200))
image= pygame.transform.flip(image, True, True)



#
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





