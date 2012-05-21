'''
Created on 17/10/2011

@author: irving
'''

import ConfigParser

class CfgUtils():
    def __init__(self,nombrearchivo,seccion,valor):
        self.archivo = ConfigParser.ConfigParser()
        self.nombrearchivo = nombrearchivo
        self.seccion = seccion 
        self.valor = valor
        
    def leer(self):
        
        self.archivo.read([self.nombrearchivo])
        self.valore = self.archivo.get(self.seccion,self.valor)
        
        return self.valore
    
    def escribir(self,nuevovalor):
            self.nuevovalor = nuevovalor
            self.archivo.set(self.seccion, self.valor, str(self.nuevovalor))
            f = open(self.nombrearchivo, "w")  
            self.archivo.write(f)  
            f.close()     