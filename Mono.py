'''
Created on 12/10/2011

@author: irving
'''
import pygame
from pygame.sprite import Sprite
from pygame.constants import K_LEFT, K_RIGHT
from util import cargar_imagen,cargar_sonido

class Mono(Sprite):
    def __init__(self):
        Sprite.__init__(self);
        self.cargar_imagenes();
        self.sonido_risa = cargar_sonido('risa.wav')
        self.sonido_grito = cargar_sonido('grito.wav')
        self.image = self.normal;
        self.rect = self.rect;
        self.rect.x = 400;
        self.rect.y = 430;
        self.estado_contador = 0;
            
    def cargar_imagenes(self):
        self.normal,self.rect = cargar_imagen('mono.png', -1);
        self.contento,self.rect = cargar_imagen('mono_contento.png', -1);
        self.grito,self.rect = cargar_imagen('mono_pierde.png', -1);
        
    def risa(self):
        self.image = self.contento
        self.sonido_risa.play()
        self.estado_contador=50;

    
    def grito_perder(self):
        self.image = self.grito
        self.sonido_grito.play()
        self.estado_contador=50;        
    
    def update(self):
        if self.estado_contador >0:
            self.estado_contador-=1;
            if self.estado_contador <1:
                self.image = self.normal                
        key = pygame.key.get_pressed();
        
        if key[K_LEFT]:
            self.rect.x -=5;
        elif key[K_RIGHT]:
            self.rect.x +=5;
            
        if self.rect.left <=0:
            self.rect.left = 0;
        elif self.rect.right >=640:
            self.rect.right = 640;