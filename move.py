import pygame, random, sys
from pygame.locals import *

class GameMove():
    
    __customes = ("turtle", "prawn", "octopus", "fish", "moray")
    __names = ("_lentorra y petarda_", "_la puta gamba_", "_el jodio manco_", "_payasete mongolete_", "_tripa a rastras_")

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Moviendo un Bichejo")
        
        itemUsed = random.randint(0, 4)                    
        self.__theRunner = Runner(320, 240, self.__customes[itemUsed], self.__names[itemUsed])
            
    def __close(self):
        pygame.quit()
        sys.exit()
            
    def start(self):
        gameOver = False
        while not gameOver:
            
            '''Comprobamos eventos'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.__theRunner.position[1] -= random.randint(10, 50)
                    if event.key == pygame.K_DOWN:
                        self.__theRunner.position[1] += random.randint(10, 50)
                    if event.key == pygame.K_LEFT:
                        self.__theRunner.position[0] -= random.randint(10, 50)
                    if event.key == pygame.K_RIGHT:
                        self.__theRunner.position[0] += random.randint(10, 50)
#                    else:
#                        m1, m2, m3 = pygame.mouse.get_pressed()
#                        if m1 == 1 or m2 == 1:
#                            self.__theRunner.position[0] += random.randint(0, 50)
#                            self.__theRunner.position[1] += random.randint(0, 50)
#                        if m3 == 1:
#                            self.__theRunner.position[0] += random.randint(-50, 0)
#                            self.__theRunner.position[1] += random.randint(-50, 0)
                        
            '''Repintamos todos los objetos'''
            self.background = pygame.image.load("images/background.png")
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.__theRunner.custome, self.__theRunner.position)
            
            '''Renderizamos la pantalla'''
            pygame.display.flip()
        
class Runner():
    
    def __init__(self, x = 0, y = 0, custome = "turtle", name = ""):
        self.custome = pygame.image.load("images/{}.png".format(custome))
        self.position = [x, y]
        self.name = name

if __name__ == "__main__":
    pygame.init()
    moverBicho = GameMove()
    moverBicho.start()