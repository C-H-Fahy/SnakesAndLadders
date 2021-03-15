#AUTHOR: CHFahy
#CREATED: 2021-03-08

#External modules
import turtle
import random
try: 
    import time
    #The code will be able to run without time being imported correctly
except ModuleNotFoundError:
    print("WARNING: Failed to import time, Attempting to proceed")

#Internal modules
import shapes
import config1 as config

#Import other configs as config if other configs are picked
mode = input("Enter 1(or anything else) for config1.py (default) or 2 for config2.py(mode 2): \n")
if mode == "2":
    try: 
        import config2 as config
        print("using config2.py")
    except ModuleNotFoundError:
        print("WARNING: config2.py not found, using config1.py")

def FindPos(n):
    """Finds centre of square"""
    #This should be more efficent than for loop(at the cost of some readability)
    
    #Calculates row using floor division
    y = (n // config.GRID)
    #Calculates column(as x) using modulus
    if y & 1:
        #Flips column if odd row using using a really efficent trick by 
        #modulus after Bitwise NOTing n
        x = (~n % config.GRID) 
    else:
        #Doesn't flip if not odd row
        x = (n % config.GRID)
              
    #Finds size of one square
    gap = config.SIZE//config.GRID
    #transforms column(x) and row(y)to x and y cord
    x = x * gap + gap//2 + config.GRIDPOS[0]
    y = y * gap + gap//2 + config.GRIDPOS[1]
    return(x, y)


def DrawMap():
    """Draws Out All The Fixed Stuff"""
    #Turns tracer on or off and sets drawspeed
    turtle.tracer(config.DRAW_TRACER)
    turtle.speed(config.DRAW_SPEED)
    turtle.hideturtle()
    #Finds size of one square
    gap = config.SIZE//config.GRID
    #Draw Grid        
    for i in range(0, config.GRID+1):
        #Draw Horizontal Line
        shapes.LengthLine((config.GRIDPOS[0], i*gap + config.GRIDPOS[1]), config.SIZE, 0)
        #Draw Verticle Line
        shapes.LengthLine((i*gap + config.GRIDPOS[0], config.GRIDPOS[1]), config.SIZE, 90)

    #Draws Snakes
    for i in range(0, len(config.SNAKES)):
        shapes.snake(FindPos(config.SNAKES[i][0]), FindPos(config.SNAKES[i][1]), gap/10)

    #Draws Ladders
    for i in range(0, len(config.LADDERS)):
        shapes.ladder(FindPos(config.LADDERS[i][0]), FindPos(config.LADDERS[i][1]), gap/5)

    #Draw Numbers
    for i in range(0, config.GRID ** 2):
        shapes.WriteNumber(i, FindPos(i))

    turtle.tracer(True)

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
        turtle.register_shape(config.DICE[move - 1])
        turtle.shape(config.DICE[move - 1]) 
        turtle.showturtle()
    except turtle.TurtleGraphicsError:
        #If Turtle can't set the dice shape
        print("WARNING: " + config.DICE[move - 1] + " is probably missing or invalid")
        turtle.hideturtle()
    except IndexError or NameError:
        print("WARNING: Not enough dice in config.DICE")
        turtle.hideturtle()
    finally:
        print("Roll is: " + str(move))
        
def AniDelay():
    try:
        time.sleep(config.DELAY)
    except NameError:
        print("WARNING: Delay Failed, likely due to time import or borked config")
    
def turn(player, title, pos, offset, limit):
    """Runs players turn, returns players new position"""
    esc = input("Player "+ title + " turn(press enter):\n")
    move = random.randint(1, config.ROLL)
    dice(move)
    
    #Roll player back if rollback is enabled and they don't get the exact number
    pos = move + pos
    if pos > limit and config.ROLLBACK:
        pos = pos - move*2
        if pos < 0:
            pos = 0

    #Move Player to new position        
    (x, y) = FindPos(pos)
    x = x + offset
    player.setpos(x, y)

    #Sets flag
    slFlag = True

    #Check to see if player is on a Ladder and sets new position
    #Only one Snake and Ladder can be taken per turn to avoid weirdness
    for i in range (0, len(config.LADDERS)):
        if pos == config.LADDERS[i][0] and slFlag:
            print(title + " gets ladder from " + str(config.LADDERS[i][0]) + " to " + 
            str(config.LADDERS[i][1]))
            #Finds new position
            pos = config.LADDERS[i][1]
            #Stops more moves
            slFlag = False
    #Check to see if player is on a Snake
    for i in range (0, len(config.SNAKES)):
        if pos == config.SNAKES[i][0] and slFlag:
            print(title + " gets snake from " + str(config.SNAKES[i][0]) + " to "  + 
            str(config.SNAKES[i][1]))
            #Finds new position
            pos = config.SNAKES[i][1]
            #Stops more moves
            slFlag = False
            
    #Moves to new ladder/snake position if ladder/snake is taken        
    if not(slFlag):
        #Delay so that taking of the snake and ladder is clear
        AniDelay()
        #Move to new position
        (x, y) = FindPos(pos)
        x = x + offset
        player.setpos(x, y)
        
    print("Player " + title +  " is on " + str(pos))
    return(pos)

def GameStart(aPlayerTitle, bPlayerTitle):
    """Starts one game, returns True if aPlayer has won"""
    offset = config.SIZE//(config.GRID*5)
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
        aPlayerpos = turn(aPlayer, aPlayerTitle, aPlayerpos, offset, limit)
        if aPlayerpos >= limit:
            print("Player " + aPlayerTitle +  " wins")
            return(True)
            break

        bPlayerpos = turn(bPlayer, bPlayerTitle, bPlayerpos, -offset, limit)
        if bPlayerpos >= limit:
            print("Player " + bPlayerTitle +  " wins")
            return(False)
            break

def main():
    #Setup screen and background
    turtle.screensize(config.SCREEN_SIZE[0], config.SCREEN_SIZE[1])
    turtle.bgcolor(config.BG_COLOR)
    #Draw Board
    DrawMap()
    #Take player names
    aPlayerTitle = input("Enter player A's name: \n")
    bPlayerTitle = input("Enter player B's name: \n")
    aPlayerWins = 0
    bPlayerWins = 0
    esc = ""
    while esc != "exit":
        #Start game
        print("NEW GAME")
        win = GameStart(aPlayerTitle, bPlayerTitle)
        if win:
            aPlayerWins = aPlayerWins + 1
        else:
            bPlayerWins = bPlayerWins + 1

        try:
            #Sets turtle/dice to WIN_SHAPE
            turtle.register_shape(config.WIN_SHAPE)
            turtle.shape(config.WIN_SHAPE)
            #Move to centre
            turtle.setpos(config.GRIDPOS[0] + config.SIZE//2, config.GRIDPOS[1] + config.SIZE//2)
            #reveals turtle
            turtle.showturtle()
        except turtle.TurtleGraphicsError:
            #If Turtle can't set the dice shape
            print("WARNING: " + config.WIN_SHAPE + " is probably missing or invalid")
            turtle.hideturtle()
        except NameError:
            print("WARNING: config.Win_SHAPE not set")
            turtle.hideturtle()

        AniDelay()
        print(aPlayerTitle + " has won: " + str(aPlayerWins))
        print(bPlayerTitle + " has won: " + str(bPlayerWins))

        esc = input("Type 'exit' to exit: \n")
main()
