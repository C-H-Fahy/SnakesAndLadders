#AUTHOR: CHFahy
#CREATED: 2021-03-08

#External modules
import turtle
import time
import random

#Internal modules
import config

def VertLine(x):
    """Draws a verticle line of  500"""
    turtle.penup()
    turtle.setpos(x, 0)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(500)

def HoriLine(y):
    """Draws a horizontal line of  500"""
    turtle.penup()
    turtle.setpos(0, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(500)

def FindPos(n):
    """Finds centre of square, returns None if square does not exist"""
    gap = 500//config.GRID
    a = 0
    for i in range(0, config.GRID):
        y = gap * i + gap/2
        for i in range(0, config.GRID):
            x = gap * i + gap/2
            if a == n:
                return (x, y)
            a = a + 1

def DrawMap():
    """Draws Out All The Fixed Stuff"""
    turtle.speed(config.DRAW_SPEED)
    turtle.hideturtle()
    gap = 500//config.GRID
    #Draw Grid        
    for i in range(0, config.GRID+1):
        VertLine(i*gap)
        HoriLine(i*gap)
    #Draw Numbers
    for i in range(0, config.GRID*config.GRID):
        turtle.penup()
        turtle.setpos(FindPos(i))
        turtle.pendown()
        turtle.write(i)

def PlayerSetup(player, offset):
    """Sets up player, returns players position"""
    player.penup()
    player.speed(config.DRAW_SPEED)
    playerpos = config.STARTPOS
    (x, y) = FindPos(playerpos)
    x = x + offset
    player.setpos(x, y)
    return playerpos

def turn(player, title, pos, offset):
    """Runs players turn, returns players new position"""
    esc = input("Player "+ title + " turn:\n")
    move = random.randint(1, 6)
    print(move)
    try: 
        pos = move + pos
        (x, y) = FindPos(pos)
        x = x + offset
        player.setpos(x, y)
    except TypeError:
        #When FindPos returns None
        pos = config.GRID * config.GRID - 1
        (x, y) = FindPos(pos)
        x = x + offset
        player.setpos(x, y)
        
    #Check to see if player is on Ladder and move them if they are
    for i in range (0,len(config.LADDERS)):
        if pos == config.LADDERS[i][0]:
            print(title + " gets ladder from " + str(config.LADDERS[i][0]) + " to " + 
            str(config.LADDERS[i][1]))
            time.sleep(0.5)
            pos = config.LADDERS[i][1]
            (x, y) = FindPos(pos)
            x = x + offset
            player.setpos(x, y)
            
    #Check to see if player is on Snake and move them if they are
    for i in range (0,len(config.SNAKES)):
        if pos == config.SNAKES[i][0]:
            print(title + " gets snake from " + str(config.SNAKES[i][0]) + " to"  + 
            str(config.SNAKES[i][1]))
            time.sleep(0.5)
            pos = config.SNAKES[i][1]
            (x, y) = FindPos(pos)
            x = x + offset
            player.setpos(x, y)
            
    return(pos)

def GameStart():
    offset = 100//config.GRID
    limit = config.GRID * config.GRID - 1

    #aPlayer setup
    aPlayer = turtle.Turtle()
    aPlayerpos = PlayerSetup(aPlayer, offset)

    #bPlayer setup
    bPlayer = turtle.Turtle()
    bPlayerpos = PlayerSetup(bPlayer, -offset)

    while True:
        aPlayerpos = turn(aPlayer, "A", aPlayerpos, offset)
        if aPlayerpos >= limit:
            print("Player A wins")
            break

        bPlayerpos = turn(bPlayer, "B", bPlayerpos, -offset)
        if bPlayerpos >= limit:
            print("Player B wins")
            break

def main():
    DrawMap()
    GameStart()

turtle.screensize(1000, 1000)
main()
a = input()
