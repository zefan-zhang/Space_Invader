import turtle


class Score(turtle.Turtle):
    ''' Subclass of turtle to represent Score in the game
        The score's color is white, it located at the left of the top border,
        and the socre start off with 0
    '''

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-310, 315)
        self.score = 0


    def update(self):
        ''' Function update
            Input: none
            Return: none

            Does: update the socre, use the new socre to replace the old score
        '''
        self.clear()
        self.write("Your Score: {}".format(self.score), align = "left",
                   font = ("Arial", 16, "normal"))
        
    def change(self, points):
        ''' Function change
            Input: none
            Return: none

            Does: add the point when the player hits one attacker, and update
            the score on the screen
        '''
        self.score += points
        self.update()
        
    def readfile(self):
        ''' Function readfile
            Input: none
            Return: a dictionary or False

            Does: open and read the score.txt file, take out the data, and return
            a dictionay, key: player's name, value: score. If cannot open, the
            function will return Flase.
        '''
        try:
            infile = open("score.txt", "r")
            all_data = infile.read()
            infile.close()
            lines = all_data.split()
            record = {}
            name = ""
            for i in range(len(lines) - 1):
                name += " " + lines[i]
            record[name] = lines[-1]
            return record
        except OSError:
            return False

    def topscore(self):
        ''' Function topscore
            Input: none
            Return: none

            Does: write the record maker's name and socre on the top center 
        '''
        top = self.readfile()
        for key, value in top.items():
            self.write("Top Score:" + key + " -- " + str(value),
                       align = "center", font = ("Arial", 16, "normal"))
            
                           
    def istop(self):
        ''' Function istop
            Input: none
            Return: none

            Does: check the play whether break the recored or not, if the player
            break the recored, the function return True.
        '''
        top = self.readfile()
        for value in top.values():
            if self.score > int(value):
                return True

    def writesocre(self, name):
        ''' Function writesocre
            Input: player's name
            Return: Boolean

            Does: open the score.txt file, and overwrite the new recored maker's
            name and socre to the file, and return True. If faces OSError, it
            will return False.
        '''       
        try:
            outfile = open("score.txt", "w")
            outfile.write(name + " " + str(self.score))
            outfile.close()
            return True
        except OSError:
            return False
