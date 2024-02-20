import pygame
from colors import colors
class grid:
   def __init__(self):
      self.row_num=20
      self.col_num=10
      self.cell_size =35
      self.grid=[[0 for i in range (self.col_num)] for j in range (self.row_num)]
      self.color= colors.cell_color()

   def printo(self):
    for row in range(self.row_num):
      for col in range(self.col_num):
        #print(row,col, end = " ")
        print(self.grid[row][col], end = " ")
      print()

   def draw(self,screen):
     for row in range(self.row_num):
      for col in range(self.col_num):
       cell_val=self.grid[row][col]
       cell_rect=pygame.Rect(col*self.cell_size+1,row*self.cell_size+1,self.cell_size-1,self.cell_size-1)
       pygame.draw.rect(screen,self.color[cell_val],cell_rect) #cool color combination (255, 255, 255, 128)

   def is_inside(self,row,col):
     if row >= 0 and row < self.row_num and col >= 0 and col < self.col_num:
       return True
     return False

   def is_empty(self,row,col):
     if self.grid[row][col]==0:
       return True
     return False

   def full_row(self,row):
     for col in range (self.col_num):
       if self.grid[row][col]==0: #
         return False
     return True

   def clear_row(self,row):
    for col in range (self.col_num):
      self.grid[row][col] =0

   def move_down(self,row,row_num):
    for col in range(self.col_num):
      self.grid[row+row_num][col]=self.grid[row][col]
      self.grid[row][col]=0

   def clear (self):
    completed =0
    for row in range(self.row_num-1,0,-1):
      if self.full_row(row):
        self.clear_row(row)
        completed+=1
      elif completed>0:
        self.move_down(row,completed)
    return completed

   def reset(self):
     for col in range(self.col_num):
       for row in range(self.row_num):
         self.grid[row][col]=0

