#coding:utf-8
import random

class Neuron:
    def __init__(self, inputNeurons = []):
        '''
        Neurona con varias entradas, un peso asignado a cada entrada, y una salida
        Si no hay entradas a la neurona, su salida será el valor inicial (init)
        inputNeurons: Lista de neuronas que se conectan a la actual
        weights: Lista de pesos de cada neurona de entrada (misma longitud que inputNeurons)
        '''
        self.inputNeurons = inputNeurons
        self.weights = []
        for i in range(len(inputNeurons)):
            self.weights.append(random.uniform(-1,1))
            
        self.initValue = 0
    
    def mutate(self, prob):
        '''Si hay suerte, uno o varios pesos de la neurona mutan a uno nuevo aleatorio
        '''
        for w in range(len(self.weights)):
            if random.uniform(0,1) < prob:
                self.weights[w] = random.uniform(-1,1)
        
    def getOutput(self):
        '''Devuelve la salida de la neurona. Esta es calculada recursivamente llamando a getOutput de las neuronas de entrada
        '''
        out = self.initValue
        
        for i in range(len(self.inputNeurons)):
            out += self.inputNeurons[i].getOutput() * self.weights[i]
    
        return out
        
    def setInit(self, init): self.initValue = init