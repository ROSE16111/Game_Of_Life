# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

#get String--------------------------------------------
#with open("E:\me\python\GameA2\\rle_Files\moldon30p25.cells.txt", "r") as f: 
#with open("E:\me\python\GameA2\\rle_Files\\30p25onp76piheptominohassler.cells.txt", "r") as f: 
with open("E:\me\python\GameA2\\rle_Files\\66p13on30p25.cells.txt", "r") as f: 
    txtString = f.read()


N = 64

#create the game of life object
life = conway.GameOfLife(N)

#life.insertBlinker((0,0))
#life.insertGlider((0,0))
#life.insertGliderGun((0,0))
life.insertFromPlainText(txtString)

cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    cellsUpdated = life.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 200 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
