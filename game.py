from grid import grid
from blocks import*
import random
class game:
    def __init__(self):
        self.grid=grid()
        self.blocks=[Iblock(),Jblock(),Lblock(),Oblock(),Sblock(),Tblock(),Zblock()]
        self.current_block= self.random_block()
        self.next_block= self.random_block()
        self.game_over=False
        self.score=0

    def update_score(self,rows_cleard,move_down_points):
        if rows_cleard==1:
            self.score+=100
        elif rows_cleard==2:
            self.score+=300
        elif rows_cleard==3:
            self.score+=500
        self.score+=move_down_points

    def random_block(self):
        if len(self.blocks)==0:
         self.blocks=[Iblock(),Jblock(),Lblock(),Oblock(),Sblock(),Tblock(),Zblock()]
        block= random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self,screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,1,1)
        if self.next_block.id==3:
            self.next_block.draw(screen,265,245)
        elif self.next_block.id==2:
            self.next_block.draw(screen,265,260)
        else:
          self.next_block.draw(screen,280,235)

    def move_left(self):
        self.current_block.move(0,-1)
        if self.check()==False or self.block_fits()==False:
          self.current_block.move(0,1)


    def move_right(self):
        self.current_block.move(0,1)
        if self.check()==False or self.block_fits()==False:
          self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1,0)
        if self.check()==False or self.block_fits()==False:
          self.current_block.move(-1,0)
          self.lock_block()

    def block_fits(self):
        tiles=self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row,tile.col)==False:
                return False
        return True
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            #print(position.row)
            self.grid.grid[position.row][position.col]=self.current_block.id
            self.grid.printo()
        self.current_block=self.next_block
        self.next_block=self.random_block()
        rows_cleard=self.grid.clear()
        self.update_score(rows_cleard,0)
        if self.block_fits()==False:
            self.game_over=True

    def rotate(self):
        self.current_block.rotation()
        if self.check()==False or self.block_fits()==False:
          self.current_block.undo_rotation()



    def check(self):
        tiles=  self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.col)==False:
                return False
        return True
    def reset(self):
        self.grid.reset()
        self.blocks=[Iblock(),Jblock(),Lblock(),Oblock(),Sblock(),Tblock(),Zblock()]
        current_block= self.random_block()
        next_block=self.random_block()
        self.score=0


