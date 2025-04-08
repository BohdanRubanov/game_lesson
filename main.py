# бібліотека для створення ігор
import pygame
# бібліотека для знаходження шляху
import os

# задаємо базові налаштування, писати обов'язково на початку кожного проекту 
pygame.init()
# створюємо екран і задаємо розміри
screen = pygame.display.set_mode((1200, 800))
# даємо назву вікна
pygame.display.set_caption("pardon")
# 





# створюємо класс для налаштувань 
class Settings:
    # метод конструктор де ми задаємо всі властивості об'єкта
    def __init__(self, width, height, x, y, name_image):
        # поле ширини нашого об'єкта
        self.WIDTH = width
        # поле висоти
        self.HEIGHT = height
        # поля координат 
        self.X=x
        self.Y=y
        # назва картинки
        self.NAME_IMAGE=name_image
        self.IMAGE = None
        self.load_image()
    
    def load_image(self):
        path= os.path.abspath(__file__ + "/..")
        path= os.path.join(path, self.NAME_IMAGE)
        self.IMAGE = pygame.image.load(path)
        self.IMAGE= pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
        self.IMAGE= pygame.transform.flip(self.IMAGE, True, True)
    
    def draw_image(self):
        screen.blit(self.IMAGE,(self.X,self.Y))


bruh=Settings(width=150, height=150, x=150, y = 0, name_image="image.png")   


game = True 
while game == True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          game = False
          pygame.quit()
    screen.fill((255,100,0))
    bruh.draw_image()
              
      
 
    pygame.display.flip()




