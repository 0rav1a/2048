#coding:utf-8
import random
from math import log

from Juego2048 import Juego2048
from Network import Network

N_INPUTS  = 16
N_OUTPUTS = 4

class DNA2048:
    def __init__(self, genome = []):
        '''Elemento DNA2048 con genoma aleatorio (o no, si se pasa como argumento)
        El genoma es una red neuronal
        '''
        self.genome = genome
        if (not genome):
            self.genome = Network(N_INPUTS, N_OUTPUTS)
                
    def calcFitness(self):
        '''Calcula el fitness del elemento en base a la puntuación obtenida en un tablero aleatorio
        '''
        self.juego = Juego2048()
        while (self.juego.libres() > 0): #Efectúa un movimiento hasta que pierda
            self.juego.add()
            tablero = self.juego.getTablero()
            inputs  = [] #Tablero convertido a array unidimensional
            outputs = [] #Salida de la red neuronal
            
            for fila in tablero:
                for casilla in fila:
                    #inputs.append(casilla)
                    inputs.append((log(casilla, 2) if (casilla != 0) else 0)/self.juego.getMax())
                                     
            outputs = self.genome.getOutput(inputs)
            
            #Selección de movimiento a partir de outputs    
            while (tablero == self.juego.getTablero() and any(outputs)):
                output = 0
                for o in range(N_OUTPUTS):
                    if abs(outputs[o]) > abs(outputs[output]): output = o
                 
                if output == 0: self.juego.mover("w")
                elif output == 1: self.juego.mover("s")
                elif output == 2: self.juego.mover("a")
                elif output == 3: self.juego.mover("d")
                outputs[output] = 0
            
        self.fitness = self.juego.getScore()
        #self.fitness /= 4096.0
        
    def crossover(self, partner):
        '''Devuelve un genoma producto de combinar aleatoriamente self y partner
        '''
        self.genome.crossover(partner.getGenome())
        
    def mutate(self, prob):
        '''La red muta
        '''
        self.genome.mutate(prob)
    
    def clone(self):
        '''Devuelve un elemento 2048 con mismo genoma que self
        '''
        return DNA2048(self.genome)
            
    def show(self):
        self.juego.imprimir()
        print "Score:\t\t" + str(self.fitness)
    def getFitness(self): return self.fitness
    def getGenome(self): return self.genome