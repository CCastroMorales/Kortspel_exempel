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
    self.running = True
    self.gameloop()

  def stop(self):
    self.running = False
    pygame.quit()

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
    while (self.running):
      mousepos = pygame.mouse.get_pos()
      pygame.display.set_caption("%i, %i" % (mousepos[0], mousepos[1]))

      events = pygame.event.get()

      for event in events:
        # Känn av klick
        if event.type == pygame.MOUSEBUTTONUP:
          #score += 1
          #print("Your score: %i" % (score))
          print("Mouse up at %i,%i" % (mousepos[0], mousepos[1]))
        ## ------- 

      self.draw()
      pygame.display.update()

      # Avsluta spelet
      for event in events:
        if event.type == pygame.QUIT:
          self.stop()
          break

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.stop()
            break