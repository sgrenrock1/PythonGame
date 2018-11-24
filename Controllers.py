__author__ = 'Steve'
import pygame

#This class detects key inputs
class Controllers(object):
    def __init__(self):
        self.events = []
        self.QUIT = False
        self.K_LEFT = False
        self.K_RIGHT = False
        self.K_UP = False
        self.K_DOWN = False
        self.K_a = False
        self.P_K_LEFT = False
        self.P_K_RIGHT = False

    def update(self):
        self.updatePreviousStates()
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.QUIT = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.QUIT = True
                if event.key == pygame.K_RIGHT:
                    self.K_RIGHT = True
                    self.K_LEFT = False
                elif event.key == pygame.K_LEFT:
                    self.K_LEFT = True
                    self.K_RIGHT = False
                elif event.key == pygame.K_UP:
                    self.K_UP = True
                elif event.key == pygame.K_DOWN:
                    self.K_DOWN = True
                elif event.key == pygame.K_a:
                    self.K_a = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.K_RIGHT = False
                elif event.key == pygame.K_LEFT:
                    self.K_LEFT = False
                elif event.key == pygame.K_a:
                    self.K_a = False

    def updatePreviousStates(self):
        self.P_K_LEFT = self.K_LEFT
        self.P_K_RIGHT = self.K_RIGHT
