from colors import colors
import pygame
from position import position


class block:
    def __init__ (self,id):
      self.id=id
      self.cells= {}
      self.row_off=0
      self.col_off=0
      self.cell_size=35
      self.rotation_state =0
      self.color=colors.cell_color()

    def move(self,rows,cols):
     self.row_off+=rows
     self.col_off+=cols

    def get_cell_positions(self):
       tiles=self.cells[self.rotation_state] #tiles = cell position
       moved_tiles=[]
       for pos in tiles:
           new_position = position(pos.row+self.row_off,pos.col+self.col_off)
           moved_tiles.append(new_position)
       return moved_tiles

    def rotation(self):
        self.rotation_state+=1
        if self.rotation_state== len(self.cells):
            self.rotation_state=0

    def undo_rotation(self):
        self.rotation_state -=1
        if self.rotation_state <0:
            self.rotation_state=len(self.cells)-1

    def draw(self,screen,offsetx,offsety):
       tiles= self.get_cell_positions()
       for tile in tiles:
        tile_rect= pygame.Rect(tile.col*self.cell_size+offsetx,tile.row*self.cell_size+offsety,self.cell_size-1,self.cell_size-1)
        pygame.draw.rect(screen,self.color[self.id],tile_rect)

