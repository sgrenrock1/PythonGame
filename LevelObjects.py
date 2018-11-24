__author__ = 'Steve'
from Behaviors import SpriteBehavior, MoveBehavior
import Resources
"""
These classes follow a pattern similar to Actor.
The only difference is no attack behaviour.
"""
class LevelObject(object):
    def __init__(self, moveBehavior, spriteBehavior, x, y, stage):
        super().__init__()
        self.stage = stage
        self.moveBehavior = moveBehavior
        self.spriteBehavior = spriteBehavior
        self.moveBehavior.x = x
        self.moveBehavior.y = y
        self.surface = None

    def collision(self, a):
        pass

    def acceptVisitor(self, v):
        pass

    def visit(self, a):
        pass

    def attack(self, a):
        pass

    def getAttacked(self, a):
        pass

    def performMove(self):
        self.moveBehavior.move()

    def updateSprite(self):
        """
        Accesses the spriteBehavior dictionary
         Goes the entry with the matching action and direction
          Selects the correct frame
        Takes the x and y values from the moveBehavior
        Uses Stage.blit() to add the sprite to the image
        """
        self.surface = self.spriteBehavior.spriteDict[self.spriteBehavior.location]
        pos = (self.moveBehavior.x, self.moveBehavior.y)
        self.stage.blit(self.surface, pos)

class Ground(LevelObject):
    def __init__(self, x, y, stage):
        super().__init__(GroundMove(), GroundSprite(), x, y, stage)
        self.name = "Ground"

    def update(self):
        self.performMove()

    def paint(self):
        self.updateSprite()

class Flower(LevelObject):
    def __init__(self, x, y, stage):
        super().__init__(GroundMove(), FlowerSprite(), x, y, stage)
        self.name = "Flower"

    def update(self):
        self.performMove()

    def paint(self):
        self.updateSprite()

class FlowerSprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.location = "forest"
        self.spriteDict = Resources.FLOWER

    def move(self):
        return self.spriteDict[self.location]


class GroundMove(MoveBehavior):
    def __init__(self):
        super().__init__()
        self.x = 800
        self.y = 525
        self.speed = 0
        self.advancedSpeed = 16

    def move(self):
        self.x -= self.speed

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def resetSpeed(self):
        self.speed = 0

class GroundSprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.location = "forest"
        self.spriteDict = Resources.GROUND

    def move(self):
        return self.spriteDict[self.location]

class BackDrop(LevelObject):
    def __init__(self, x, y, stage):
        super().__init__(BackDropMove(), BackDropSprite(), x, y, stage)
        self.name = "BackDrop"

    def collision(self, a):
        pass

    def visit(self, a):
        pass

    def update(self):
        self.performMove()

    def paint(self):
        self.updateSprite()

class BackDropMove(MoveBehavior):
    def __init__(self):
        super().__init__()
        self.x = 800
        self.y = 525
        self.speed = 0
        self.advancedSpeed = 1

    def move(self):
        self.x -= self.speed

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def resetSpeed(self):
        self.speed = 0

class BackDropSprite(SpriteBehavior):
    def __init__(self):
        super().__init__()
        self.location = "forest"
        self.spriteDict = Resources.BACK_DROP

    def move(self):
        return self.spriteDict[self.location]

