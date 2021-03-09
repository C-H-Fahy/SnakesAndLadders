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

def drawmap():
    """Draws Out All The Fixed Stuff, Outputs list with the centres of Squares"""
    gap = 500//constants.GRID
    #Finds positions of all squares 
    positions = []
    for i in range(0, constants.GRID):
        y = gap * i + gap/2
        for i in range(0, constants.GRID):
            x = gap * i + gap/2
            positions.append((x, y))

    #Drawing        
    for i in range(0, constants.GRID+1):
        vertline(i*gap)
        horiline(i*gap)
        
    for i in range(0, len(positions)):
        turtle.penup()
        turtle.setpos(positions[i])
        turtle.pendown()
        turtle.write(i)
 
    return(positions)

def main():
    positions = drawmap()
    print(positions)

turtle.screensize(1000, 1000)
main()

a = input()
