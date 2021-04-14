#Squares start from 0 

#Number of squares grid is across, any size of grid is possible, 
#so long as the numbers and images can fit in the squares
GRID = 18

#Each entry is location of Snake on grid 
#Format is (Startpoint/TriggerSquare, Endpoint)
#any number of snakes is possible, Ladders have priority over snakes, 
#only one Snake/Ladder can be taken per turn
SNAKES = ((322, 67), (296, 22), (210, 96), (261, 2))

#Each entry is location of Ladder on grid 
#Format is (Startpoint/TriggerSquare, Endpoint)
#any number of ladders is possible
LADDERS = ((245, 320), (168, 220), (215, 268), (21, 158), (45, 166))

#if this is True the playerthe player needs to get exactly
#the right number from their position to the endsquare to
#win and if they don't(and it's True) they
#will go back the  number of spaces they rolled over
ROLLBACK = True

#Size and positions of grid appears as in turtle
SIZE = 750
GRIDPOS = (-375, -375)
DICEPOS = (-400, -400)
SCREEN_SIZE = (850, 850)
BG_COLOR = "#ffffe6"

#Drawing/Move speed of drawing turtle
DRAW_SPEED = 0
#Determine if Turtles animinations are on while drawing
DRAW_TRACER = False
#Move speed of characters
MOVE_SPEED = 0

#Delay when going Up/Down Ladder/Snake
DELAY = 0.25

#Starting Square this is the square that the game starts on
#(counting starts from 0)
STARTPOS = 0 

#Max roll
ROLL = 6

#Shape Filenames
A_PLAYER_SHAPE = "bull.gif"
B_PLAYER_SHAPE = "cow.gif"
DICE = ("dice1.gif", "dice2.gif", "dice3.gif", "dice4.gif", "dice5.gif", "dice6.gif")
WIN_SHAPE = "win.gif"
