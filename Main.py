#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.constants import *

import pytweener

from util import cargar_imagen,texto
from Mono import Mono
from Boom import Boom
from Cazador import Cazador
from ObjetoCaer import Banana,Bomba
from barravida import BarraVida
from cfgutils import CfgUtils

escena = None

SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;

'''Creamos Pantala'''    
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Monkey Banana for PC - 1.0")
print "Creacion de ventana exitosa..."

'''
####################################################
#                  ESCENAS                         #
####################################################
''' 
class Opcion:
    '''Recurso para Menu'''
    def __init__(self,image,x,y):
        self.x = x
        self.y = y
        self.image = image
            
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

class Menu():
            
    def __init__(self):
        self.fondo,self._ = cargar_imagen('menu.png', 1);
        self.image,self.rect=cargar_imagen('menuopciones.png', True);
        self.tweener = pytweener.Tweener()
        self.clock = pygame.time.Clock()
        self.current = 1
        self.opcion = Opcion(self.image,0,150)
                           
    def update(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.current+=1
                    if self.current >5:
                        self.current =5
                if event.key == K_RIGHT:
                    self.current -=1   
                    if self.current <1:
                        self.current =1;
                        
        if self.current == 1:
            self.tweener.addTween(self.opcion,x=0,y=150,tweenTime=1.0,tweenType=pytweener.Easing.Elastic.easeOut)
            if key[K_RETURN]:
                iniciar_juego()
        if self.current == 2:    
            self.tweener.addTween(self.opcion,x=-400,y=150,tweenTime=1.0,tweenType=pytweener.Easing.Elastic.easeOut)
            if key[K_RETURN]:
                iniciar_instrucciones()
        if self.current == 3:
            self.tweener.addTween(self.opcion,x=-800,y=150,tweenTime=1.0,tweenType=pytweener.Easing.Elastic.easeOut)
            if key[K_RETURN]:
                iniciar_records()            
        if self.current == 4:
            self.tweener.addTween(self.opcion,x=-1100,y=150,tweenTime=1.0,tweenType=pytweener.Easing.Elastic.easeOut)
            if key[K_RETURN]:
                iniciar_creditos()
        if self.current == 5:
            self.tweener.addTween(self.opcion,x=-1400,y=150,tweenTime=1.0,tweenType=pytweener.Easing.Elastic.easeOut)
            if key[K_RETURN]:
                exit()
                
        self.dt=self.clock.tick(100)
        self.tweener.update(self.dt/1000.0)
      
    def imprimir(self,screen):
        screen.blit(self.fondo,(0,0))
        self.opcion.draw(screen)
        pygame.display.update()
        pygame.display.flip();

class Creditos():
    def __init__(self):
        self.image,_=cargar_imagen('creditos.png', 1);
        self.img_regresar,self.rect_regresar=cargar_imagen('regresar.png', True);
        self.rect_regresar.x = 20
        self.rect_regresar.y = 410
        
    def update(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.rect_regresar.collidepoint(event.pos[0],event.pos[1]):
                    iniciar_menu()    
                
    def imprimir(self,screen):
        screen.blit(self.image,(0,0))
        screen.blit(self.img_regresar,self.rect_regresar)
        pygame.display.flip();

class Instrucciones():
    def __init__(self):
        self.image,_=cargar_imagen('instrucciones.png', 1)
        self.img_regresar,self.rect_regresar=cargar_imagen('regresar.png', True);
        self.rect_regresar.x = 20
        self.rect_regresar.y = 410
        
    def update(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.rect_regresar.collidepoint(event.pos[0],event.pos[1]):
                    iniciar_menu()            
    
    def imprimir(self,screen):
        screen.blit(self.image,(0,0))
        screen.blit(self.img_regresar,self.rect_regresar)
        pygame.display.flip()
    
class Records():
    def __init__(self):
        self.image,_=cargar_imagen('record.png', 1);
        
        """Archivo de configuracion"""
        self.record = CfgUtils('records.cfg','record','valor')
        
        self.fuente = pygame.font.Font(None,90)
        
        self.record_img,self.record_rect=texto((255,255,255),self.record.leer(), self.fuente, SCREEN_WIDTH/2-70, SCREEN_HEIGHT/2-30);
        
        print self.record_rect
        print SCREEN_HEIGHT,SCREEN_WIDTH
        
        self.img_regresar,self.rect_regresar=cargar_imagen('regresar.png', True);
        self.rect_regresar.x = 20
        self.rect_regresar.y = 410
        
    def update(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.rect_regresar.collidepoint(event.pos[0],event.pos[1]):
                    iniciar_menu()
    
    def imprimir(self,screen):
        screen.blit(self.image,(0,0))
        screen.blit(self.record_img,self.record_rect)
        screen.blit(self.img_regresar,self.rect_regresar)
        pygame.display.flip();

class Gameover():
    def __init__(self,puntos,nivel):
        self.image,_=cargar_imagen('gameover.png', 1);
        
        self.irmenu_img,self.irmenu_rect=cargar_imagen('irmenu.png', True);
        self.irmenu_rect.x = 40;
        self.irmenu_rect.y =400;
        
        self.volverajugar_img,self.volverajugar_rect=cargar_imagen('volverjugar.png', True);
        self.volverajugar_rect.x = 450;
        self.volverajugar_rect.y = 400;
        
        
        self.puntos = puntos
        self.nivel = nivel
        
        """Archivo de configuracion"""
        self.record = CfgUtils('records.cfg','record','valor')
        if self.puntos > int(self.record.leer()):
            self.record.escribir(self.puntos)
            
          
        self.fuente = pygame.font.Font(None,70)
        self.record_img,self.record_rect=texto((255,255,255),"Puntos: "+str(self.puntos), self.fuente, 150,150);
        self.nivel_img,self.nivel_rect=texto((255,255,255),"Nivel: "+str(self.nivel), self.fuente, 240,300);
        
    def update(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.volverajugar_rect.collidepoint(event.pos[0],event.pos[1]):
                    iniciar_juego()
                elif self.irmenu_rect.collidepoint(event.pos[0],event.pos[1]):
                    iniciar_menu()
    
    def imprimir(self,screen):
        screen.blit(self.image,(0,0))
        screen.blit(self.record_img,self.record_rect)
        screen.blit(self.nivel_img,self.nivel_rect)
        screen.blit(self.volverajugar_img,self.volverajugar_rect)
        screen.blit(self.irmenu_img,self.irmenu_rect)
        pygame.display.flip()
    
class Juego():
    def __init__(self):
        
        """Archivo de configuracion"""
        self.record = CfgUtils('records.cfg','record','valor')
        
        self.sprites = pygame.sprite.Group();
        self.bombas = pygame.sprite.Group();
        self.bananas = pygame.sprite.Group();
        
        self.puntos = 0;
        self.nivel = 1;
        self.vida = 150;
        self.barravida = BarraVida(400, 20, (255,0,5), (255,255,255), 30, 150)
        self.velocidad = 2;
        
        self.blanco=(255,255,255)
        
        '''Creamos mono'''
        self.mono = Mono();
        self.sprites.add(self.mono);

        '''Creamos cazador'''
        self.cazador = Cazador();
        self.sprites.add(self.cazador);
        
        self.fuentegrande = pygame.font.Font(None,70);
        self.fuentechica=pygame.font.Font(None,40);
        
        self.contador_creacion_bombas = 0;
        self.contador_creacion_bananas = 0;
        
        self.fondo,_ = cargar_imagen('fondo.png', 1);
        
        '''Creamos el texto para evitar errores al imprimir'''
        self.puntos_img,self.puntos_rect=texto(self.blanco, "Puntos: "+str(self.puntos), self.fuentechica, 15, 10);
        self.nivel_img,self.nivel_rect=texto(self.blanco, "Nivel: " +str(self.nivel), self.fuentechica, 15, 10)
        self.record_img,self.record_rect=texto(self.blanco, "Record: "+str(self.record.leer()), self.fuentechica, 15, 40)        
        
    def update(self):
        global escena
        self.puntos_img,self.puntos_rect=texto(self.blanco, "Puntos: "+str(self.puntos), self.fuentechica, 15, 10);
        self.nivel_img,self.nivel_rect=texto(self.blanco, "Nivel: " +str(self.nivel), self.fuentechica, 400, 45)
        
        if self.vida <=0:
            escena = Gameover(self.puntos,self.nivel)
        
        self.puntosnivel = self.puntos/self.nivel
        if self.puntosnivel == 200:
            self.nivel +=1;
            self.velocidad +=0.5
       
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
        '''Creacion de las bombas'''
        self.contador_creacion_bombas +=3*self.nivel*1.2;
        if self.contador_creacion_bombas >=250*self.nivel:
            self.nueva_bomba = Bomba(self.velocidad);
            self.sprites.add(self.nueva_bomba);
            self.bombas.add(self.nueva_bomba);
            self.contador_creacion_bombas=0;
        
        '''Creacion de las bananas'''
        self.contador_creacion_bananas +=4*self.nivel*2;
        if self.contador_creacion_bananas >=self.nivel*200:
            self.nueva_banana = Banana(self.velocidad);
            self.sprites.add(self.nueva_banana);
            self.bananas.add(self.nueva_banana);
            self.contador_creacion_bananas=0;
        
        for hit in pygame.sprite.spritecollide(self.mono,self.bombas,1):
            self.mono.grito_perder();
            self.cazador.risa();
            (x,y) = hit.rect.center;
            self.sprites.add(Boom(x,y));
            self.vida -=15;
        
        for hit in pygame.sprite.spritecollide(self.mono,self.bananas,1):
            self.mono.risa();
            self.puntos +=20
                    
        self.sprites.update()
    
    def imprimir(self,screen):
        screen.blit(self.fondo,(0,0));
        screen.blit(self.puntos_img,self.puntos_rect)
        screen.blit(self.nivel_img,self.nivel_rect)
        screen.blit(self.record_img,self.record_rect)
        self.sprites.draw(screen)
        self.barravida.imprimir(screen, self.vida)
        pygame.display.flip();
        
'''
####################################################
#              FUNCIONES                           #
#            CAMBIOS Y ESCENAS                     #
####################################################
'''
def iniciar_juego():
    global escena
    print "Iniciando Juego"
    escena=Juego()

def iniciar_menu():
    global escena
    print "Iniciando Menu"
    escena = Menu()

def iniciar_creditos():
    global escena
    print "Iniciando Creditos"
    escena = Creditos()
    
def iniciar_records():
    global escena
    print "Iniciando Records"
    escena = Records()

def iniciar_instrucciones():
    global escena
    print "Iniciando Instrucciones"
    escena = Instrucciones()

'''
####################################################
#              BUCLE PRINCIPAL                     #
####################################################
'''
def main():
    global escena,screen
    pygame.init()
    
    '''Reloj'''
    clock = pygame.time.Clock()
    
    escena=Menu()
        
    while True:
        
        key = pygame.key.get_pressed()
        if key[K_f] and key[K_RETURN]: #Activamos modo FULLSCREEN
            screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),FULLSCREEN)
            
        escena.update()
        escena.imprimir(screen)
        print clock.tick(60)
        
if __name__ == '__main__':
    main()
