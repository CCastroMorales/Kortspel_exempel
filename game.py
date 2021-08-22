import pygame
import random
from card import *

class Game:
  def __init__(self):
    pygame.init()
    pygame.font.init()

    self.display = pygame.display.set_mode((500,400),0,32)

    self.myfont = pygame.font.SysFont(None, 30)
    self.textsurface = self.myfont.render('Samsam', False, (0, 0, 0))

  def create_cards(self):
    cards = []
    x = 10
    y = 10
    for i in range(0,4):
      for j in range(0,13):
        card_value = y+1
        card = Card(x, y, card_value)

        if random.random() > 0.5:
          card.side = CARD_SIDE_FRONT
        else:
          card.side = CARD_SIDE_BACK

        cards.append(card)
        x += card.width + 6
      y += card.height + 4
      x = 10
    return cards

  def run(self):
    self.cards = self.create_cards()
    self.gameloop()

  def draw(self):
    # Rita bakgrunden
    self.display.fill((234,34,22))

    # Rita korten
    for card in self.cards:
      card.draw(self.display)
      #pygame.draw.rect(self.display,card.color,(card.x, card.y, card.width, card.height))
      #print("%i %i %i %i" % (card.x, card.y, card.width, card.height))

    # Rita texten
    mousepos = pygame.mouse.get_pos()
    mouse_pos_surface = self.myfont.render("%i, %i" % (mousepos[0], mousepos[1]), False, (0, 0, 0))
    self.display.blit(mouse_pos_surface,(10,350))


  def gameloop(self):
    while (True):
      mousepos = pygame.mouse.get_pos()
      pygame.display.set_caption("%i, %i" % (mousepos[0], mousepos[1]))

      # Känn av klick
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          #score += 1
          #print("Your score: %i" % (score))
          print("Mouse up at %i,%i" % (mousepos[0], mousepos[1]))
      ## ------- 

      self.draw()
      pygame.display.update()