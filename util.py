'''
Created on 16/10/2011

@author: irving
'''
import pygame
import os
    
def cargar_imagen(name,transparente):
    """CARGA DE IMAGENES"""
    fullname = os.path.join('./datos/',name);
    
    try:
        image = pygame.image.load(fullname);
    except pygame.error, message:
        print "Imposible cargar imagen ",fullname;
        raise SystemExit, message;
    
    if transparente==True:
        image.convert_alpha()

    return image, image.get_rect();
    
def cargar_sonido(name):
    """CARGA SONIDOS"""
    class NoneSound:
        def play(self):
            pass
    
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound();
    
    fullname = os.path.join('./datos/',name);
    
    try:
        sound = pygame.mixer.Sound(fullname);
    except pygame.error, message:
        print "No se pudo cargar el sonido ",fullname;
        raise SystemExit, message;
    
    return sound;

def texto(color,texto,fuente,posx,posy):
    '''Creamos texto para posteriormente imprimirlo
        La funcion retorna: surface y rect'''
    text_surface = fuente.render(str(texto),1,color)
    text_rect=text_surface.get_rect()
    text_rect.left,text_rect.top = (posx,posy)
    return text_surface,text_rect
