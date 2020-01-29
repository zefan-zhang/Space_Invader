import turtle

class Frame(turtle.Turtle):

    def __init__(self):
        ''' Subclass of turtle to represent the Frame in the game
            The frame with 3 pixel size width, color red
        '''
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("red")
        self.pensize(3)
        self.goto(-310, -310)
        self.pendown()
        

    def draw(self):
        ''' Function draw
            Input: none
            Return: none

            Does: draw a 620*620 pixel boarder for the game
        '''
        for i in range(4):
            self.fd(620)
            self.lt(90)

