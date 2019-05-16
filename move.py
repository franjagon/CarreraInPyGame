'''Importamos las librerías -random-, para poder invocar valores aleatorios, -sys-, para poder invocar la salida de la interfaz y -pygame-.'''
'''Importamos la librería de variables locales de PYGAME, para poder invocar sus códigos de identificación para las teclas, el ratón, etc...'''
'''Importamos nuestro programa main para poder usar su clase Runner.'''
import random, sys, pygame
from pygame.locals import *
import main as M

'''Nuestra clase principal (objeto) será un juego en el que podremos mover a nuestra elección un ítem (bicho).'''
class GameMove():    
    '''Los atributos (todos privados) no se podran ni getear si setear, serán fijos ya que se corresponderán con imágenes no mutables.'''
    __customes = ("turtle", "prawn", "octopus", "fish", "moray")
    __names = ("_lentorra y petarda_", "_la puta gamba_", "_el jodio manco_", "_payasete mongolete_", "_tripa a rastras_")
    
    '''El método constructor no recibirá valores. Se encargará de definir la base de la ventana de ejecución y de generar un ítem para que lo movamos.'''
    def __init__(self):
        '''Lo primero es definir la pantalla. Fijamos su tamaño y su imagen de fondo.'''
        self.__screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("images/background.png")
        
        '''En las tuplas fijas e indexadas de la clase tenemos los disfraces y nombres de los posibles bichos para elegir.
           Generamos un bicho, instanciando la clase Runner de main.
           Pasamos una posición inicial X e Y centrada en la pantalla y el disfraz y nombre que nos salga generando un índice de forma aleatoria para las tuplas.
           Una vez conocemos nuestro bicho, le ponemos un título personalizado a la ventana de ejecución.'''        
        itemUsed = random.randint(0, 4)                    
        self.__theBug = M.Runner(320, 240, self.__customes[itemUsed], self.__names[itemUsed])
        pygame.display.set_caption("Moviendo a {}".format(self.__theBug.name.upper()))
 
    '''Definimos un método para cerrar la aplicación de forma más elegante.'''
    def __close(self):
        pygame.quit()
        sys.exit()

    '''Este método será el que inicie nuestro juego.'''
    def start(self):
        '''Lanzamos un bucle infinito, ya que nuestro juego solo acabará si decidimos finalizarlo con el botón que cierra la ventana terminando la ejecución.'''
        while True:            
            '''Comprobamos los eventos. En nuestro caso, este paso es también la ejecución del código del juego, ya que moveremos el bicho pulsando teclas o los botones del ratón.
               El primero, el cierre de ventana.
               Después las posibles pulsaciones de las teclas de dirección, incrementando o decrementando las coordenadas X e Y de posición del bicho.
               Por último, los posibles clicks de los botones del ratón, que derivarán en un movimiento aleatorio del bicho en cualquier dirección.'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.__theBug.position[1] -= random.randint(10, 50)
                    if event.key == pygame.K_DOWN:
                        self.__theBug.position[1] += random.randint(10, 50)
                    if event.key == pygame.K_LEFT:
                        self.__theBug.position[0] -= random.randint(10, 50)
                    if event.key == pygame.K_RIGHT:
                        self.__theBug.position[0] += random.randint(10, 50)
                elif event.type == MOUSEBUTTONDOWN:
                    self.__theBug.position[0] += random.randint(-50, 50)
                    self.__theBug.position[1] += random.randint(-50, 50)
                        
            '''Redibujamos todos los objetos. Lo primero la imagen de fondo de la ventana y después el bicho (en su posición actualizada).'''
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.__theBug.custome, self.__theBug.position)
            
            '''Renderizamos la pantalla'''
            pygame.display.flip()

'''Nuestra ejecución como programa principal iniciará el framework de PYGAME, instanciará un objeto "juego de mover el bicho" e invocará su metodo empezar para que se inicie la ejecución.'''
if __name__ == "__main__":
    pygame.init()
    moverBicho = GameMove()
    moverBicho.start()
