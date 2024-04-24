# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal
import rle

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int64)
        self.neighborhood = np.ones((3,3), np.int64) # 8 connected kernel/core核心
        self.neighborhood[1,1] = 0 #do not count centre pixel像素
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        #get the current grid
        current_grid = self.getStates()
        #get weighted sum of neighbors
        #PART A 
        if self.fastMode == False:
            print("NormalMode")
            neighbors_count = np.zeros_like(current_grid)
            rows, cols = len(current_grid), len(current_grid[0])
            for r in range(rows):
                for c in range(cols):
                    for i in range(max(0,r-1),min(rows,r+2)):
                        for j in range(max(0, c-1), min(cols, c+2)):
                            if i != r or j != c:
                                neighbors_count[r][c] += current_grid[i][j]
            

        #Part E use convolution as fastMode
        else:
            print("FastMode")
            neighbors_count = signal.convolve2d(current_grid, self.neighborhood, mode='same', boundary='fill', fillvalue=self.deadValue)


        #implement the GoL rules by thresholding the weights（权重阈值化）
        #PART A CODE HERE
        new_grid = np.zeros_like(current_grid)
        new_grid = np.where((current_grid == self.aliveValue) & ((neighbors_count < 2) | (neighbors_count > 3)), self.deadValue, new_grid)
        new_grid = np.where((current_grid == self.aliveValue) & ((neighbors_count == 2) | (neighbors_count == 3)), self.aliveValue, new_grid)
        new_grid = np.where((current_grid == self.deadValue) & (neighbors_count == 3), self.aliveValue, new_grid)
        #update the grid
        self.grid = new_grid
        return self.grid
    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct(闪烁振荡器) at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct(滑翔机结构) at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue # add a lost live
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        
    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        r = -1  
        lines = txtString.strip().split('\n')
        for line in lines: 
            if not line.startswith('!'):
                r+=1
                for l,i in enumerate(line):
                    if i == 'O' or i == 'o':
                        self.grid[r+pad][l+pad] = self.aliveValue
                

    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        rle_parser = rle.RunLengthEncodedParser(rleString)
        for r, row in enumerate(rle_parser.pattern_2d_array): #r index enumerate(iterable, start=0)
            for c, col in enumerate(row):
                if col == 'o':
                    self.grid[r+pad][c+pad] = self.aliveValue