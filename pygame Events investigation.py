'''

Keyboard input test for Pygame

'''

import pygame
from sys import exit
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode([500, 500])
window = pygame.Surface((500, 500))

# draw the initial screen
screen.blit(window, (0,0))

pygame.event.clear()

while True:
  for event in pygame.event.get():
    print ('Event Type ', event.type )
    if event.type == QUIT:
      #event type 12
      print ('QUIT Pressed')
      pygame.quit()
      exit()
    elif event.type == KEYDOWN:
      # event type 2
      print ('KeyDown Event Key ', chr(event.key))
    elif event.type == KEYUP:
      print ('KeyUp Event Key ', chr(event.key))
    elif event.type == MOUSEMOTION:
      # event type 4
      print ('Mouse Moving ', event.pos) # pos contains the coordinates
    elif event.type == MOUSEBUTTONDOWN:
      # 
      print ('Mouse button ', event.pos, event.button)
    elif event.type == MOUSEBUTTONUP:
      print ('Mouse Moving ', event.pos, event.button)
      
    pygame.event.clear


      
      

