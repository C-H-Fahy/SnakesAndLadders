#AUTHOR: CHFahy
#CREATED: 2021-03-08

#Please read README.txt

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


def find_pos(n):
    """returns centre of square n
    
    n:  int
    
    returns: tuple(int, int)
    """
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


def draw_map():
    """Draws out the map
    the grid and all the snakes and ladders and numbers
    """
    #turns tracer on or off and sets drawspeed
    turtle.tracer(config.DRAW_TRACER)
    turtle.speed(config.DRAW_SPEED)
    turtle.hideturtle()
    #Finds size of one square
    gap = config.SIZE//config.GRID
    #Draw Grid        
    for i in range(0, config.GRID+1):
        #Draw Horizontal Line
        shapes.length_line((config.GRIDPOS[0], i*gap + config.GRIDPOS[1]), config.SIZE, 0)
        #Draw Verticle Line
        shapes.length_line((i*gap + config.GRIDPOS[0], config.GRIDPOS[1]), config.SIZE, 90)

    #Draws Snakes
    for i in range(0, len(config.SNAKES)):
        shapes.snake(find_pos(config.SNAKES[i][0]), find_pos(config.SNAKES[i][1]), gap/10)

    #Draws Ladders
    for i in range(0, len(config.LADDERS)):
        shapes.ladder(find_pos(config.LADDERS[i][0]), find_pos(config.LADDERS[i][1]), gap/5)

    #Draw Numbers
    for i in range(0, config.GRID ** 2):
        shapes.write_number(find_pos(i), i)
    #Reset tracer
    turtle.tracer(True)


def player_setup(player, offset, shape, title):
    """Sets up player, returns players position
    
    player: string
    offset: int
    shape:  string
    title:  string
    
    returns: int
    """
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
    (x, y) = find_pos(playerpos)
    x = x + offset
    player.setpos(x, y)
    return playerpos


def dice(move):
    """Sets dice shape to shape in config
    
    move: int
    """
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

        
def ani_delay(s):
    """Delays for s seconds
    
    s:  float
    """
    try:
        time.sleep(s)
    except NameError:
        print("WARNING: Delay Failed, likely due to time import or borked config")

        
def snake_ladder(pos, title):
    """Finds Position after snake or ladder, returns old position if on same pos
    
    pos:    int
    title:  string
    
    returns: int
    """
    #Check to see if player is on a Ladder
    for i in range (0, len(config.LADDERS)):
        if pos == config.LADDERS[i][0]:
            print(title + " gets ladder from " + str(config.LADDERS[i][0]) + " to " + 
            str(config.LADDERS[i][1]))
            #Finds new position
            return(config.LADDERS[i][1])
            #Stops more moves
    #Check to see if player is on a Snake
    for i in range (0, len(config.SNAKES)):
        if pos == config.SNAKES[i][0]:
            print(title + " gets snake from " + str(config.SNAKES[i][0]) + " to "  + 
            str(config.SNAKES[i][1]))
            #Finds new position
            return(config.SNAKES[i][1])
            #Stops more moves
    #Returns 
    return(pos)

    
def turn(player, title, pos, offset, limit):
    """Runs players turn, returns players new position
    
    player: string
    title:  string
    pos:    int
    offset: int
    limit:  int
    
    returns: int
    """
    
    #Takes input
    print("\nPlayer " + title + " is starting on " + str(pos))
    esc = input("Player "+ title + " turn(press enter): ")
    #Generates random number
    move = random.randint(1, config.ROLL)
    #Sets dice shape
    dice(move)
    #Finds current position
    pos = move + pos
    #Roll player back if rollback is enabled and they don't get the exact number
    if pos > limit and config.ROLLBACK:
        #Finds amount over
        over = pos - limit
        #finds new position using amount over
        pos = limit - over
        print("You rolled over by " + str(over) + ", bouncing back to " + str(pos))
        if pos < 0:
            pos = 0
    #Move Player to new position        
    (x, y) = find_pos(pos)
    x = x + offset
    player.setpos(x, y)
            
    #Moves to new ladder/snake position if ladder/snake is taken        
    newpos = snake_ladder(pos, title)
    if newpos != pos:
        pos = newpos
        #Delay so that taking of the snake and ladder is clear
        ani_delay(config.DELAY)
        #Move to new position
        (x, y) = find_pos(pos)
        x = x + offset
        player.setpos(x, y)
    print("Player " + title +  " is on " + str(pos))
    return(pos)


def game_start(aPlayerTitle, bPlayerTitle):
    """Starts one game, returns True if aPlayer has won

    aPlayerTitle: string
    bPlayerTitle: string
    
    returns: boolean
    """
    
    print("Rollback is: " + str(config.ROLLBACK))

    offset = config.SIZE//(config.GRID*5)
    limit = config.GRID ** 2 - 1

    #aPlayer setup
    aPlayer = turtle.Turtle()
    aPlayerpos = player_setup(aPlayer, offset, config.A_PLAYER_SHAPE, aPlayerTitle)

    #bPlayer setup
    bPlayer = turtle.Turtle()
    bPlayerpos = player_setup(bPlayer, -offset, config.B_PLAYER_SHAPE, bPlayerTitle)

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
    """SnakesAndLadders game loop"""
    #Setup screen and background
    turtle.screensize(config.SCREEN_SIZE[0], config.SCREEN_SIZE[1])
    turtle.bgcolor(config.BG_COLOR)
    #Draw Board
    draw_map()
    #Take player names
    aPlayerTitle = input("Enter player A's name: \n")
    bPlayerTitle = input("Enter player B's name: \n")
    aPlayerWins = 0
    bPlayerWins = 0
    esc = ""
    while esc != "exit":
        #Start game
        print("\nNEW GAME")
        win = game_start(aPlayerTitle, bPlayerTitle)
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

        ani_delay(config.DELAY)
        print(aPlayerTitle + " has won: " + str(aPlayerWins))
        print(bPlayerTitle + " has won: " + str(bPlayerWins))
        esc = input("Type 'exit' to exit: \n")
main()
