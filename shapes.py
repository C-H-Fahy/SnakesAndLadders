#AUTHOR: CHFahy
#CREATED: 2021-03-09
import turtle
    
def length_line(pos: tuple[int, int], length: int, angle: float):
    """Draws a line of length at the position and angle
    """
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)


def grid(left_corner: tuple[int, int], num_across: int, gap: int):
    """draws a grid
    args: 
        left_corner: position of grids left corner 
        num_across: number of squares across(eg, 5 for a 5*5)
        gap: size of one square
    """
    for i in range(0, num_across + 1):
        #Draw Horizontal Line
        length_line((left_corner[0], i*gap + left_corner[1]), gap*num_across, 0.00)
        #Draw Verticle Line
        length_line((i*gap + left_corner[0], left_corner[1]), gap*num_across, 90.00)


def write_number(pos: int, value: int):
    """writes value to pos
    """
    turtle.penup()
    turtle.setpos(pos)
    turtle.pendown()
    turtle.write(value)


def ladder(coming_from: tuple[int, int], to: tuple[int, int], width: int):
    """draws a ladder between the two positions
    """
    turtle.pensize(2)
    turtle.color("red")
    turtle.penup()
    turtle.setpos(coming_from)
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
    turtle.setpos(coming_from)
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


def snake(coming_from: tuple[int, int], to: tuple[int, int], width: int):
    """draws a snake between the two positions
    """
    turtle.penup()
    turtle.setpos(coming_from)
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


