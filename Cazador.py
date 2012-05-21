'''
Created on 12/10/2011

@author: irving
'''
from pygame.sprite import Sprite
from util import cargar_imagen

class Cazador(Sprite):   
    def __init__(self):
        Sprite.__init__(self);
        self.normal=cargar_imagen('cazador.png', -1);
        self.sonrisa =cargar_imagen('cazador_contento.png', -1);
        self.image,self.rect = self.normal;
        self.rect.x = 20;
        self.rect.y = 80;
        self.estado_contador=0;
    
    def risa(self):
        self.image,_ = self.sonrisa;
        self.estado_contador =50;
        
    def update(self):
        if self.estado_contador >0:
            self.estado_contador-=1;
            if self.estado_contador <1:
                self.image,_ = self.normal