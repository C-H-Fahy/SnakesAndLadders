#AUTHOR: CHFahy
#CREATED: 2021-03-09
import turtle
def line(x, y):
    """Draws a line between 2 cords"""
    turtle.penup()
    turtle.setpos(x)
    turtle.pendown()
    turtle.setpos(y)
    
    
def LengthLine(pos, length, angle):
    """Draws a line of SIZE of grid at the position and angle inputed"""
    turtle.penup()
    turtle.setpos(pos[0], pos[1])
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)
    
    
def ladder(comingFrom, to, width):
    """draws a ladder between the two positions"""
    turtle.pensize(2)
    turtle.color("red")
    turtle.penup()
    turtle.setpos(comingFrom)
    length = turtle.distance(to)
    direction = turtle.towards(to)
    
    turtle.setheading(direction)
    turtle.left(90)
    turtle.forward(width/2)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()
 
    turtle.setpos(comingFrom)
    turtle.setheading(direction)
    turtle.right(90)
    turtle.forward(width/2)
    
    turtle.setheading(direction)
    turtle.pendown()
    

    for i in range(1, 5):
        turtle.forward(length//5)
        turtle.left(90)
        turtle.forward(width)
        turtle.backward(width)
        turtle.setheading(direction)
    turtle.forward(length//5)
    turtle.pensize(1)
    
    
def snake(comingFrom, to, width):
    """draws a snake between the two positions"""
    turtle.color("green")
    line(comingFrom, to)
    turtle.color("#000000")

