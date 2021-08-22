import pygame
import random

CARD_SIDE_FRONT = 0
CARD_SIDE_BACK = 1

class Suit:
  HEART   = 0
  DIAMOND = 1
  CLOVER  = 2
  SPADE   = 3

def print_suit(suit):
  if suit == Suit.HEART:
    return "Hrt"
  elif suit == Suit.DIAMOND:
    return "Dmd"
  elif suit == Suit.CLOVER:
    return "Clv"
  elif suit == Suit.SPADE:
    return "Spd"
  else:
    return ""

class Card:
  x = 0
  y = 0
  width = 36
  height = 48
  value = 0
  suit = Suit.HEART
  side = CARD_SIDE_BACK

  def __init__(self, x, y, suit, value):
    self.x = x
    self.y = y 
    self.suit = suit
    self.value = value
    self.color = self.random_color()

  def __str__(self):
    side = "F" if self.side == CARD_SIDE_FRONT else "B"
    suit = print_suit(self.suit)
    return "[%s%i %s] (%i,%i)" % (suit, self.value, side, self.x, self.y)

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

  def at(self, x, y):
    if x >= self.x and x <= self.x + self.width:
      if y >= self.y and y <= self.y + self.height:
        return True
    return False