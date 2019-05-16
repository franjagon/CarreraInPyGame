'''Importamos las librerías -random-, para poder invocar valores aleatorios, -sys-, para poder invocar la salida de la interfaz y -pygame-.'''
import random, sys, pygame

'''Nuestra clase principal (objeto) será la carrera propiamente dicha.'''
class GameRace():
    '''Los atributos (todos privados) no se podran ni getear si setear, serán fijos ya que se corresponderán con imágenes no mutables.'''
    __runners = []
    __posYs = (152, 196, 243, 288, 382)
    __customes = ("turtle", "prawn", "octopus", "fish", "moray")
    __names = ("_lentorra y petarda_", "_la puta gamba_", "_el jodio manco_", "_payasete mongolete_", "_tripa a rastras_")
    __start = 5
    __finish = 635
    
    '''El método constructor no recibirá valores. Se encargará de definir la base de la ventana de ejecución y de generar los corredores.'''
    def __init__(self):
        '''Lo primero (para poder montar una aplicación con PYGAME) es definir la pantalla. Fijamos su tamaño, su imagen de fondo y su título.'''
        self.__screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("images/background.png")
        pygame.display.set_caption("La Carrera Infernal de los Bichejos")
        
        '''En las tuplas fijas e indexadas de la clase tenemos las posiciones Y de cada corredor, sus disfraces (imágenes) y sus nombres.
           Definimos un número de 4 corredores que serán elegidos para colocarse en la línea de salida calle a calle.
           Para ello generamos una lista vacía que se irá llenando con los índices de los corredores elegidos para la carrera de forma aleatoria.'''
        used = []
        for i in range(4):
            '''En cada iteración generamos un número aleatorio de 0 a 4 (5 posibilidades). Si el número no está en la lista de usados, lo añadimos y lo tomamos como índice.'''
            isNotUsed = False
            while not isNotUsed:
                alreadyUsed = random.randint(0, 4)
                if alreadyUsed not in used:
                    used.append(alreadyUsed)
                    isNotUsed = True
                    
            '''Tomando el índice (obtenido aleatoriamente y no utilizado hasta el momento), invocamos una instancia de la clase Runner y la sumamos a nuestra lista de corredores.'''
            self.__runners.append(Runner(self.__start, self.__posYs[i], self.__customes[used[i]], self.__names[used[i]]))
    
    '''Definimos un método para cerrar la aplicación de forma más elegante.'''
    def __close(self):
        pygame.quit()
        sys.exit()
    
    '''Este método se encargará de ejecutar la partida (la carrera). El ciclo de vida (bucle) obligatorio de PYGAME es:
           (1)  Revisar los eventos y actuar si alguno ha sucedido.
           (2)  Ejecutar el código de la aplicaión.
           (3)  Redibujar todos los elementos gráficos en la ventana de ejecución.
           (4)  Refrescar con el redibujado la pantalla (renderizar).'''
    def match(self):
        '''Definimos la condición de salida del bucle como el final de la partida (a False de inicio) y lanzamos el bucle para la consecución de la misma.'''
        gameOver = False
        while not gameOver:            
            '''(1)  Comprobamos los eventos.
               En nuestro caso no interactuaremos en la partida, así que el unico evento al que estaremos atentos será el click sobre el botón de cerrar la pantalla.
               En caso de darse cerraremos la ventana dando por terminada la ejecución (esté como esté la partida).'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
            
            '''(2)  El código de nuestra aplicación serán los turnos de avance de los corredores.'''
            for runner in self.__runners:
                '''En cada turno iremos iterando los corredores (invocando el método run de la clase Runner).'''
                runner.run()
                
                '''Tras avanzar un corredor, revisaremos si ha llegado a la meta.
                   Y si es así daremos el mensaje del ganador (en el título de la ventana) y activaremos la condición de final de partida.
                   Y forzaremos la salida del bucle para que ningún otro corredor pueda ya llegar a la meta.'''
                if runner.position[0] >= self.__finish:
                    pygame.display.set_caption("La Carrera Infernal de los Bichejos " + " ...and the WINNER is ... {}".format(runner.name.upper()))
                    gameOver = True
                    break
            
            '''(3)  Redibujamos todos los objetos. Lo primero la imagen de fondo de la ventana. Y después (iterándolos) cada uno de los corredores.'''
            self.__screen.blit(self.background, (0, 0))
            for runner in self.__runners:
                self.__screen.blit(runner.custome, runner.position)
            
            '''(4)  Por último, renderizamos la pantalla. Que es cuando realmente se recolocan en ella todos sus elementos en sus posiciones recalculadas.'''
            pygame.display.flip()
            
        '''Una vez acaba la partida, para que la pantalla no se cierre en ese mismo instante, lanzamos un bucle infinito en el que únicamente atenderemos (y del que sólo
           saldremos con) el click sobre el botón de cerrar la pantalla, para finalizar definitivamente.'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
                    
'''Esta clase será el objeto corredor.'''        
class Runner():
    '''El método constructor recibirá obligatoriamente los valores para establecer una posición inicial para el corredor y opcionalmente un disfraz y un nombre.'''
    def __init__(self, x = 0, y = 0, custome = "turtle", name = ""):
        self.custome = pygame.image.load("images/{}.png".format(custome))
        self.position = [x, y]
        self.name = name
        
    '''Este método contendrá la codificación para hacer que el corredor corra (avance por la pantalla horizontalmente).
       Para ello incrementará la coordenada X de su posición con un número generado de forma aleatoria.'''
    def run(self):
        self.position[0] += random.randint(1, 6)

'''Nuestra ejecución como programa principal iniciará el framework de PYGAME, instanciará un objeto carrera e invocará su metodo partida para que se lance dicha carrera.'''
if __name__ == "__main__":
    pygame.init()
    miJuegodeCarreras = GameRace()
    miJuegodeCarreras.match()
    