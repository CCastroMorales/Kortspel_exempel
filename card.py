import pygame
import random

CARD_SIDE_FRONT = 0
CARD_SIDE_BACK = 1

class Card:
  x = 0
  y = 0
  width = 20
  height = 32
  value = 0
  side = CARD_SIDE_BACK

  def __init__(self, x, y, value):
    self.x = x
    self.y = y 
    self.value = value
    self.color = self.random_color()

  def random_color(self):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

  def draw(self, display):
    white = (255,255,255)
    pygame.draw.rect(display,white,(self.x, self.y, self.width, self.height))

    if self.side == CARD_SIDE_FRONT:
      self.draw_front(display)
    else:
      self.draw_back(display)

  def draw_front(self, display):
    white = (255,255,255)
    pygame.draw.rect(display,white,(self.x, self.y, self.width, self.height))

  def draw_back(self, display):
    black = (0,0,0)
    pygame.draw.rect(display,black,(self.x, self.y, self.width, self.height))

  def flip(self):
    if self.side == CARD_SIDE_FRONT:
      self.side = CARD_SIDE_BACK
    else:
      self.side = CARD_SIDE_FRONT