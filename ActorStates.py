__author__ = 'Steve'

class ActorState(object):
    def __init__(self):
        super().__init__()

    def stand(self):
        pass
    def walk(self):
        pass
    def attack(self):
        pass

class Standing(ActorState):
    def __init__(self, actor):
        super().__init__()
        self.actor = actor

    def stand(self):
        print("You are standing")

    def walk(self):
        print("You are walking")
        self.actor.state = Walking(self.actor)

    def attack(self):
        if self.actor.attackBehavior.attackPower <= 0:
            print("Can't Attack")
        else:
            print("Now attacking")
            self.actor.state = Attacking(self.actor)

class Walking(ActorState):
    def __init__(self, actor):
        super().__init__()
        self.actor = actor

    def stand(self):
        print("You are standing")
        self.actor.state = Standing(self.actor)

    def walk(self):
        print("You are walking")

    def attack(self):
        if self.actor.attackBehavior.attackPower <= 0:
            print("Can't Attack")
        else:
            print("Now attacking")
            self.actor.state = Attacking(self.actor)

class Attacking(ActorState):
    def __init__(self, actor):
        super().__init__()
        self.actor = actor

    def stand(self):
        print("You're already standing")

    def walk(self):
        print("Can't walk while attacking")

    def attack(self):
        print("You're already Attacking")









