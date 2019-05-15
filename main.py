import pygame, random, sys

class GameRace():
    
    runners = []
    __posYs = (152, 196, 243, 288, 382)
    __customes = ("turtle", "prawn", "octopus", "fish", "moray")
    __names = ("_lentorra y petarda_", "_la puta gamba_", "_el jodio manco_", "_payasete mongolete_", "_tripa a rastras_")
    __start = 5
    __finish = 635
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("La Carrera Infernal de los Bichejos")
        
        used = []
        for i in range(4):
            isNotUsed = False
            while not isNotUsed:
                alreadyUsed = random.randint(0, 4)
                if alreadyUsed not in used:
                    used.append(alreadyUsed)
                    isNotUsed = True
                    
            self.runners.append(Runner(self.__start, self.__posYs[i], self.__customes[used[i]], self.__names[used[i]]))
            
    def __close(self):
        pygame.quit()
        sys.exit()
            
    def match(self):
        gameOver = False
        while not gameOver:
            
            '''Comprobación de eventos'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
            
            '''Pasamos un turno de la carrera. Movemos los objetos. Y si alguno gana...'''
            for runner in self.runners:
                runner.run()
                
                if runner.position[0] >= self.__finish:
                    pygame.display.set_caption("La Carrera Infernal de los Bichejos " + " ...and the WINNER is ... {}".format(runner.name.upper()))
                    gameOver = True
                    break
            
            '''Repintamos todos los objetos'''
            self.background = pygame.image.load("images/background.png")
            self.__screen.blit(self.background, (0, 0))
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            '''Renderizado de pantalla'''
            pygame.display.flip()
            
        '''Para que la pantalla no desaparezca en el instante en el que acaba la carrera, obligamos a pygame a que siga comprobando eventos'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
        
class Runner():
    
    def __init__(self, x = 0, y = 0, custome = "turtle", name = ""):
        self.custome = pygame.image.load("images/{}.png".format(custome))
        self.position = [x, y]
        self.name = name
        
    def run(self):
        self.position[0] += random.randint(1, 6)

if __name__ == "__main__":
    pygame.init()
    miJuegodeCarreras = GameRace()
    miJuegodeCarreras.match()