'''
Created on 17/10/2011

@author: irving
'''
import pygame

class BarraVida():
    '''Creamos la clase BarraVida'''
    '''Los paramatros x & y son posicion /
                colorvida = Relleno de color de la barra
                colorlinea = Contorno de la barra
                alto = Alto de la barra
                ancho = Ancho de la barra'''
    def __init__(self,x,y,colorvida,colorlinea,alto,ancho):
        self.x= x
        self.y = y
        self.colorvida = colorvida
        self.colorlinea = colorlinea
        self.ancho = ancho;
        self.alto = alto
        
    def update(self):
        pass
    
    def imprimir(self,screen,vida):
        '''Imprimimos en pantalla los dos objetos que componen la barra'''
        '''Parametros screen = Pantalla donde se va a imprimir
                    vida = cantidad de vida que contendra la barra
                        Por ejemplo:
                            vida = 100;
                            vida -=2'''
        self.vida = vida
        pygame.draw.rect(screen,(self.colorlinea),(self.x-2,self.y-16,self.ancho+4,self.alto+3),2)
        pygame.draw.line(screen,(self.colorvida),(self.x,self.y),(self.x+self.vida,self.y),self.alto)
         
'''        
def main():
    vida_contador = 200;
    vida = BarraVida(10,20,(255,0,0),(255,255,255),30,200)
    
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
    
        if key[K_RETURN]:
            vida_contador -= 4;
            if vida_contador <= 0:
                vida_contador = 0;
        elif key[K_BACKSPACE]:
            vida_contador +=4;
            if vida_contador >=200:
                vida_contador = 200;
                
    
        screen.fill((0,0,0))
        vida.imprimir(screen,vida_contador)
        pygame.display.flip()

main()'''     