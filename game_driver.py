'''
    CS5001
    Spring 2019
    HW7
    MyName: Zefan Zhang
    Today's data Apr 11, 2019
'''


from defender import Defender
from frame import Frame
from attacker import Attacker
from weapon import Weapon
from score import Score
from protector import Protector
import turtle
import os

NUMBER_OF_ATTACKERS = 10
TOTAL_GAME_LEVEL = 15
PER_HIT_POINT = 10


defender = Defender()
weapon = Weapon("ready")
score = Score()
topscore = Score()


def get_attacker_lst(num):
    ''' Function get_attacker_lst
        Input: an integer
        Return: a list

        Does: creat an empty list, and add attacers to the list, the number
        of attackers based on the input integer.
    '''
    attackers = []
    for i in range(num):
        attackers.append(Attacker())
    return attackers


def throw_shield():
    ''' Function throw_shield
        Input: none
        Return: none

        Does: check the state of the weapon, if the state is ready, it plays
        sound effect(only in OS system), and change the state from ready to fire
        , the weapon will appear at a 10 pixel top above the defender
    '''
    if weapon.state == "ready":
        os.system("afplay throw.wav&")
        weapon.state = "fire"
    x = defender.xcor()
    y = defender.ycor() + 10
    weapon.goto(x, y)
    weapon.showturtle()

def is_hit(p1, p2):
    ''' Function is_hit
        Input: two turtle objects
        Return: Boolean

        Does: check two objects whether collision or not, it is collision,
        return True, otherwise return False.
    '''
    a = (p1.xcor() - p2.xcor()) ** 2
    b = (p1.ycor() - p2.ycor()) ** 2
    distance = (a + b) ** 1/2
    if distance < 500:
        return True
    else:
        return False

def main():
    #Set up the screen
    sc = turtle.Screen()
    sc.bgpic("background.gif")

    #Draw the main game frame
    frame = Frame()
    frame.draw()
    
    #Draw the score
    score.update()
    topscore.goto(0,315)
    topscore.topscore()

    #Set the protector doctor_strange
    doctor_strange = Protector()
    doctor_strange.shape("doctor.gif")
    doctor_strange.goto(-240, -140)
    
    #Set the protector iron_man
    iron_man = Protector()
    iron_man.shape("ironman.gif")
    iron_man.goto(-80, -140)
    
    #Set the protector thor
    thor = Protector()
    thor.shape("thor.gif")
    thor.goto(80, -140)
    
    #Set the protector hulk
    hulk = Protector()
    hulk.shape("hulk.gif")
    hulk.goto(240, -140)
    
    #Keyboard binding
    turtle.listen()
    turtle.onkey(defender.move_left, "Left")
    turtle.onkey(defender.move_right, "Right")
    turtle.onkey(throw_shield, "space")
    
    #Innitialize the start at level
    level = 1

    #Use a for loop to make the game have multiple levels
    for i in range(TOTAL_GAME_LEVEL):
        
        #Put the protectors in a list
        protectors = [doctor_strange, iron_man, thor, hulk]
        
        #Call the get_attacker_lst function and creat an attackers list
        attackers = get_attacker_lst(NUMBER_OF_ATTACKERS)

        #The while loop will keep running until the defender disappear
        while defender.isvisible():
            
            #Move the weapon
            if weapon.state == "fire":
                weapon.move()
                
            #Set 10 attackers move in a random speed    
            for attacker in attackers:
                attacker.move()
                
                #Check the attacker, if it is out of the bottom boader,
                #remover it from the list
                if attacker.isvisible() == False:
                    attackers.remove(attacker)

                #Check for a collision between the weapon and the attacker
                if is_hit(weapon, attacker):
                    
                    #Play the sound, when weapon hit attacker
                    #The sound only can paly in a OS system
                    os.system("afplay scream.wav&")
                    
                    #Reset the weapon
                    weapon.hideturtle()
                    weapon.state = "ready"
                    weapon.goto(defender.xcor(), defender.ycor())
                    
                    #Reset the attackers
                    attacker.hideturtle()
                    
                    #Add socre when hit one attacker
                    score.change(PER_HIT_POINT)
                    
                    #Remove the attacker who was been hited from the list
                    attackers.remove(attacker)
                

                #Check for a collision between the defender and the attacker
                #If two objects is a collision, break the for loop
                if is_hit(defender, attacker):
                    #if it is a collision, the defender and the attacker
                    #becoming invisible
                    defender.hideturtle()
                    attacker.hideturtle()
                    break

                #Use a for loop to check for the states between the protector,
                #the weapon, and attacker
                for hero in protectors:
                    if is_hit(hero, attacker):
                        os.system("afplay scream.wav&")
                        hero.hideturtle()
                        attacker.hideturtle()
                        protectors.remove(hero)
                        attackers.remove(attacker)

                    if is_hit(weapon, hero):
                        weapon.hideturtle()
                        weapon.state = "ready"
                        weapon.goto(defender.xcor(), defender.ycor())
                
            #If the 10 attackers disappear, palying a applause sound, and add
            #one more level
            if len(attackers) == 0:     
                level += 1
                os.system("afplay applause.wav&")
                #If the current level is less or equal to the TOTAL_GAME_LEVEL
                #the game will move the next level, and report to the player
                #what the next level is, also reset the attacker and protector
                if level <= TOTAL_GAME_LEVEL:
                    print("Congrats! Move to next level, level:", level)
                    invisible_hero = [doctor_strange, iron_man, thor, hulk]
                    for i in range(len(invisible_hero)):
                        invisible_hero[i].showturtle()
                    protectors = invisible_hero
                    
                #If the player complete the total 15 levels, they win the entire
                #game, the game end.
                elif level > TOTAL_GAME_LEVEL:
                    print("The Avengers save the world:)!!!")
                break
            
        #The the defender disappear, the game over, and report the the player
        #he or she lose the game
        if defender.isvisible() == False:
            os.system("afplay boos.wav&")
            print ("Thanos destory the world:(")
            break


    #Call the is top method in Score class to check whether the player
    #break the recored  
    if score.istop():
        
        #Prompt the player to enter his or her name when the player become a
        #new recored maker
        yourname = input("Congras,your just created a new record, "
                         "please enter your name!\n")
        
        #Call the writesocre in the Score class
        #overwrite new recored maker's name and socre in "socre.txt" file
        score.writesocre(yourname)

main()
