# -*- coding: utf-8 -*-
"""
Game of life simple script for checking init states and checking if the evolution is
implemented correctly.

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

#get String--------------------------------------------
with open("E:\me\python\GameA2\\rle_Files\\66p13on30p25.cells.txt", "r") as f: 
    txtString = f.read()




N = 64

#create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((0,0))
#life.insertGlider((0,0))
life.insertGliderGun((0,0))
cells = life.getStates() #initial state

#evolve once
life.evolve()
cellsUpdated1 = life.getStates()

#evolve twice
life.evolve()
cellsUpdated2 = life.getStates()

#evolve triple
life.evolve()
cellsUpdated3 = life.getStates()

#evolve fourth
life.evolve()
cellsUpdated4 = life.getStates()

#evolve fifth
life.evolve()
cellsUpdated5 = life.getStates()

#evolve sixth
life.evolve()
cellsUpdated6 = life.getStates()





#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import numpy as np

plt.figure(0)
plt.gray()
plt.imshow(cells)

ax = plt.gca()
# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
#grid
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.figure(1)
plt.imshow(cellsUpdated1)

plt.figure(2)
plt.imshow(cellsUpdated2)

#plt.figure(3)
#plt.imshow(cellsUpdated3)

#plt.figure(4)
#plt.imshow(cellsUpdated4)

#plt.figure(5)
#plt.imshow(cellsUpdated5)

#plt.figure(6)
#plt.imshow(cellsUpdated6)

plt.show()
