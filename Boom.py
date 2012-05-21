'''
Created on 12/10/2011

@author: irving
'''
from pygame.sprite import Sprite
from util import cargar_imagen

class Boom(Sprite):   
    def __init__(self,x,y):
        Sprite.__init__(self);
        self._load_images();
        self.paso = 0;
        self.retraso = 5;
        self.image,self.rect = cargar_imagen('boom1.png', -1)
        self.rect.center =(x,y)
        
    def _load_images(self):
        self.frames = [];
        
        for n in range(1,3):
            path = 'boom%d.png';
            nueva_image = cargar_imagen(path % n, -1)[0];
            self.frames.append(nueva_image);       
            
        
    def update(self):
        self.image = self.frames[self.paso]
        if self.retraso <0:
            self.retraso = 5;
            self.paso +=1;
        if self.paso >1:
            self.kill();
        else:
            self.retraso-=1;