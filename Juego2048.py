#coding:utf-8
import random
import time

FIL = 4
COL = 4

class Juego2048:
    def __init__(self):
        self.score = 0
        self.tablero = []
        for i in range(FIL):
            self.tablero.append([])
            for j in range(COL):
                self.tablero[i].append(0)
            
        self.add()
        #self.add()
            
    def imprimir(self):
        '''Imprime el tablero por pantalla
        '''
        for f in range(FIL):
            print
            for c in range(COL):
                if self.tablero[f][c] == 0: print " \t",
                else: print str(self.tablero[f][c]) + "\t",
            print
        print "__________________________"
            
    def add(self):
        '''Añade un elemento (un 2 o un 4) a una posición libre del tablero
        '''
        libres = []
        for f in range(FIL):
            for c in range(COL):
                if self.tablero[f][c] == 0: libres.append((f, c))
            
        rndX, rndY = random.choice(libres)
        elem = random.randint(0, 9)
        elem = 4 if elem == 9 else 2
        self.tablero[rndX][rndY] = elem

    def agrupar(self, linea):
        '''Efectúa un movimiento sobre una linea (fila o columna). Agrupa los elementos iguales al principio de la lista
        '''
        agrupada = [] #Lista que se devolverá
        for i in range(len(linea)): agrupada.append(0)
        sig = 0 #Siguiente hueco libre en la lista
        buf = 0 #Último elemento que se ha movido. Si coincide con el siguiente se sumarán
        
        for elem in linea:
            if elem != 0:
                if elem == buf:
                    agrupada[sig-1] *= 2
                    self.score += agrupada[sig-1]
                    buf = 0
                else:
                    agrupada[sig] = elem
                    sig += 1
                    buf = elem
                    
        return agrupada

    def mover(self, direccion):
        '''Efectúa un movimiento en todo el tablero en la dirección dada
        '''
        #movido = [i[:] for i in self.tablero[:]]
        movido = self.tablero
                    
        if direccion == "a":
            for f in range(FIL):
                fila = []
                for c in range(COL):
                    fila.append(movido[f][c])
                fila = self.agrupar(fila)
                
                for c in range(COL):
                    movido[f][c] = fila[c]
                
        elif direccion == "d":
            for f in range(FIL):
                fila = []
                for c in range(COL):
                    fila.append(movido[f][c])
                fila = self.agrupar(fila[::-1])[::-1]
                
                for c in range(COL):
                    movido[f][c] = fila[c]
                
        elif direccion == "w":
            for c in range(COL):
                columna = []
                for f in range(FIL):
                    columna.append(movido[f][c])
                columna = self.agrupar(columna)
                
                for f in range(FIL):
                    movido[f][c] = columna[f]
                
        elif direccion == "s":
            for c in range(COL):
                columna = []
                for f in range(FIL):
                    columna.append(movido[f][c])
                columna = self.agrupar(columna[::-1])[::-1]
                
                for f in range(FIL):
                    movido[f][c] = columna[f]
        
        #self.add()
            
    def libres(self):
        '''Devuelve el número de casillas libres en el tablero. Si no hay ninguna, has perdido
        '''
        libres = 0
        for fila in self.tablero:
            for elem in fila:
                if elem == 0: libres += 1
        
        return libres
        
    def getMax(self):
        max = 0
        for fila in self.tablero:
            for casilla in fila:
                if casilla > max: max = casilla
        
        return max
        
    def getTablero(self): return [list(fila) for fila in self.tablero]
    def getScore(self): return self.score