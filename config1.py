#NOTE: Snakes and Ladders position will be offset by one verses the Coursework brief, 
#as the example(but not the spec) in the brief starts numbering from 1 instead of 0, 
#the positions of the snakes and ladders be changed in this config file

#Number of squares grid is across, any size of grid is possible, 
#so long as the numbers and images can fit in the squares
GRID = 31

#Each entry is location of Snake on grid (Startpoint/TriggerSquare, Endpoint)
#any number of snakes is possible
SNAKES = [(868, 30), (7, 2), (15, 5)]

#Each entry is location of Ladder on grid (Startpoint/TriggerSquare, Endpoint)
#any number of ladders is possible
LADDERS = [(4, 899), (8, 11), (17,22)]


#Size and positions of grid appears as in turtle
SIZE = 750
GRIDPOS = (-330, -330)
DICEPOS = (-340, -340)

#Drawing/Move speed of all turtles
DRAW_SPEED = 0
MOVE_SPEED = 0

#Delay when going Up/Down Ladder/Snake
DELAY = 0.25

#Starting Square this is the square that the game starts on(counting starts from 0)
STARTPOS = 0 

#Max roll
ROLL = 6

#Shape Filenames
A_PLAYER_SHAPE = "bull.gif"
B_PLAYER_SHAPE = "cow.gif"
DICE = ["dice1.gif", "dice2.gif", "dice3.gif", "dice4.gif", "dice5.gif", "dice6.gif"]
