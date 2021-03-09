#AUTHOR: CHFahy

#External
import turtle
import time
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
    gap = 500//constants.GRID
    a = 0
    for i in range(0, constants.GRID):
        y = gap * i + gap/2
        for i in range(0, constants.GRID):
            x = gap * i + gap/2
            if a == n:
                return (x, y)
                print(x, y)
            a = a + 1

def drawmap():
    """Draws Out All The Fixed Stuff"""
    gap = 500//constants.GRID
    #Drawing        
    for i in range(0, constants.GRID+1):
        vertline(i*gap)
        horiline(i*gap)
        
    for i in range(0, constants.GRID*constants.GRID):
        turtle.penup()
        turtle.setpos(findpos(i))
        turtle.pendown()
        turtle.write(i)

def main():
    drawmap()

turtle.screensize(1000, 1000)
main()

a = input()
