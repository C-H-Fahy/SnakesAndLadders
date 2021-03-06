#AUTHOR: CHFahy
#CREATED: 2021-03-08

#Please read README.txt

#External modules
import turtle
import random
import time

#Internal modules
import shapes
import config1 as config



def find_cord(n: int) -> tuple:
    """returns centre of square n
    """
    #This should be more efficent than for loop
    #(at the cost of some readability)

    #Calculates row using floor division
    y = n // config.GRID
    #Calculates column(as x) using modulus
    if y & 1:
        #Flips column if odd row using by modulus after Bitwise NOT n
        x = ~n % config.GRID
    else:
        #Doesn't flip if not odd row
        x = n % config.GRID
              
    #Finds size of one square
    gap = config.SIZE//config.GRID
    #transforms column(x) and row(y)to x and y cord
    x = x * gap + gap//2 + config.GRIDPOS[0]
    y = y * gap + gap//2 + config.GRIDPOS[1]
    return(x, y)


def draw_map():
    """Draws out everything
    including the grid and all the snakes and ladders and numbers
    """
    #turns tracer on or off and sets drawspeed
    turtle.tracer(config.DRAW_TRACER)
    turtle.speed(config.DRAW_SPEED)
    turtle.hideturtle()
    #Finds size of one square
    gap = config.SIZE//config.GRID

    #Draw Grid        
    shapes.grid(config.GRIDPOS, config.GRID, gap)

    #Draws Snakes
    for i in range(0, len(config.SNAKES)):
        shapes.snake(find_cord(config.SNAKES[i][0]), find_cord(config.SNAKES[i][1]), gap//10)

    #Draws Ladders
    for i in range(0, len(config.LADDERS)):
        shapes.ladder(find_cord(config.LADDERS[i][0]), find_cord(config.LADDERS[i][1]), gap//5)

    #Draw Numbers
    for i in range(0, config.GRID ** 2):
        shapes.write_number(find_cord(i), i)

    #Reset tracer and drawspeed
    turtle.tracer(True)
    turtle.speed(0)


def player_setup(player: object, offset: int, shape: str, title: str) -> int:
    """Sets up player, returns players position
    """
    try:
        #Sets players shape
        turtle.register_shape(shape)
        player.shape(shape)
    except turtle.TurtleGraphicsError:
        #If Turtle can't set the players shape
        print("WARNING: " + shape + " is probably missing or invalid")

    print("Player " + title + " is " + shape)
    
    #Setup player turtle
    player.penup()
    player.speed(config.MOVE_SPEED)
    playerpos = config.STARTPOS
    
    #Move to starting position
    (x, y) = find_cord(playerpos)
    x = x + offset
    player.setpos(x, y)
    return playerpos


def dice(move: int):
    """Sets dice shape to shape in config
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


def snake_ladder(pos: int, title: str) -> int:
    """Finds Position after snake or ladder, 
    returns old position if on same pos
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

    #If no ladders or snakes taken return old pos
    return(pos)

    
def turn(player: object, title: str, oldpos: int, offset: int, limit:int) -> int:
    """Runs players turn, 
    returns players new position
    """
    #Takes input
    print("\nPlayer " + title + " is starting on " + str(oldpos))
    esc = input("Player "+ title + " turn(press enter): ")
    #Generates random number
    move = random.randint(1, config.ROLL)
    #Sets dice shape
    dice(move)
    #Finds current position
    pos = move + oldpos

    #Roll player back if rollback is enabled 
    #and they don't get the exact number
    if pos > limit and config.ROLLBACK:
        #Finds amount over
        over = pos - limit
        #finds new position using amount over
        pos = limit - over
        print("You rolled over by " + str(over) + ", bouncing back to " + str(pos))
        if pos < 0:
            pos = 0

    if config.EVERY_SQUARE:
        #When True players stop on every square
        for i in range(oldpos, pos): 
            (x, y) = find_cord(i)
            x = x + offset
            player.setpos(x, y)

    #Move Player to current position   
    #When EVERY_SQUARE False(or ROLLBACK occurs) players 
    #move directly to square and don't stop on every one
    (x, y) = find_cord(pos)
    x = x + offset
    player.setpos(x, y)

    #Moves to new ladder/snake position if ladder/snake is taken        
    newpos = snake_ladder(pos, title)
    if newpos != pos:
        pos = newpos
        #Delay so that taking of the snake and ladder is clear
        time.sleep(config.DELAY)
        #Move to new position
        (x, y) = find_cord(pos)
        x = x + offset
        player.setpos(x, y)
    print("Player " + title +  " is on " + str(pos))
    return(pos)


def game_start(a_player_title: str, b_player_title: str) -> bool:
    """Starts one game, returns True if a_player has won
    """
    print("Rollback is: " + str(config.ROLLBACK))

    offset = config.SIZE//(config.GRID*5)
    limit = config.GRID ** 2 - 1

    #a_player setup
    a_player = turtle.Turtle()
    a_player_pos = player_setup(a_player, offset, config.A_PLAYER_SHAPE, a_player_title)

    #b_player setup
    b_player = turtle.Turtle()
    b_player_pos = player_setup(b_player, -offset, config.B_PLAYER_SHAPE, b_player_title)

    #diceTurtle setup
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(config.DICEPOS)

    while True:
        #aPlayer takes turn
        a_player_pos = turn(a_player, a_player_title, a_player_pos, offset, limit)
        if a_player_pos >= limit:
            #If aPlayer wins
            print("Player " + a_player_title +  " wins")
            return(True)
        #bPlayer takes turn
        b_player_pos = turn(b_player, b_player_title, b_player_pos, -offset, limit)
        if b_player_pos >= limit:
            #If bPlayer wins
            print("Player " + b_player_title +  " wins")
            return(False)


def main():
    """main function
    loops game until interupt or 'exit' is entered at end of game
    """
    #Setup screen and background
    turtle.screensize(config.SCREEN_SIZE[0], config.SCREEN_SIZE[1])
    turtle.bgcolor(config.BG_COLOR)
    #Draw Board
    draw_map()
    #Take player names
    a_player_title = input("Enter player A's name: \n")
    b_player_title = input("Enter player B's name: \n")
    a_player_wins = 0
    b_player_wins = 0
    esc = ""
    while esc != "exit":
        #Start game
        print("\nNEW GAME")
        a_win = game_start(a_player_title, b_player_title)

        if a_win:
            #If aPlayer wins increment a_player_wins
            a_player_wins = a_player_wins + 1
        else:
            #If bPlayer wins increment b_player_wins
            b_player_wins = b_player_wins + 1

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
        #Ensure win screen stays up for short time
        time.sleep(config.DELAY)
        
        #number of wins and input for exit
        print(a_player_title + " has won: " + str(a_player_wins))
        print(b_player_title + " has won: " + str(b_player_wins))
        esc = input("Type 'exit' to exit: \n")
main()
