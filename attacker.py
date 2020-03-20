import turtle
import random

LEFT_WALL_EDGE = -295
RIGHT_WALL_EDGE = 295
turtle.register_shape("thanos.gif")


class Attacker(turtle.Turtle):
    ''' Subclass of turtle to represent a Attacker in the game
        A Attacker will appear at a random postion on the turtle window, it
        with 70 pixel godown speed
    '''

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.color("red")
        self.shape("thanos.gif")
        self.goto(random.randint(-295, 295), random.randint(150, 280))
        self.godown = 70

    def move(self):
        ''' Function move
            Input: none
            Return: none

            Does: when the attackers hit the right wall, it reappears on the
            left wall and moves down
        '''
        x = self.xcor()
        y = self.ycor()
        x += random.randint(0, 10)
        if x > RIGHT_WALL_EDGE:
            x = LEFT_WALL_EDGE
            y -= self.godown
            
        if y < LEFT_WALL_EDGE:
            self.hideturtle()
            
        self.goto(x, y)
