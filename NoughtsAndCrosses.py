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

def drawgrid(startpoint):
    for i in range(0, constants.GRID+1):
        vertline(i*(500//constants.GRID))
        horiline(i*(500//constants.GRID))
      
turtle.screensize(1000, 1000)  
        
drawgrid(0)
a = input()

