import turtle

turtle.register_shape("doctor.gif")
turtle.register_shape("ironman.gif")
turtle.register_shape("hulk.gif")
turtle.register_shape("thor.gif")

class Protector(turtle.Turtle):
    ''' Subclass of turtle to represent a Protector in the game
    '''

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(5)
        self.goto(0, 0)
        self.seth(90)
        self.color("white")
        self.shape("circle")
