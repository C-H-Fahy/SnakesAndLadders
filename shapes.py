#AUTHOR: CHFahy
#CREATED: 2021-03-09
import turtle
    
def LengthLine(pos, length, angle):
    """Draws a line of SIZE of grid at the position and angle inputed"""
    turtle.penup()
    turtle.setpos(pos[0], pos[1])
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)

def WriteNumber(value, pos, offset):
        turtle.penup()
        turtle.setpos(pos[0] - offset, pos[1] + offset)
        turtle.pendown()
        turtle.write(value)
    
    
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
    turtle.color("black")
    
def snake(comingFrom, to, width):
    """draws a snake between the two positions"""
    turtle.pensize(width*2)
    turtle.penup()
    turtle.setpos(comingFrom)
    direction = turtle.towards(to)
    length = turtle.distance(to)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.pensize((width//4)*2)
    turtle.color("pink")
    turtle.forward(width*2)
    turtle.color("green")
    turtle.pensize((width//2)*2)
    LengthLine(turtle.pos(), length - width*4, direction)
    turtle.color("black")

