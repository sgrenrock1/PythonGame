__author__ = 'Steve'
from Actor import Actor
from Behaviors import *
#from Python import Python
import Resources
from LevelObjects import Flower
class Star(Actor):
    def __init__(self,direction, x, y, stage):
        super().__init__(StarMove(direction, x, y), StarAttack(), StarSprite(), x, y, stage)
        self.name = "Star"

    def acceptVisitor(self, v):
        v.visit(self)

    def visit(self, v):
        if v.name == "Python":
            self.stage.nonActors.append(Flower(v.moveBehavior.getX(), v.moveBehavior.getY(), self.stage))
            self.stage.removeActor(self)
            self.stage.removeActor(v)

    def update(self):
        self.performMove()

    def paint(self):
        self.updateSprite()

class StarMove(MoveBehavior):
    def __init__(self, direction, x, y):
        super().__init__()
        self.direction = direction
        self.x = x + 50
        self.y = y + 75
        self.speed = 50
        self.distanceTraveled = 0
        self.advancedSpeed = 34

    def move(self, direction):
        if self.direction == "Right":
            self.x += self.speed
            self.distanceTraveled += self.speed
        if self.direction == "Left":
            self.x -= self.speed
            self.distanceTraveled += self.speed

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def resetSpeed(self):
        self.speed = 50

class StarAttack(AttackBehavior):
    def __init__(self):
        super().__init__()
        self.attackDuration = 0
    def attack(self):
        pass

class StarSprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.action = "move"
        self.direction = "Left"
        self.frame = 0
        self.spriteDict = Resources.STAR

    def move(self, direction):
        self.action = "move"
        self.direction = direction
        if self.frame > 3:
            self.frame = 0
            return self.spriteDict[self.action + self.direction][self.frame]
        else:
            self.frame += 1
            return self.spriteDict[self.action + self.direction][self.frame]
