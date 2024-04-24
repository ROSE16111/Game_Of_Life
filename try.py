#E:\ > conda create - p / me / python / GameA2 / env_Game python = 3.11.7
#conda activate E:\me\python\GameA2\env_game
import numpy as np
import scipy
import matplotlib
import math
import rle
import conway
#E:\me\python\GameA2\rle_Files\gosperglidergun.rle
#get String--------------------------------------------
with open("E:\me\python\GameA2\\rle_Files\\66p13on30p25.cells.txt", "r") as f: 
    rle_String = f.read()
rle_parser = rle.RunLengthEncodedParser (rle_String)
print(rle_parser.pattern_2d_array)
#txtString = rle_parser.human_friendly_pattern

txtString=rle_String
print(txtString)
#simple-------------------------------------------
N = 64
fastMode = True
#create the game of life object
life = conway.GameOfLife(N,fastMode)

#insert
#life.insertFromRLE(rle_String)
life.insertFromPlainText(txtString)

cells = life.getStates()

#evolve once
life.evolve()
cellsUpdated1 = life.getStates()


#plot-------------------------------------
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

plt.show()