#NOTE: Snakes and Ladders position will be offset by one verses the Coursework brief, 
#as the example(but not the spec) in the brief starts numbering from 1 instead of 0, 
#the positions of the snakes and ladders be changed in this config file

#Number of squares grid is across, any size of grid is possible, 
#so long as the numbers can fit in the squares
GRID = 5

#Starting Square this is the square that the game starts on(counting starts from 0)
STARTPOS = 0 

#Each entry is location of Snake on grid (Startpoint/TriggerSquare, Endpoint)
#any number of snakes is possible
SNAKES = [(7, 2), (19, 0), (23, 13)]

#Each entry is location of Ladder on grid (Startpoint/TriggerSquare, Endpoint)
#any number of ladders is possible
LADDERS = [(4, 14), (8, 11), (17,22)]


#Size and positions of grid appears as in turtle
SIZE = 500
GRIDPOS = (0, 0)

#Drawing/Move speed of all turtles
DRAW_SPEED = 0

#Delay when going Up/Down Ladder/Snake
DELAY = 0.25

#Shape Filenames
A_PLAYER_SHAPE = "shape.png"
B_PLAYER_SHAPE = "shape.png"
