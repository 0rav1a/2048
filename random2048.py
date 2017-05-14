#coding:utf-8
import random
from Juego2048 import *

score = 0
for i in range(100):
    juego = Juego2048()
    while (juego.libres() > 0): #Efectúa un movimiento hasta que pierda
        juego.add()
        tablero = juego.getTablero()
        
        outputs = ["w","s","a","d"]
        while (tablero == juego.getTablero() and outputs):
            output = random.choice(outputs)
            juego.mover(output)
            outputs.remove(output)
            
    if juego.getScore() > score: score = juego.getScore()

print score