#AUTHOR: CHFahy
#CREATED: 2021-03-09
import turtle
    
def length_line(pos: tuple(int, int), length: int, angle: int):
    """Draws a line of SIZE of grid at the position and angle inputed
    
    returns: none
    """
    turtle.penup()
    turtle.setpos(pos[0], pos[1])
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)


def write_number(pos: tuple(int, int), value: int):
    """Writes value to pos
    
    returns: none
    """
    turtle.penup()
    turtle.setpos(pos[0], pos[1])
    turtle.pendown()
    turtle.write(value)


def ladder(comingFrom: tuple(int, int), to: tuple(int, int), width: float):
    """Draws a ladder between the two positions 
    
    returns: none
    """
    turtle.pensize(2)
    turtle.color("red")
    turtle.penup()
    turtle.setpos(comingFrom)
    length = turtle.distance(to)
    direction = turtle.towards(to)

    #Draws one side of ladder
    turtle.setheading(direction)
    turtle.left(90)
    turtle.forward(width/2)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()
    
    #Draws other side of ladder and steps
    turtle.setpos(comingFrom)
    turtle.setheading(direction)
    turtle.right(90)
    turtle.forward(width/2)
    
    turtle.setheading(direction)
    turtle.pendown()
    for i in range(1, 5):
        turtle.forward(length/5)
        turtle.left(90)
        turtle.forward(width)
        turtle.backward(width)
        turtle.setheading(direction)
    turtle.forward(length/5)
    #Reset Turtle
    turtle.pensize(1)
    turtle.color("black")


def snake(comingFrom: tuple(int, int), to: tuple(int, int), width: float):
    """draws a snake between the two positions
    
    returns: none
    """
    turtle.penup()
    turtle.setpos(comingFrom)
    direction = turtle.towards(to)
    length = turtle.distance(to)
    turtle.setheading(direction)
    turtle.pendown()
    #Draws Tongue 
    turtle.pensize(width*0.90)
    turtle.color("pink")
    turtle.forward(width*2)
    #Set colour light green
    turtle.color("#00ff00")
    #Draws Head
    turtle.pensize(width*3)
    turtle.forward(width)
    #Draws Body
    turtle.pensize(width)
    turtle.forward(length - width*4)
    #Reset Turtle
    turtle.pensize(1)
    turtle.color("black")


