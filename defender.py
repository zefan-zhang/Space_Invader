import turtle

LEFT_WALL_EDGE = -295
RIGHT_WALL_EDGE = 295
turtle.register_shape("captain.gif")

class Defender(turtle.Turtle):
    ''' Subclass of turtle to represent a Defender in the game
        The denfeder will appear at the cental bottom of the turtle window, it
        with 30 pixel moveable speed
    '''
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.goto(0, -250)
        self.seth(90)
        self.shape("captain.gif")
        self.color("blue")
        self.speed = 30

    def move_left(self):
        ''' Function move_left
            Input: none
            Return: none

            Does: the defender can move left, and it cannot move furtuer when
            it hit the left wall
        '''
        x = self.xcor()
        x -= self.speed
        if x < LEFT_WALL_EDGE:
            x = LEFT_WALL_EDGE
        self.setx(x)


    def move_right(self):
        ''' Function move_right
            Input: none
            Return: none

            Does: the defender can move right, and it cannot move furtuer when
            it hit the right wall
        '''
        x = self.xcor()
        x += self.speed
        if x > RIGHT_WALL_EDGE:
            x = RIGHT_WALL_EDGE
        self.setx(x)

        
        

