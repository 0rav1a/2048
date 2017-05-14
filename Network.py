#coding:utf-8
import random
from Neuron import Neuron

class Network:
    def __init__(self, nInputs = 1, nOutputs = 1):
        '''Red neuronal con nInputs entradas y nOutputs salidas (y una capa oculta). Los pesos de todas las neuronas son aleatorios
        '''
        self.layers = {"input": [], "hidden": [], "output": []}
        
        for i in range(nInputs):
            self.layers["input"].append(Neuron())
        
        for n1 in range(nInputs): #Una neurona por cada combinación posible de dos neuronas de la capa de entrada
            for n2 in range(nInputs)[n1+1:]:
                inputNeurons = [self.layers["input"][n1], self.layers["input"][n2]]
                self.layers["hidden"].append(Neuron(inputNeurons))
        '''        
        for i in range(nInputs): #Una neurona por cada neurona de entrada
            inputNeurons = self.layers["input"]
            self.layers["hidden"].append(Neuron(inputNeurons))
        '''
        for o in range(nOutputs):
            inputNeurons = self.layers["hidden"]
            self.layers["output"].append(Neuron(inputNeurons))
        
    def crossover(self, partner):
        '''Devuelve una red aleatoria producto de combinar las neuronas de self y partner
        '''
        child = Network()
        newLayers = {"input": [], "hidden": [], "output": []}
        
        for layer in self.layers: #Para cada capa de la red
            for i in range(len(self.layers[layer])): #Para cada neurna de la capa
                newLayers[layer].append(random.choice([self.layers[layer][i], partner.getLayers()[layer][i]]))
                
        child.setLayers(newLayers)
        
        return child
    
    def mutate(self, prob):
        '''Se le ofrece a cada neurona la posibilidad de mutar
        '''
        for layer in self.layers: #Para cada capa de la red
            for i in range(len(self.layers[layer])): #Para cada neurona de la capa
                self.layers[layer][i].mutate(prob)
        
    def getOutput(self, inputs):
        '''
        Dada una lista de inputs, devuelve la lista de outputs de la red neuronal
        La longitud de inputs debe ser la misma que la de inputLayer (nInputs)
        '''
        for i in range(len(inputs)):
            self.layers["input"][i].setInit(inputs[i])
            
        return [outputNeuron.getOutput() for outputNeuron in self.layers["output"]]
    
    def getLayers(self): return self.layers
    def setLayers(self, l): self.layers = l