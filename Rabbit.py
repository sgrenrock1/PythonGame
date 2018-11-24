__author__ = 'Steve'
from Actor import Actor
from Behaviors import *
import Resources
from Star import Star
from Tracking import *
from ActorStates import *
class Rabbit(Actor, Observable):
    def __init__(self, x, y, stage):
        super().__init__(RabMove(), RabAttack(), RabSprite(), x, y, stage)
        self.controllers = stage.controllers
        self.name = "Rabbit"
        self._observers = []
        self.standing = Standing(self)
        self.walking = Walking(self)
        self.attacking = Attacking(self)
        self.state = self.standing

    def acceptVisitor(self, v):
        v.visit(self)

    def visit(self, v):
        pass

    def addObserver(self, observer):
        self._observers.append(observer)

    def notifyAttacking(self):
        for observer in self._observers:
            if observer.moveBehavior.x <= 800:
                observer.updateDefence(self.spriteBehavior.direction)

    def update(self):
        if self.performingAttack:
            self.notifyAttacking()
            self.performAttack(3, self.spriteBehavior.direction)
            self.state.attack()
        else:
            self.handleInput()
            self.state = self.standing

    def handleInput(self):
        """handles the key events"""
        if self.controllers.K_RIGHT:
            self.setRight()
            self.performMove()
            self.state.walk()
        if self.controllers.K_LEFT:
            self.setLeft()
            self.performMove()
            self.state.walk()
        if self.controllers.K_a:
            self.setFrameToZero()
            self.performAttack(4, self.getDirection())
            self.state.attack()
        if self.controllers.K_LEFT == False and self.controllers.K_RIGHT == False:
            self.performStop()
            self.state.stand()
        if self.controllers.QUIT:
            self.stage.quit()

    def paint(self):
        self.updateSprite()

class RabMove(MoveBehavior):
    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 350
        self.speed = 25.25
        self.distanceTraveled = 0
        self.atEdge = False
        self.maxX = 225

    def move(self, direction):
        """
        Moves the sprite across the screen
        Stops the sprite at a certain point
        """
        if direction == "Right":
            if self.x < self.maxX:
                self.x += self.speed
            else:
                self.distanceTraveled += self.speed
                self.atEdge = True

        if direction == "Left":
            if self.x > 50:
                self.x -= self.speed

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDistanceTraveled(self):
        return self.distanceTraveled

class RabAttack(AttackBehavior):
    def __init__(self):
        super().__init__()
        self.attackDuration = 7
        self.attackPower = 50

    def attack(self, direction, x, y, stage):
        if self.attackPower > 0:
            stage.otherActors.append(Star(direction, x+35, y+65, stage))
            self.attackPower -= 1
        else:
            pass

class RabSprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.spriteDict = Resources.RABBIT
        self.frame = 0
        self.action = "walk"
        self.direction = "Right"

    def stop(self):
        self.action = "stand"
        self.frame = 0
        return self.spriteDict[self.action + self.direction][self.frame]

    def move(self, direction):
        self.action = "walk"
        self.direction = direction
        if self.frame > 6:
            self.frame = 0
            return self.spriteDict[self.action + self.direction][self.frame]
        else:
            self.frame += 1
            return self.spriteDict[self.action + self.direction][self.frame]

    def attack(self, direction):
        self.action = "attack"
        self.direction = direction
        return self.spriteDict[self.action + self.direction][self.frame]
