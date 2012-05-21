'''
Created on 13/10/2011

@author: irving
'''
import random
from pygame.sprite import Sprite

from util import cargar_imagen

class ObjetoCaer(Sprite):
    def __init__(self,velocidad):
        Sprite.__init__(self);
        self.velocidad = velocidad;
        self.rect.x = random.randint(0,572);
        self.posaleatoria = random.randint(0,7);
        self.posiciones = [-60,-130,-210,-265,-330,-400,-465,-550];
        self.rect.y = self.posiciones[self.posaleatoria];
    
    def update(self):
        self.movimiento()
        self.animacion()

    def movimiento(self):
        self.rect.y +=self.velocidad;  
        if self.rect.y >=480:
            self.kill()

    def animacion(self):
        pass

class Banana(ObjetoCaer):
    """docstring for Banana"""
    def __init__(self,velocidad):
        self.image,self.rect = cargar_imagen('banana.png', -1);
        ObjetoCaer.__init__(self,velocidad)

class Bomba(ObjetoCaer):
    """docstring for Bomba"""
    def __init__(self,velocidad):
        self._load_images();
        self.paso = 0;
        self.retraso =4;
        self.image,self.rect = cargar_imagen('bomba1.png', -1);
        self.posiciones = [-68,-136,-204,-272,-340,-408,-476,-544];
        ObjetoCaer.__init__(self,velocidad)


    def _load_images(self):
        self.frames =[];
        
        for n in range(1,3):
            path = 'bomba%d.png';
            self.nueva_image = cargar_imagen(path % n, -1)[0];
            self.frames.append(self.nueva_image);

    def animacion(self):
        self.image = self.frames[self.paso];
        if self.retraso <0:
            self.retraso =4;
            self.paso += 1;
        if self.paso > 1:
            self.retraso=4;
            self.paso=0;
        else:
            self.retraso -=1;




            