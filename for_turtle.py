import turtle

# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# Keep asking for shape requests until the user enters "quit"
while True:
    # Ask the user for the shape and number of shapes to draw
    shape = input("What shape do you want to draw? (Type 'quit' to exit.) ")
    if shape == "quit":
        break
    num_shapes = int(input("How many of that shape do you want to draw? "))

    # Draw the shapes
    for i in range(num_shapes):
        if shape == "square":
            turtle.begin_fill()
            for j in range(4):
                turtle.forward(50)
                turtle.left(90)
            turtle.end_fill()
        elif shape == "circle":
            turtle.begin_fill()
            turtle.circle(25)
            turtle.end_fill()
        elif shape == "triangle":
            turtle.begin_fill()
            for j in range(3):
                turtle.forward(50)
                turtle.left(120)
            turtle.end_fill()
        else:
            print("Invalid shape.")
            break

        # Shift the turtle to the right for the next shape
        turtle.penup()
        turtle.forward(75)
        turtle.left(15)
        turtle.pendown()

# Keep the turtle window open until the user closes it
turtle.done()
