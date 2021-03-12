#AUTHOR: CHFahy
#CREATED: 2021-03-08

#External modules
import turtle
import random
try: 
    import time
except ModuleNotFoundError:
    print("WARNING: Failed to import time, Attempting to proceed")

#Internal modules
import shapes
import config1 as config

#Import other configs as config if other configs are picked
mode = input("Enter 1(or anything else) for config1.py (default) or 2 for config2.py(mode 2): \n")
if mode == "2":
    print("using config2.py")
    try: 
        import config2 as config
    except ModuleNotFoundError:
        print("WARNING: config2.py not found, using config1.py")

def FindPos(n):
    """Finds centre of square"""
    #This should be more efficent than for loop(at the cost of some readability)
    gap = config.SIZE//config.GRID

    row = n // config.GRID
    y = row * gap + gap//2 + config.GRIDPOS[1]
    if row & 1:
        #Flips if odd row
        x = -((n % config.GRID) * gap + gap//2) + config.SIZE + config.GRIDPOS[0]
    else:
        #Doesn't flip if not odd row
        x = (n % config.GRID) * gap + gap//2 + config.GRIDPOS[0]
    return(x, y)
    
    
def DrawMap():
    """Draws Out All The Fixed Stuff"""
    turtle.speed(config.DRAW_SPEED)
    turtle.hideturtle()
    gap = config.SIZE//config.GRID
    #Draw Grid        
    for i in range(0, config.GRID+1):
        #Draw Horizontal Line
        shapes.LengthLine((config.GRIDPOS[0], i*gap + config.GRIDPOS[1]), config.SIZE, 0)
        #Draw Verticle Line
        shapes.LengthLine((i*gap + config.GRIDPOS[0], config.GRIDPOS[1]), config.SIZE, 90)
    #Draw Numbers
    for i in range(0, config.GRID ** 2):
        shapes.WriteNumber(i, FindPos(i),  gap//4)
    #Draws Snakes
    for i in range(0, len(config.SNAKES)):
        shapes.snake(FindPos(config.SNAKES[i][0]), FindPos(config.SNAKES[i][1]), gap//10)
    #Draws Ladders
    for i in range(0, len(config.LADDERS)):
        shapes.ladder(FindPos(config.LADDERS[i][0]), FindPos(config.LADDERS[i][1]), gap//5)

def PlayerSetup(player, offset, shape, title):
    """Sets up player, returns players position"""
    try:
        #Sets players shape
        turtle.register_shape(shape)
        player.shape(shape)
    except turtle.TurtleGraphicsError:
        #If Turtle can't set the players shape
        print("WARNING: " + shape + " is probably missing or invalid")
    print("Player " + title + " is " + shape) 
    player.penup()
    player.speed(config.MOVE_SPEED)
    playerpos = config.STARTPOS
    (x, y) = FindPos(playerpos)
    x = x + offset
    player.setpos(x, y)
    return playerpos

def dice(move):
    try:
        #Sets dice shape
        turtle.register_shape(config.DICE[move])
        turtle.shape(config.DICE[move]) 
        turtle.showturtle()
    except turtle.TurtleGraphicsError:
        #If Turtle can't set the dice shape
        print("WARNING: " + config.DICE[move] + " is probably missing or invalid")
        turtle.hideturtle()
    except IndexError or NameError:
        print("WARNING: Not enough dice in config.DICE")
        turtle.hideturtle()
    finally:
        print("Roll is: " + str(move + 1))
    
def turn(player, title, pos, offset):
    """Runs players turn, returns players new position"""
    esc = input("Player "+ title + " turn:\n")
    move = random.randint(0, config.ROLL - 1)
    dice(move)
    
    #Move Player
    pos = move + pos + 1
    (x, y) = FindPos(pos)
    x = x + offset
    player.setpos(x, y)
        
    #Check to see if player is on Ladder and move them if they are
    for i in range (0, len(config.LADDERS)):
        if pos == config.LADDERS[i][0]:
            print(title + " gets ladder from " + str(config.LADDERS[i][0]) + " to " + 
            str(config.LADDERS[i][1]))
            
            try:
                time.sleep(config.DELAY)
            except NameError:
                print("WARNING: Delay Failed, likely due to time import or borked config")

            pos = config.LADDERS[i][1]
            (x, y) = FindPos(pos)
            x = x + offset
            player.setpos(x, y)
            
    #Check to see if player is on Snake and move them if they are
    for i in range (0, len(config.SNAKES)):
        if pos == config.SNAKES[i][0]:
            print(title + " gets snake from " + str(config.SNAKES[i][0]) + " to "  + 
            str(config.SNAKES[i][1]))
            
            try:
                time.sleep(config.DELAY)
            except NameError:
                print("WARNING: Delay Failed, likely due to time import or borked config")
                
            pos = config.SNAKES[i][1]
            (x, y) = FindPos(pos)
            x = x + offset
            player.setpos(x, y)
            
    return(pos)
    

def GameStart(aPlayerTitle, bPlayerTitle):
    offset = (config.SIZE//5)//config.GRID
    limit = config.GRID ** 2 - 1

    #aPlayer setup
    aPlayer = turtle.Turtle()
    aPlayerpos = PlayerSetup(aPlayer, offset, config.A_PLAYER_SHAPE, aPlayerTitle)

    #bPlayer setup
    bPlayer = turtle.Turtle()
    bPlayerpos = PlayerSetup(bPlayer, -offset, config.B_PLAYER_SHAPE, bPlayerTitle)
    
    #diceTurtle setup
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(config.DICEPOS)

    while True:
        aPlayerpos = turn(aPlayer, aPlayerTitle, aPlayerpos, offset)
        if aPlayerpos >= limit:
            print("Player " + aPlayerTitle +  " wins")
            break

        bPlayerpos = turn(bPlayer, bPlayerTitle, bPlayerpos, -offset)
        if bPlayerpos >= limit:
            print("Player " + bPlayerTitle +  " wins")
            break
            
def main():
    turtle.screensize(1250, 1250)
    DrawMap()
    GameStart("A", "B")
main()

