__author__ = 'Steve'
import pygame
from Controllers import *
from Rabbit import Rabbit
from Python import Python, FastPython
import Resources
from LevelObjects import *
class Stage(object):
    def __init__(self):
        self.frameRate = 12
        self.screen = pygame.display.get_surface()
        self.controllers = Controllers()
        self.otherActors = []
        self.nonActors = []
        self.Rabbit = Rabbit(100, 375, self)
        self.clock = pygame.time.Clock()
        self.running = False
        self.bgImage = Resources.BG_IMAGES["1"]
        self.level = open("levels/just_ground.txt")
        self.checkInput = True

    def run(self):
        self.running = True
        self.initLevel()
        self.addRabbitObservers()
        while self.running:
            if self.checkInput:
                self.controllers.update()
            self.screen.blit(self.bgImage, (0,0))
            self.Rabbit.moveBehavior.atEdge = False
            self.Rabbit.update()
            self.checkEdge()
            self.updateNonActors()
            self.updateActors()
            self.Rabbit.paint()
            self.checkCollisions()
            pygame.display.flip()
            self.checkForRemoval()
            self.clock.tick(self.frameRate)
        pygame.quit()

    def addRabbitObservers(self):
        for actor in self.otherActors:
            if actor.name == "Python":
                self.Rabbit.addObserver(actor)

    def checkEdge(self):
        """
        Checks if the player is at the right-hand edge of the movable area.
        If so, the other Actors on the stage are notified to move left at an
        accelerated speed.
        """
        if self.Rabbit.moveBehavior.atEdge:
            for actor in self.otherActors:
                if actor.moveBehavior.x > 850:
                    actor.moveBehavior.speed = 16
                else:
                    actor.moveBehavior.speed = actor.moveBehavior.advancedSpeed
            for actor in self.nonActors:
                if actor.moveBehavior.x > 850:
                    actor.moveBehavior.speed = 16
                else:
                    actor.moveBehavior.speed = actor.moveBehavior.advancedSpeed
        else:
            for actor in self.otherActors:
                actor.moveBehavior.resetSpeed()
            for actor in self.nonActors:
                actor.moveBehavior.resetSpeed()

    def updateNonActors(self):
        """
        Updates the positions and paints the other Actors
        """
        for actor in self.nonActors:
            actor.update()
            actor.paint()

    def updateActors(self):
        """
        Updates the positions and paints the other Actors
        """
        for actor in self.otherActors:
            actor.update()
            actor.paint()

    def blit(self, surface, pos):
        self.screen.blit(surface, pos)

    def checkForRemoval(self):
        """
        Checks if any actors have moved sufficiently outside the playing field.
        Removes the ones that have.
        """
        for actor in self.otherActors:
            if actor.moveBehavior.x < -800:
                self.removeActor(actor)

    def removeActor(self, actor):
        """
        Removes an Actor in otherActors based on that Actor's index
        """
        self.otherActors.pop(self.otherActors.index(actor))

    def quit(self):
        self.running = False

    def initLevel(self):
        """
        Reads a .txt file and assembles the Stage with Actors and LevelObjects
        """
        y = 0
        for line in self.level:
            curLine = line.rstrip()
            x = 0
            for char in curLine:
                charPos = 1
                if char == "G":
                    self.nonActors.append(Ground(x, 525, self))
                if char == "P":
                    self.otherActors.append(Python(x, y - 50, self))
                if char == "D":
                    self.nonActors.append(BackDrop(x, 327, self))
                if char == "p":
                    self.otherActors.append(FastPython(Python(x, y-50, self)))



                x += 20
            y += 25




    def checkCollisions(self):
        """
        Uses rectangles to check the intersections(collisions) of different Actors.
        First - checks any collisions that have occurred against the player.
        Second - checks what collisions have occurred against other actors.
        Uses the visitor pattern to actuate events during a collision
        """
        rabbitDimensions = pygame.Rect(self.Rabbit.moveBehavior.x,
                                       self.Rabbit.moveBehavior.y,
                                       self.Rabbit.surface.get_width(),
                                       self.Rabbit.surface.get_height())
        for actor in self.otherActors:
            a1 = pygame.Rect(actor.moveBehavior.x,
                             actor.moveBehavior.y,
                             actor.surface.get_width(),
                             actor.surface.get_height())
            if a1.colliderect(rabbitDimensions):
                self.Rabbit.acceptVisitor(actor)
                actor.acceptVisitor(self.Rabbit)
            for actor2 in self.otherActors:
                a2 = pygame.Rect(actor2.moveBehavior.x,
                                 actor2.moveBehavior.y,
                                 actor2.surface.get_width(),
                                 actor2.surface.get_height())
                if a2.colliderect(a1):
                    actor.acceptVisitor(actor2)
                    actor2.acceptVisitor(actor)







def main():
    pygame.init()
    pygame.display.set_mode([800,600])
    pygame.display.set_caption("Game")
    stage = Stage()
    stage.run()

if __name__ == "__main__":
    main()


