#AUTHOR: CHFahy

#External
import turtle
import time
import random
#Internal
import constants

def vertline(x):
    """draws a verticle line of  500"""
    turtle.penup()
    turtle.setpos(x, 0)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(500)

def horiline(y):
    """draws a horizontal line of  500"""
    turtle.penup()
    turtle.setpos(0, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(500)
    
def findpos(n):
    """Finds centre of square, returns None if square does not exist"""
    gap = 500//constants.GRID
    a = 0
    for i in range(0, constants.GRID):
        y = gap * i + gap/2
        for i in range(0, constants.GRID):
            x = gap * i + gap/2
            if a == n:
                return (x, y)
            a = a + 1

def DrawMap():
    """Draws Out All The Fixed Stuff"""
    turtle.speed(constants.DRAW_SPEED)
    gap = 500//constants.GRID
    #Draw Grid        
    for i in range(0, constants.GRID+1):
        vertline(i*gap)
        horiline(i*gap)
    #Draw Numbers
    for i in range(0, constants.GRID*constants.GRID):
        turtle.penup()
        turtle.setpos(findpos(i))
        turtle.pendown()
        turtle.write(i)

def turn(player, title, pos, offset):
    esc = input("Player "+ title + " turn")
    move = random.randint(1, 6)
    print(move)
    try: 
        pos = move + pos
        player.setpos(findpos(pos))
    except TypeError:
        #When findpos returns None
        pos = constants.GRID * constants.GRID - 1
        player.setpos(findpos(pos))
    return(pos)
    

def GameStart():
    aPlayer = turtle.Turtle()
    bPlayer = turtle.Turtle()
    aPlayer.penup()
    bPlayer.penup()
    
    aPlayerpos = constants.STARTPOS
    bPlayerpos = constants.STARTPOS
    aPlayer.speed(constants.DRAW_SPEED)
    bPlayer.speed(constants.DRAW_SPEED)
    aPlayer.setpos(findpos(aPlayerpos))
    bPlayer.setpos(findpos(bPlayerpos))
    limit = constants.GRID * constants.GRID - 1

    while True:
        aPlayerpos = turn(aPlayer, "A", aPlayerpos, +10)
        #bPlayerpos = turn(bPlayer, "A", bPlayerpos, +10)
        if aPlayerpos >= limit:
            print("Player A wins")
            break
        if bPlayerpos >= limit:
            print("Player B wins")
            break

def main():
    DrawMap()
    GameStart()

turtle.screensize(1000, 1000)
main()

a = input()
