Steven Grenrock, TermProject (2013-06-06)

Dependencies:
-Python 3.2
-pygame for Python 3.2


Pattern Use:
Strategy Pattern(seen in Actor.py, Behaviors.py, LevelObjects.py, Rabbit.py, Python.py, Star.py) -
    Each "Actor" object has a MoveBehavior, AttackBehavior, and SpriteBehavior.
	MoveBehavior controls the position and speed of objects.
	AttackBehavior controls what occurs on screen when an attack is actuated
		and the duration of the attack.
	SpriteBehavior controls which sprite should appear on screen based on the actor's action and direction.
	    Animation are played by traversing through a list of frames.

Observer Pattern(seen in Tracking.py, Python.py, Rabbit.py) - Python(an actual snake) objects observe Rabbit.
    They are told to change direction if Rabbit attacks towards them.

Decorator Pattern(seen in Python.py) - Gives the ability to create a Python object with different strategies.
    In this game the base Python(green) can be decorated to move faster and have a purple color.

State Pattern(seen in ActorStates.py, Rabbit.py) - Prints out what the Rabbit is doing.
    What gets printed out varies with what the Rabbit is doing.

Visitor Pattern(seen in Stage_driver.py(def checkCollisions), Python.py, Rabbit.py, Star.py) - When two sprites overlap,
	they each visit the other.


Operation:
Run Stage_driver.py
Use the left and right arrow keys to move the player around.
Press 'A' to attack.






