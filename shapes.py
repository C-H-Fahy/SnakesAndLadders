#AUTHOR: CHFahy
#CREATED: 2021-03-09
import turtle
import math

def CordToVector(a, b):
    deltax = a[0] - b[0]
    deltay = a[1] - b[1]
    
    #Finds Direction in radians(converted when return)
    try:
        direction = math.atan(deltax/deltay)
    except ZeroDivisionError:
        #In radians because math uses radians
        direction = 1.5708

    #Finds Magnitude
    mag = math.sqrt((deltax ** 2)*(deltay ** 2))
    if mag == 0:
        if abs(deltax) > abs(deltay):
            mag = -deltax
        else:
            mag = -deltay
    
    return(math.degrees(direction), mag)
    
def midpoint(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

def line(x, y):
    """Draws a line between 2 cords"""
    turtle.penup()
    turtle.setpos(x)
    turtle.pendown()
    turtle.setpos(y)
    
def VertLine(pos, length):
    """Draws a verticle line of  SIZE of grid at the position inputed"""
    turtle.penup()
    turtle.setpos(pos[0], pos[1])
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(length)
    
def HoriLine(pos, length):
    """Draws a horizontal line of  length of grid at the position inputed"""
    turtle.penup()
    turtle.setpos(pos[0], pos[1])
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(length)
    
def ladder(comingFrom, to, width):
    """draws a ladder between the two positions"""
    turtle.color("red")
    
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

def snake(comingFrom, to, width):
    """draws a snake between the two positions"""
    turtle.color("green")
    line(comingFrom, to)
    turtle.color("#000000")

