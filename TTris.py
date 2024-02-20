import pygame
from sys import exit
from game import game
from grid import grid
from colors import colors
pygame.init()
screen = pygame.display.set_mode((525,700))
pygame.display.set_caption("ttris")
clock = pygame.time.Clock()
fontt = pygame.font.Font(None,45)
gamename=fontt.render('TTris',True,'Gold')
score=fontt.render('Score',True,'Gold')
score_rect=pygame.Rect(359,70,160,60)
next_tile=fontt.render('Next',True,'Gold')
next_tile_rect=pygame.Rect(359,212,160,135)
gamee=fontt.render('GAME',True,'Gold')
overr=fontt.render('OVER',True,'Red')

block = game()
gg=grid()
game_update=pygame.USEREVENT
pygame.time.set_timer(game_update,500)
while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
      if event.type==pygame.KEYDOWN:
        if block.game_over==True:
          block.game_over=False
          block.reset()
        if event.key==pygame.K_LEFT and block.game_over==False:
          block.move_left()

        if event.key==pygame.K_RIGHT and block.game_over==False:
          block.move_right()

        if event.key==pygame.K_DOWN and block.game_over==False:
          block.move_down()
          block.update_score(0,1)

        if event.key==pygame.K_UP and block.game_over==False:
          block.rotate()
      if event.type==game_update and block.game_over==False:
        block.move_down()

  scoree=fontt.render(str(block.score),True,'Gold')
  screen.fill(colors.fill)
  pygame.draw.line(screen,'White',(351,0),(351,700),width=1)
  #screen.blit(gamename,(400,20))
  screen.blit(score,(400,30))
  pygame.draw.rect(screen,colors.other,score_rect,0,10)
  screen.blit(scoree,scoree.get_rect(centerx=score_rect.centerx,centery=score_rect.centery))
  screen.blit(next_tile,(404,170))
  pygame.draw.rect(screen,colors.other,next_tile_rect,0,10)
  if block.game_over==True:
   screen.blit(gamee,(395,430))
   screen.blit(overr,(395,464))

  block.draw(screen)


  #gg.printo()

  pygame.display.update()
  clock.tick(60)
