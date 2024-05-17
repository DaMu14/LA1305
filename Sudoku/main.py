import tkinter as tk
from tkinter import messagebox
import random
import copy

def create_sudoku_field():
 i=0
 for y in range (0, 900, 100):
  for x in range (0, 900, 100):
   fields[i] = [pygame.Rect(x, y, 100, 100), sudoku[i]]
   pygame.draw.rect(screen, (0, 0, 0), fields[i][0], 1)

   
