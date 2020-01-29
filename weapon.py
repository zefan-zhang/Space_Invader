import turtle


turtle.register_shape("shield.gif")

class Weapon(turtle.Turtle):
    ''' Subclass of turtle to represent a Weapon in the game
        The weapon go to the central bottom of the turtle screen, but is
        invisible at the begaining, its moving speed is 50 pixel, and its state
        is ready to fight
    '''

    def __init__(self, state = "ready"):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, -295)
        self.shape("shield.gif")
        self.color("yellow")
        self.speed = 50
        self.seth(90)
        self.state = state

        
    def move(self):
        ''' Function move
            Input: none
            Return: none

            Does: move the weapon, it the weapon state is fire, it will move up
            at the speed that gives on __init__, and it the it gone out of the
            top boarder, it will become invisiable, and change its state as
            ready again, waiting for the next command
        '''
        if self.state == "fire":
            y = self.ycor()
            y += self.speed
            self.sety(y)
            if self.ycor() > 300:
                self.hideturtle()
                self.state = "ready"
