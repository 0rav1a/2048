#coding:utf-8
import random
import time
from DNA2048 import DNA2048 as DNA

SIZE = 100 #Tamaño de cada generación
MUTATION = 0.2 #Probabilidad de mutación
UNFIT = 0.5 #Porcentaje de individuos de cada generación que muere en el proceso de selección
EVOLVED = 50000 #Fitness para el cual se considera que un genoma está completamente evolucionado

def getFittest(generation):
    '''Devuelve el individuo más apto de una generación
    '''
    fittest = generation[0]
    for individual in generation[1:]:
        if individual.getFitness() > fittest.getFitness(): fittest = individual
        
    return fittest
    
def getLessFit(generation):
    '''Devuelve el individuo menos apto de una generación
    '''
    lessfit = generation[0]
    for individual in generation[1:]:
        if individual.getFitness() < lessfit.getFitness(): lessfit = individual
        
    return lessfit
    
def evaluation(generation):
    '''Evalúa el fitness de cada individuo de la población
    '''
    for individual in generation:
        individual.calcFitness()
    
def selection(generation):
    '''Un porcentaje de los individuos menos aptos muere
    '''
    for i in range(int(SIZE*UNFIT)):
        generation.remove(getLessFit(generation))

def reproduction(parent1, parent2):
    '''Elige dos padres del matingPool y genera un hijo con genoma cominado (y posible mutación)
    '''    
    child = DNA(parent1.crossover(parent2))
    child.mutate(MUTATION)
    
    return child
    
def pick(generation, totalFit):
    randomFit = random.uniform(0, totalFit)
    for individual in generation:
        randomFit -= individual.getFitness()
        if randomFit <= 0:
            return individual
    
def getNewGeneration(generation = []):
    '''Devuelve una nueva generación producto de evolucionar la dada. Si no se da ninguna, se genera con individuos de genoma aleatorio
    '''
    newGeneration = []
    
    if (generation == []):
        for i in range(SIZE):
            newGeneration.append(DNA())
    
    else:
        selection(generation)

        totalFit = 0
        for individual in generation:
            totalFit += individual.getFitness()
        
        for i in range(SIZE):
            parent1 = pick(generation, totalFit)
            parent2 = pick(generation, totalFit)
            
            child = reproduction(parent1, parent2)
            newGeneration.append(child)
        
    return newGeneration
    
###MAIN
tiempo = time.time()
nGenerations = 0

generation = getNewGeneration()
evaluation(generation)

while (getFittest(generation).getFitness() < EVOLVED): #Mientras la generación no esté completamente evolucionada, se generará una nueva
    getFittest(generation).show()
    print "Generación:\t" + str(nGenerations)
    generation = getNewGeneration(generation)
    evaluation(generation)
    
    nGenerations += 1
    
print "Generaciones:\t" + str(nGenerations)
print "Segundos:\t" + str(time.time() - tiempo)