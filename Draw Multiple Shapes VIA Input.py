import turtle
#Draws the square shape based on user input to variable.
def draw_square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    
#Draws the triangle shape based on user input to variable.
def draw_triangle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

#Draws "rocket" based on user input for starting position variable.
def draw_rocket(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(142)
    turtle.left(90)
    turtle.forward(142)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)

#A while loop determines to continue drawing shapes and their starting position based on user input, if Q is typed in, then the loop ends.
while True:
    shape = input("What would you like to draw? (S)quare, (T)riangle, (R)ocket, (Q)uit: ").upper()
    
    if shape == 'Q':
        break
    
    x = int(input("Where would you like to draw it along the X axis?: "))
    y = int(input("Where would you like to draw it along the Y axis?: "))
    
    if shape == 'S':
        draw_square(x, y)
    elif shape == 'T':
        draw_triangle(x, y)
    elif shape == 'R':
        draw_rocket(x, y)
    
turtle.done()
