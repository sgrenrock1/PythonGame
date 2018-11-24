__author__ = 'Steve'
from Actor import Actor
from Behaviors import *
import Resources
from Tracking import *
class Python(Actor, Observer):
    def __init__(self, x, y, stage):
        super().__init__(PyMove(), PyAttack(), PySprite(), x, y, stage)
        self.stage = stage
        self.x = x
        self.y = y
        self.name = "Python"

    def acceptVisitor(self, v):
        v.visit(self)

    def visit(self, v):
        pass

    def updateDefence(self, direction):
        if direction == "Right":
            self.spriteBehavior.direction = "Right"
            self.moveBehavior.direction = "Right"
        if direction == "Left":
            self.spriteBehavior.direction = "Left"
            self.moveBehavior.direction = "Left"

    def update(self):
        self.performMove()

    def paint(self):
        self.updateSprite()

class FastPython(Python):

    def __init__(self, decorated):
        super(Python, self).__init__(PyFastMove(), decorated.attackBehavior,
                                     PyFastSprite(), decorated.x,
                                     decorated.y, decorated.stage)
        self.name = "Python"
        self.x = decorated.x
        self.y = decorated.y

class PyFastMove(MoveBehavior):
    def __init__(self):
        super().__init__()
        self.x=800
        self.y=450
        self.speed = 10
        self.advancedSpeed = 24
        self.action = "move"
        self.direction = "Left"

    def move(self, direction):
        if self.direction == "Left":
            self.x -= self.speed
        if self.direction == "Right":
            self.x += self.speed
            self.advancedSpeed = -4

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def resetSpeed(self):
        self.speed = 10

class PyMove(MoveBehavior):
    def __init__(self):
        super().__init__()
        self.x=800
        self.y=450
        self.speed = 5
        self.advancedSpeed = 19
        self.action = "move"
        self.direction = "Left"

    def move(self, direction):
        if self.direction == "Left":
            self.x -= self.speed
        if self.direction == "Right":
            self.x += self.speed
            self.advancedSpeed = -9

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def resetSpeed(self):
        self.speed = 5


class PyAttack(AttackBehavior):
    def __init__(self):
        super().__init__()
        self.attackDuration = 8

    def attack(self):
        pass

class PySprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.action = "move"
        self.direction = "Left"
        self.frame = 0
        self.spriteDict = Resources.PYTHON

    def move(self, direction):
        return self.spriteDict[self.action + self.direction][self.frame]

class PyFastSprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.action = "move"
        self.direction = "Left"
        self.frame = 1
        self.spriteDict = Resources.PYTHON

    def move(self, direction):
        return self.spriteDict[self.action + self.direction][self.frame]
