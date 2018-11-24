__author__ = 'Steve'
from Behaviors import *
class Actor(object):
    def __init__(self, moveBehavior, attackBehavior, spriteBehavior, x, y, stage):
        super().__init__()
        self.stage = stage
        self.moveBehavior = moveBehavior
        self.attackBehavior = attackBehavior
        self.spriteBehavior = spriteBehavior
        self.attackDuration = self.attackBehavior.attackDuration
        self.moveBehavior.x = x
        self.moveBehavior.y = y
        self.performingAttack = False
        self.surface = None
        self.i = 0

    def setRight(self):
        self.spriteBehavior.direction = "Right"

    def setLeft(self):
        self.spriteBehavior.direction = "Left"

    def performMove(self):
        self.moveBehavior.move(self.spriteBehavior.direction)
        self.spriteBehavior.move(self.spriteBehavior.direction)

    def performStop(self):
        self.spriteBehavior.stop()

    def performJump(self):
        self.moveBehavior.jump()
        self.spriteBehavior.jump()

    def setFrameToZero(self):
        self.spriteBehavior.frame = 0

    def performAttack(self, attackFrame, direction):
        """
        This method is called while an attack is occurring.
        It ensures that the animation for an attack is played all the way through
        """
        if self.spriteBehavior.frame == attackFrame:
            self.attackBehavior.attack(direction, self.moveBehavior.getX(), self.moveBehavior.getY(), self.stage)
        self.spriteBehavior.attack(direction)
        self.attackDuration -= 1
        self.setPerformingAttack(direction)

    def setPerformingAttack(self, direction):
        """
        If the attack is finished:
            Brings the sprite frame to 0 once the attack is finished.
            Brings the spite duration to the value indicated in the object's AttackBehavior
        Else:
            Advances the attack frame forward by 1
        """
        if self.attackDuration == 0:
            self.performingAttack = False
            self.setFrameToZero()
            self.attackDuration = self.attackBehavior.attackDuration
        else:
            self.performingAttack = True
            self.spriteBehavior.frame += 1


    def removeActor(self):
        self.stage.removeActor(self)

    def getDirection(self):
        return self.spriteBehavior.direction

    def setAttackBehavior(self, ab):
        self.attackBehavior = ab

    def setOffScreenSpeed(self):
        self.moveBehavior.speed = 16

    def updateSprite(self):
        """
        Accesses the spriteBehavior dictionary
         Goes the entry with the matching action and direction
          Selects the correct frame
        Takes the x and y values from the moveBehavior
        Uses Stage.blit() to add the sprite to the image
        """
        self.surface = self.spriteBehavior.spriteDict[self.spriteBehavior.action + self.spriteBehavior.direction][self.spriteBehavior.frame]
        pos = (self.moveBehavior.x, self.moveBehavior.y)
        self.stage.blit(self.surface, pos)












