# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

fastMode=True
padding = 10
N = 2100
#N = 1024
#N = 64

#read RLE file,get String--------------------------------------------
#~ with open("gosperglidergun.rle", "r") as text_file:

#with open("E:\me\python\GameA2\\rle_Files\part_E.rle", "r") as text_file:
#with open("GameA2\\rle_Files\\30p25onp76piheptominohassler.rle", "r") as text_file:
#with open("E:\me\python\GameA2\\rle_Files\\66p13on30p25.rle", "r") as text_file: 
#with open("E:\me\python\GameA2\\rle_Files\moldon30p25.rle", "r") as text_file:
with open("E:\me\python\GameA2\\rle_Files\\turingmachine.rle", "r") as text_file:

        rleString = text_file.read()

#create the game of life object
life = conway.GameOfLife(N,fastMode)
life.insertFromRLE(rleString, padding)
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

interval = 50 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)
#~ animate(0)

plt.show()
