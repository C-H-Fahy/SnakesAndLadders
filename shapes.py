#AUTHOR: CHFahy
#CREATED: 2021-03-09
import turtle
import config
import math

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

def line(a, b):
    """Draws a line between 2 cords"""
    turtle.penup()
    turtle.setpos(a)
    turtle.pendown()
    turtle.setpos(b)
    
def midpoint(a, b):
    return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    
def ladder(comingFrom, to):
    """draws a ladder between the two positions"""
    width = 100//config.GRID
    turtle.color("red")
    #Draw first line of truss
    a = (comingFrom[0] + width, comingFrom[1])
    b = (to[0]+ width, to[1])
    c = (comingFrom[0] - width, comingFrom[1])
    d = (to[0] - width, to[1])
    
    #Draw first line of truss
    line(a, b)

    #Draw second line of truss
    line(c, d)
    
    #Add steps to ladder
    e = midpoint(a, b)
    f = midpoint(c, d)
    line(e, f)
    e = midpoint(a, e)
    f = midpoint(c, f)
    line(e, f)
    e = midpoint(midpoint(a, b), b)
    f = midpoint(midpoint(c, d), d)
    line(e, f)
    
    turtle.color("#000000")

def snake(comingFrom, to):
    """draws a snake between the two positions"""
    width = 150//config.GRID
    turtle.color("green")
    line(comingFrom, to)
    turtle.color("#000000")
